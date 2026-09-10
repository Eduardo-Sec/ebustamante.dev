/* Playbook behaviour.

   Three independent features, all of them purely client side.

     1. Position highlight, one offense and one defense at a time.
     2. Play filters, multi select inside a category and AND across categories.
     3. Beginner explainers, open them all or leave them collapsed.

   Security notes for future me.
     - Every value written into an attribute or compared against the DOM comes
       from an allow list built out of what Django actually rendered. Nothing
       from localStorage, the URL or the DOM is trusted directly, so a tampered
       storage value is dropped rather than used.
     - No innerHTML, no eval, no string built selectors, no query parameters.
     - Loaded externally with defer, so there is no inline script to nonce and
       the strict script-src stays intact. */
(function () {
  "use strict";

  var root = document.querySelector(".pb");
  if (!root) { return; }

  function store(key, value) {
    try {
      if (value) { localStorage.setItem(key, value); }
      else { localStorage.removeItem(key); }
    } catch (e) { /* private mode or storage disabled */ }
  }

  function read(key) {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  }

  /* --------------------------------------------------- 1. position highlight */
  (function positions() {
    var chips = Array.prototype.slice.call(root.querySelectorAll(".pb-chip[data-p]"));
    if (!chips.length) { return; }

    var GROUPS = { off: "data-off", def: "data-def" };
    var KEYS = { off: "pb-pos-off", def: "pb-pos-def" };
    var allowed = { off: [], def: [] };

    chips.forEach(function (b) {
      var g = b.getAttribute("data-g");
      var p = b.getAttribute("data-p");
      if (allowed[g] && p && allowed[g].indexOf(p) === -1) { allowed[g].push(p); }
    });

    function valid(group, value) {
      return typeof value === "string"
        && Object.prototype.hasOwnProperty.call(allowed, group)
        && allowed[group].indexOf(value) !== -1;
    }

    function paint(group) {
      var current = root.getAttribute(GROUPS[group]);
      chips.forEach(function (b) {
        if (b.getAttribute("data-g") !== group) { return; }
        b.setAttribute("aria-pressed", b.getAttribute("data-p") === current ? "true" : "false");
      });
    }

    function set(group, value) {
      if (value !== null && !valid(group, value)) { return; }
      if (value) { root.setAttribute(GROUPS[group], value); }
      else { root.removeAttribute(GROUPS[group]); }
      store(KEYS[group], value);
      paint(group);
    }

    chips.forEach(function (b) {
      b.addEventListener("click", function () {
        var g = b.getAttribute("data-g");
        var p = b.getAttribute("data-p");
        if (!Object.prototype.hasOwnProperty.call(GROUPS, g)) { return; }
        set(g, root.getAttribute(GROUPS[g]) === p ? null : p);
      });
    });

    var clear = root.querySelector(".pb-clear");
    if (clear) {
      clear.addEventListener("click", function () { set("off", null); set("def", null); });
    }

    ["off", "def"].forEach(function (g) {
      var saved = read(KEYS[g]);
      if (valid(g, saved)) { set(g, saved); }
      else { store(KEYS[g], null); paint(g); }
    });
  }());

  /* --------------------------------------------------------- 2. play filters */
  (function filters() {
    var chips = Array.prototype.slice.call(root.querySelectorAll(".pb-fchip[data-f]"));
    var cards = Array.prototype.slice.call(root.querySelectorAll(".pb-play[data-depth]"));
    if (!chips.length || !cards.length) { return; }

    var KEY = "pb-play-filters";
    var counter = root.querySelector(".pb-count");
    var groups = root.querySelectorAll(".pb-pgroup");
    var index = Array.prototype.slice.call(root.querySelectorAll(".pb-idx[data-for]"));

    /* attribute each filter category reads off a play card */
    var ATTR = { depth: "data-depth", family: "data-family", form: "data-form",
                 beats: "data-beats", situ: "data-situ" };

    /* allow list of key:value pairs, straight off the rendered buttons */
    var allowed = [];
    chips.forEach(function (b) {
      var k = b.getAttribute("data-f");
      var v = b.getAttribute("data-v");
      if (Object.prototype.hasOwnProperty.call(ATTR, k) && v) { allowed.push(k + ":" + v); }
    });

    var active = [];   // array of "key:value" strings

    function tokens(card, key) {
      /* pipe separated, because values like "cover 2" contain spaces */
      var raw = card.getAttribute(ATTR[key]) || "";
      return raw.split("|").filter(Boolean);
    }

    function matches(card) {
      /* OR inside a category, AND across categories */
      var keys = Object.keys(ATTR);
      for (var i = 0; i < keys.length; i += 1) {
        var key = keys[i];
        var wanted = active
          .filter(function (t) { return t.indexOf(key + ":") === 0; })
          .map(function (t) { return t.slice(key.length + 1); });
        if (!wanted.length) { continue; }
        var have = tokens(card, key);
        var hit = wanted.some(function (w) { return have.indexOf(w) !== -1; });
        if (!hit) { return false; }
      }
      return true;
    }

    function apply() {
      var shown = 0;
      cards.forEach(function (card) {
        var on = matches(card);
        card.classList.toggle("pb-hidden", !on);
        if (on) { shown += 1; }
      });

      index.forEach(function (a) {
        var target = document.getElementById(a.getAttribute("data-for"));
        a.classList.toggle("pb-hidden", !target || target.classList.contains("pb-hidden"));
      });

      Array.prototype.forEach.call(groups, function (sec) {
        var live = sec.querySelectorAll(".pb-play:not(.pb-hidden)").length;
        sec.classList.toggle("pb-hidden", live === 0);
      });

      chips.forEach(function (b) {
        var token = b.getAttribute("data-f") + ":" + b.getAttribute("data-v");
        b.setAttribute("aria-pressed", active.indexOf(token) !== -1 ? "true" : "false");
      });

      if (counter) {
        counter.setAttribute("aria-live", "polite");
        var total = counter.getAttribute("data-total") || String(cards.length);
        counter.textContent = active.length
          ? "showing " + shown + " of " + total
          : "showing all " + total;
      }

      var empty = root.querySelector(".pb-empty");
      if (empty) { empty.classList.toggle("pb-hidden", shown !== 0); }

      store(KEY, active.length ? active.join("|") : null);
    }

    chips.forEach(function (b) {
      b.addEventListener("click", function () {
        var token = b.getAttribute("data-f") + ":" + b.getAttribute("data-v");
        if (allowed.indexOf(token) === -1) { return; }
        var at = active.indexOf(token);
        if (at === -1) { active.push(token); } else { active.splice(at, 1); }
        apply();
      });
    });

    var reset = root.querySelector(".pb-freset");
    if (reset) { reset.addEventListener("click", function () { active = []; apply(); }); }

    var saved = read(KEY);
    if (typeof saved === "string" && saved) {
      saved.split("|").forEach(function (t) {
        if (allowed.indexOf(t) !== -1 && active.indexOf(t) === -1) { active.push(t); }
      });
    }
    apply();

    /* if a filter is live, open the panel so nobody wonders where the plays went */
    var panel = document.getElementById("playfilters");
    if (panel && active.length) { panel.open = true; }
  }());

  /* --------------------------------------------------- 3. beginner explainers */
  (function basics() {
    var toggle = root.querySelector(".pb-basics-toggle");
    if (!toggle) { return; }
    var KEY = "pb-basics";
    var blocks = Array.prototype.slice.call(root.querySelectorAll("details.pb-basics"));

    function set(on) {
      blocks.forEach(function (d) { d.open = on; });
      toggle.setAttribute("aria-pressed", on ? "true" : "false");
      toggle.textContent = on ? "hide the basics" : "explain the basics";
      store(KEY, on ? "1" : null);
    }

    toggle.addEventListener("click", function () {
      set(toggle.getAttribute("aria-pressed") !== "true");
    });

    set(read(KEY) === "1");
  }());

  /* ------------------------------------------- 4. card collapse on small screens */
  (function collapse() {
    var togs = Array.prototype.slice.call(root.querySelectorAll(".pb-tog"));
    if (!togs.length) { return; }

    /* The markup ships expanded so that with no JavaScript the whole card is
       readable. Only once we know the script is running do we start hiding
       things, and only on a narrow screen. */
    root.classList.add("pb-js");

    var KEY = "pb-cards";
    var narrow = window.matchMedia("(max-width: 759px)");
    var globalBtn = root.querySelector(".pb-expand");

    function body(tog) {
      var el = tog.nextElementSibling;
      return el && el.classList.contains("pb-more") ? el : null;
    }

    function setOne(tog, open) {
      var el = body(tog);
      if (!el) { return; }
      el.classList.toggle("pb-collapsed", !open);
      tog.setAttribute("aria-expanded", open ? "true" : "false");
    }

    function setAll(open, remember) {
      togs.forEach(function (t) { setOne(t, open); });
      if (globalBtn) {
        globalBtn.setAttribute("aria-pressed", open ? "true" : "false");
        globalBtn.textContent = open ? "collapse every card" : "expand every card";
      }
      if (remember) { store(KEY, open ? "open" : "shut"); }
    }

    togs.forEach(function (t) {
      t.addEventListener("click", function () {
        setOne(t, t.getAttribute("aria-expanded") !== "true");
      });
    });

    if (globalBtn) {
      globalBtn.addEventListener("click", function () {
        setAll(globalBtn.getAttribute("aria-pressed") !== "true", true);
      });
    }

    /* A saved choice wins. Otherwise collapse on a phone and leave a desktop
       alone, because a desktop has the room. */
    var saved = read(KEY);
    if (saved === "open" || saved === "shut") { setAll(saved === "open", false); }
    else { setAll(!narrow.matches, false); }

    /* If somebody rotates the phone or resizes, follow the viewport again,
       but never override a choice they made by hand. */
    var onChange = function () {
      if (read(KEY)) { return; }
      setAll(!narrow.matches, false);
    };
    if (narrow.addEventListener) { narrow.addEventListener("change", onChange); }
    else if (narrow.addListener) { narrow.addListener(onChange); }

    /* Opening a card the URL points at, so a shared #p-flood link is readable
       the moment it lands. */
    function openHashTarget() {
      var id = window.location.hash.slice(1);
      if (!id) { return; }
      var card = document.getElementById(id);
      if (!card) { return; }
      var tog = card.querySelector(".pb-tog");
      if (tog) { setOne(tog, true); }
      card.classList.remove("pb-hidden");
      card.scrollIntoView();
    }
    openHashTarget();
    window.addEventListener("hashchange", openHashTarget);
  }());

  /* --------------------------------------------------------- 5. back to top */
  (function toTop() {
    var btn = root.querySelector(".pb-totop") || document.querySelector(".pb-totop");
    if (!btn) { return; }
    var ticking = false;
    function check() {
      btn.classList.toggle("pb-show", window.pageYOffset > 900);
      ticking = false;
    }
    window.addEventListener("scroll", function () {
      if (ticking) { return; }
      ticking = true;
      window.requestAnimationFrame(check);
    }, { passive: true });
    btn.addEventListener("click", function () {
      window.scrollTo(0, 0);
      var first = root.querySelector(".pb-chip");
      if (first) { first.focus(); }
    });
    check();
  }());

  /* ------------------------------------------------------------- 6. printing */
  (function printing() {
    var btn = root.querySelector(".pb-print");
    if (btn) {
      btn.addEventListener("click", function () {
        /* never print a collapsed card */
        Array.prototype.forEach.call(root.querySelectorAll(".pb-more"), function (el) {
          el.classList.remove("pb-collapsed");
        });
        window.print();
      });
    }
  }());

  /* --------------------------------------------------- 7. custom cursor */
  (function cursor() {
    /* Matches main.js's implementation so a reader moving between the main
       site and the playbook sees the same pointer. Self contained, no
       dependency on main.js or anything outside this page, because the
       #cursor-* CSS rules and the (pointer: coarse) fallback that restores
       the native cursor on touch devices already ship in main.css. */
    if (window.matchMedia("(pointer: coarse)").matches) { return; }

    var dot = document.getElementById("cursor-dot");
    var bracket = document.getElementById("cursor-bracket");
    var dataEl = document.getElementById("cursor-data");
    var valX = document.getElementById("val-x");
    var valY = document.getElementById("val-y");
    if (!dot || !bracket || !dataEl || !valX || !valY) { return; }

    document.body.style.cursor = "none";

    var mouseX = 0, mouseY = 0, dataX = 0, dataY = 0;

    function pad(n) { return String(Math.round(n)).padStart(4, "0"); }

    document.addEventListener("mousemove", function (e) {
      mouseX = e.clientX;
      mouseY = e.clientY;
      dot.style.left = mouseX + "px";
      dot.style.top = mouseY + "px";
      bracket.style.left = mouseX + "px";
      bracket.style.top = mouseY + "px";
      valX.textContent = pad(mouseX);
      valY.textContent = pad(mouseY);
    });

    function lerp(a, b, t) { return a + (b - a) * t; }

    function animate() {
      dataX = lerp(dataX, mouseX, 0.15);
      dataY = lerp(dataY, mouseY, 0.15);
      dataEl.style.left = dataX + "px";
      dataEl.style.top = dataY + "px";
      window.requestAnimationFrame(animate);
    }
    animate();

    document.addEventListener("mouseleave", function () {
      dot.style.opacity = "0";
      dataEl.style.opacity = "0";
      bracket.style.opacity = "0";
    });

    document.addEventListener("mouseenter", function (e) {
      mouseX = e.clientX;
      mouseY = e.clientY;
      dot.style.left = mouseX + "px";
      dot.style.top = mouseY + "px";
      bracket.style.left = mouseX + "px";
      bracket.style.top = mouseY + "px";
      dataX = mouseX;
      dataY = mouseY;
      dot.style.opacity = "1";
      dataEl.style.opacity = "1";
      bracket.style.opacity = "1";
    });

    document.addEventListener("mousedown", function () {
      dot.style.transform = "translate(-50%, -50%) scale(2.5)";
    });

    document.addEventListener("mouseup", function () {
      dot.style.transform = "translate(-50%, -50%) scale(1)";
    });

    Array.prototype.forEach.call(root.querySelectorAll("a, button"), function (el) {
      el.addEventListener("mouseenter", function () {
        dot.style.transform = "translate(-50%, -50%) scale(2.5)";
        dot.style.background = "#34d399";
      });
      el.addEventListener("mouseleave", function () {
        dot.style.transform = "translate(-50%, -50%) scale(1)";
        dot.style.background = "#059669";
      });
    });
  }());
}());
