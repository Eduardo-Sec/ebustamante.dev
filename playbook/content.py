"""Prose, rules and reference tables for the playbook pages."""

OFF_POS = [
    ("QB", "Quarterback",
     "Reads coverage before the snap and gets through three reads in three seconds. "
     "He can run whenever he wants, and nobody is allowed to touch him."),
    ("C", "Center",
     "Snaps it clean two or more yards back, then releases as a real receiver. The center "
     "is eligible in this league and he is open more often than anyone."),
    ("X", "Split end, wide left, on the line",
     "Our best one on one route runner. Usually the isolated receiver in trips."),
    ("Z", "Flanker, wide right, on the line",
     "Deep threat. Runs most of the corners and the posts."),
    ("Y", "Inside receiver, on the line",
     "Works the middle of the field, digs, snags and shallow crossers. Has to be willing "
     "to catch it in traffic."),
    ("H", "Slot, off the line",
     "Our motion man and our fastest player in space. Jets, wheels, bubbles, and the "
     "second thrower on trick plays."),
    ("R", "Back, off the line",
     "Checkdown, swing routes, the direct snap package, and the guy who has to sell "
     "every run fake."),
]

DEF_POS = [
    ("E", "Edge rusher", "Arcs around, keeps contain, and never touches the quarterback."),
    ("M", "Mike", "Hook zone in the middle, man on the inside receiver, and the Tampa 2 runner."),
    ("N", "Nickel", "Mirror of M on the other side. Also the second rusher on pressure calls."),
    ("CL", "Corner, left", "Flat in Cover 2, deep third in Cover 3, man on the widest receiver."),
    ("CR", "Corner, right", "Mirror of CL."),
    ("FS", "Free safety", "Deep half, deep middle, or centre field in man. Never gets beaten deep."),
    ("SS", "Strong safety", "Deep half in zone, robber and quarterback spy in man."),
]

RULES = [
    ("Twenty yards is a first down, not ten",
     "Four downs to reach the next zone line, the 20, the 40, the other 20. That is five "
     "yards a play just to stay alive. Every series needs at least one chunk play, which is "
     "why half this playbook is built to gain 12 or more on a single snap."),
    ("Shotgun only, and the snap has rules",
     "The ball has to travel at least two yards. No direct snap to the quarterback, no snap "
     "to anyone standing on the line, and no snap to a man in motion. Four of us have to be "
     "on the line at the snap, and ours are always C, X, Y and Z."),
    ("Everybody freezes for one full second",
     "All seven of us have to be motionless for a second before the snap, in a two point "
     "stance, with only one man in motion at a time. This is the penalty we will get flagged "
     "for most often. Count it out loud in warm ups."),
    ("One forward pass, unlimited backward ones",
     "We only get one forward pass per down, and a completed pass behind the line still uses "
     "it up. Pitches and laterals going backward are free, and that is the entire basis of "
     "our trick play package."),
    ("A dropped lateral is not a turnover",
     "A fumble is dead the moment it touches the ground and <strong>the team that fumbled "
     "keeps the ball</strong>. The next play starts from where it landed. A botched pitch "
     "costs us yards, never possession, so trick plays here are far cheaper than they are in "
     "real football."),
    ("Nobody may touch our quarterback",
     "Any contact with the QB is roughing the passer, ten yards and an automatic first down. "
     "Our quarterback can stand in the pocket and let routes develop. Our rushers have to arc "
     "around and go for the flag, never the body."),
    ("No rush requirement, no run restrictions",
     "The rules do not force the defense to rush, and they do not force the quarterback to be "
     "rushed before he runs. That cuts both ways. Teams will drop seven and dare us to throw, "
     "which is exactly when we run the draw."),
    ("We cannot block with our hands",
     "Screen blocking only, hands behind the back or crossed on the chest. Downfield blockers "
     "have to be set and stationary before the runner passes them, and any intentional contact "
     "is ten yards. In practice that means get to your spot early and freeze."),
    ("No flag guarding, no hurdling, no diving to advance",
     "Ball carriers may not swat at a defender's arm, stiff arm, run bent over, or lower their "
     "head. You may only dive to catch a pass. Spinning and jumping are legal, so spin instead "
     "of stiff arming."),
    ("The spot is where the ball is, not where the flags are",
     "Extending the ball forward at the zone line is worth real yards. Just do not leave your "
     "feet doing it."),
    ("Extra points are worth one, two or three",
     "Three yards is 1 point, ten yards is 2, twenty yards is 3. An interception on a try is "
     "blown dead immediately, so there is no risk of a return. The chart is on the special "
     "teams page and this is where intramural games get won."),
    ("Running clock, twenty five second play clock",
     "Two twenty minute halves. The clock only stops in the final two minutes of each half. "
     "Two thirty second timeouts per half and they do not carry over. If we are ahead, taking "
     "all twenty five seconds every snap is a weapon."),
    ("Punts have to be declared, and fakes are illegal",
     "On fourth down the referee asks whether we are punting. No fake or quick kicks at any "
     "time. Four of us have to be on the line, nobody crosses until the ball is kicked, and we "
     "have to give the returner a chance at the catch."),
    ("Everyone stays within fifteen yards of the ball",
     "Five yard penalty otherwise. No sleeper plays, no hiding a receiver by the bench."),
    ("Only the captain talks to the referee",
     "Anyone else disputing a call gets a warning and then an ejection. Judgment calls cannot "
     "be protested at all, only eligibility and rule interpretations, and only at the moment "
     "they happen."),
    ("Mercy rule at twenty five points",
     "Up or down twenty five with five minutes left and the game is over."),
]

PREGAME = [
    "All jewelry off, rings, watches, earrings, studs, necklaces, rubber bands. Tape does not "
    "make it legal.",
    "Shirts and hoods tucked in, and staying tucked in.",
    "No pockets, belt loops or exposed drawstrings on shorts.",
    "No hats with bills, no hard headgear, no exposed knots.",
    "No metal, ceramic or detachable cleats. Screw in is fine if the screw is part of the cleat.",
    "No pads or braces above the waist, and hard leg braces have to be covered.",
    "Flag belt at the waistline, one flag on each hip, one centre back, none covered by clothing.",
    "Matching shirt colours, or we are wearing intramural pinnies.",
    "Two practice balls in the bag, they are our responsibility and not the referee's.",
    "Ask the referee before kickoff where the ball is spotted after a score. The rules sheet "
    "says the 10 in one place and the 20 in another.",
]

ROUTE_ROWS = [
    ("Arrow / flat", "2 to 3 yds", "Immediately, flat to the sideline while gaining depth",
     "Head around by the time you cross the numbers, this ball is already gone"),
    ("Bubble", "1 yd behind the line", "Belly back one step, then run flat",
     "Catch it moving forward. Never stop your feet"),
    ("Slant", "3 yds", "Three hard steps, then a flat 45&deg; cut inside",
     "Eyes up on step three. Widen your split first so you have room to run to"),
    ("Hitch / curl", "5 to 6 yds", "Sink your hips, stop, step back toward the QB",
     "Do not drift. The QB throws to a spot, not to you"),
    ("Snag", "5 to 6 yds", "Settle in the first open window, face the QB",
     "Against zone, freeze. Against man, keep drifting away from your defender"),
    ("Quick out", "5 to 6 yds", "Flat 90&deg; break to the sideline",
     "On double moves break at 5, not 8, so the defender has to commit"),
    ("Drag / shallow", "4 to 5 yds", "Break flat across immediately, climbing a yard",
     "Never slow down. Speed is what makes crossers work"),
    ("Seam", "vertical", "No break, bend based on coverage",
     "Two safeties, bend to the middle between them. One safety, stay in the seam away "
     "from him"),
    ("Dig", "11 to 13 yds", "Flat 90&deg; break inside",
     "Run through the catch, this is a run after catch route"),
    ("Deep out", "12 to 14 yds", "Flat 90&deg; break to the sideline",
     "The ball is thrown before you break. Snap your head around at the plant"),
    ("Comeback", "13 to 14, back to 10", "Plant and come downhill toward the sideline",
     "Best route in football against a corner in a full sprint"),
    ("Corner", "10 to 12 yds", "45&deg; out and still climbing",
     "Stem at his inside shoulder first. Look over your outside shoulder"),
    ("Post", "10 to 12 yds", "45&deg; in and still climbing",
     "Never flatten a post, flat posts get intercepted"),
    ("Wheel", "flat to 5, then turn up", "Turn upfield around the numbers",
     "Stay a yard inside the sideline so the QB has room to throw outside you"),
    ("Go / fade", "no break", "Straight up",
     "Outside release, get on top of him, look at 15 to 18 over your outside shoulder"),
]

ROUTE_RULES = [
    ("Break on depth, not on the defender",
     "Unless one of the conversions below applies, the depth is the promise."),
    ("Sell the break with your stem",
     "Three hard steps at his inside or outside shoulder before you cut. If you drift "
     "straight to where you are going, he never has to turn."),
    ("Decelerate one step, maximum",
     "Separation is bought at the break, not with top speed."),
    ("Ninety degrees means ninety degrees",
     "A rounded break gives him time to recover and it kills the timing."),
    ("Head around at the plant",
     "Not two steps later."),
    ("Cheat your split",
     "Line up two or three yards tighter when you are breaking outside, and wider when you "
     "are breaking inside. Give yourself room to run to."),
]

CONVERT_ROWS = [
    ("Defender is pressed within 3 yards", "Hitch becomes a fade. Out becomes a slant.",
     "He has no cushion to protect, so run past him instead of stopping in front of him."),
    ("Defender is 8 or more yards off", "Fade becomes a hitch. Corner becomes an out.",
     "He is giving us the short throw. Take it, five free yards on first down is a good play."),
    ("Two deep safeties", "Seam bends toward the middle of the field.",
     "The hole in a two deep shell is between the safeties at 12 to 18 yards."),
    ("One deep safety in the middle", "Seam stays in the seam, away from him.",
     "Make him choose between you and the receiver on the other side."),
    ("Two or more rushers", "Anything past 6 yards converts to the nearest short route.",
     "Get your head around immediately. The QB is throwing hot, ready or not."),
    ("QB leaves the pocket", "Scramble rules for everyone.",
     "Deep stays deep and works across. Intermediate breaks to the sideline he is running "
     "toward. Shallow mirrors back toward him. Everybody makes eye contact."),
]

QB_LADDER = [
    ("Count the deep defenders",
     "Anyone standing more than eight yards off the ball. Zero, one, two or four. That single "
     "number eliminates most of the possibilities before you do anything else."),
    ("Check both corners",
     "How much cushion, and which shoulder are they shading. Tight and inside means there is "
     "man help over the top. Deep and outside means they are bailing to a zone."),
    ("Send H in motion and watch",
     "Somebody travels across with him and it is man. The whole coverage slides over one and "
     "it is zone. Nobody moves at all and it is zone, probably a soft one."),
    ("Count the rushers",
     "How many are within two yards of the line. Two or more means the ball has to come out "
     "on time and somebody is uncovered underneath."),
    ("Pick your side before the snap",
     "Decide which half of the field you are throwing into. Reading the whole field after the "
     "snap is how you end up holding it for four seconds."),
]

QB_READ_ROWS = [
    ("Nobody deep, everyone tight, a defender travels with motion", "Cover 0",
     "Mesh, Bunch Sting, Split Draw. Ball out fast."),
    ("One safety in the middle, corners tight", "Cover 1 man free",
     "Mesh, Bunch Post-Wheel, Deuce Scissors."),
    ("Two safeties, corners squatting at 5 to 7", "Cover 2",
     "Deuce Smash for the corner route, Empty Verts for the seams, Trey Dagger."),
    ("Two safeties, corners deep at 9 to 11, linebackers widened", "Cover 4, quarters",
     "Trey Drive, Trey Snag, and the run game. Take the underneath yards."),
    ("One safety in the middle, corners opening and bailing", "Cover 3",
     "Trey Flood, Trey Snag, Trey Dagger."),
    ("Nobody deeper than 6 and two men on the line", "Zero Dog pressure",
     "Sting hot, the center's outlet, or Split Draw right at the vacated middle."),
]

QB_POST_SNAP = [
    "The first defender to move tells the truth. Disguise dies at the snap, so watch the "
    "safety. If he rotates to the middle it is single high, if he stays wide it is two deep.",
    "Work one side, high to low. Never read the same defender twice, and never come back to a "
    "receiver you have already passed on.",
    "Three reads in three seconds, then run. Nobody is allowed to touch you, so a scramble is "
    "a free play, but throw before you cross the line of scrimmage.",
    "Never throw back across your body to the middle when you are scrambling. That is the "
    "interception that gets returned for six.",
    "The center is the pressure release. Against two rushers he is your hot throw at four or "
    "five yards, and defenses forget about him constantly.",
]

DEF_DEPTH_ROWS = [
    ("E, rusher", "One yard off the ball, outside shoulder of the widest lineman",
     "Same on every call. Arc three yards wide."),
    ("CL and CR, corners",
     "Two and Trap, 5 to 7 yards, Trap shows 8. Three, 7 to 9 with outside leverage. Four, "
     "10 to 11. Man, 5 to 7, and 4 to 5 in the red zone.",
     "Leverage rule, if you have help inside then play outside, and if you have help over the "
     "top then play inside."),
    ("N and M, hook players", "4 to 5 yards pre-snap, drop to 8 to 10",
     "Never end a play standing at 5 yards unless you made the pull."),
    ("FS and SS, safeties",
     "Two, 12 to 14 on the hash. Three, FS at 10 to 12 in the middle. Four, 11 to 12. One, FS "
     "at 12 to 14 in the middle.",
     "One rule beats all the others, nobody gets behind you."),
]

MAN_TECH = [
    ("Cushion is five to seven yards",
     "Four to five inside the red zone where there is nowhere deep to go. Cushion is the space "
     "between you and him, and managing it is your entire job."),
    ("Leverage tells you which half you own",
     "If you have a safety over the top, play inside leverage and force him outside toward the "
     "sideline. If you have inside help, play outside and force him in."),
    ("Three speeds of backpedal",
     "Control pedal at about 75 percent while your cushion is healthy. Speed pedal once he is "
     "inside three yards. Flip your hips and run when the cushion is gone."),
    ("If he is close enough to touch, he is close enough to run past you",
     "Turn and run. Getting beat deep is the only unrecoverable mistake out here."),
    ("Eyes on his hips, never on the quarterback",
     "A receiver physically cannot break a route without opening his hips. Head fakes, "
     "shoulder fakes and ball fakes all lie, hips do not."),
    ("Break when he breaks",
     "Plant off your outside foot and drive through his upfield shoulder, aiming at the catch "
     "point rather than at the man."),
]

READ_LADDER = [
    ("Three steps and no break",
     "It is not quick game. Stop reading the backfield and get depth."),
    ("Five or six yards and his hips sink",
     "Hitch, curl or snag. Drive on it now, this is where interceptions come from."),
    ("He fakes inside and his hips go outside",
     "Out or corner. Stay on top and squeeze him toward the sideline."),
    ("Twelve yards and still no break",
     "Go, post or corner. Turn, run, and find the ball late over your shoulder."),
    ("He accelerates through twelve",
     "He is going deep. If he decelerates he is breaking. Speed change is the earliest tell "
     "you get."),
    ("Split tells",
     "A receiver squeezed near the middle usually needs room to break outside, and a receiver "
     "split wide usually needs room to break inside. Not a law, but it is right more often "
     "than it is wrong."),
]

ZONE_TECH = [
    ("Cover grass, then cover a man",
     "Get to your landmark depth first. Do not chase a receiver out of your zone, pass him off "
     "and pick up the next one."),
    ("Eyes on the quarterback's shoulders and hips",
     "Feet always moving. His shoulders point at the throw before the ball does."),
    ("Settle at depth when he sets his feet, then break on the throw",
     "Break on the ball, not on the receiver."),
    ("Wall off crossers with your body",
     "Position, not hands. Grabbing is a ten yard penalty."),
    ("Talk constantly",
     "Vertical. Cross. In. Out. Ball. A quiet zone defense is a broken zone defense."),
]

RUSH_TECH = [
    ("Line up one yard off the ball",
     "On the outside shoulder of the widest lineman. The defensive line of scrimmage sits a "
     "yard behind theirs."),
    ("Arc, do not charge",
     "Take a path three yards wide of the blocker and get depth behind the quarterback before "
     "you turn in. Running at his chest gets us a roughing penalty and an automatic first down."),
    ("Contain means he never gets outside you",
     "If he escapes the pocket, every zone behind you breaks down."),
    ("Aim at the flag, not the body",
     "Reach for the hip. If you get anything else, let go instantly."),
    ("Two rushers squeeze, they do not race",
     "One contains outside, one takes the inside lane, and you never cross each other's face."),
    ("Vary the timing",
     "Show rush and drop. Show drop and rush. A quarterback who knows exactly when you are "
     "coming is a quarterback with all day."),
]

FLAG_TECH = [
    ("Watch the hips",
     "The ball, the head and the shoulders all lie. The hips go where he goes."),
    ("Break down two yards away",
     "Short choppy steps, weight forward, hands low and ready. Lunging from four yards out is "
     "how we give up long runs."),
    ("Take an inside out angle and use the sideline",
     "Never let a ball carrier cross your face back into the middle of the field."),
    ("Grab the flag, not the shirt",
     "You may contact his body and shoulder with your hands, but never the head or neck, and "
     "you may not hold, push or knock him down. If you grab anything but the flag, let go "
     "immediately."),
    ("Never swipe at the ball",
     "Attempting to strip it is ten yards from the end of the run. Everything we do goes "
     "toward the belt."),
    ("Hold the flag up",
     "The rules ask for it and it helps the official spot the ball where the ball actually was."),
    ("Second and third man rally",
     "The pull is not the end of the play until the whistle."),
]

PUNT_RULES = [
    "On fourth down the referee asks the captain whether we are punting or going for it. Once "
    "we answer, the defense is told, and we can only change our minds with a charged timeout "
    "or an accepted penalty that replays the down. So decide before he gets to us.",
    "Fake and quick kicks are illegal at any time, ten yards from the previous spot. There is "
    "no fake punt in this playbook because there cannot be one.",
    "The punter takes the snap like any other snap, at least two yards back. Four of us have "
    "to be on the line. Neither team crosses the line until the ball is kicked.",
    "We have to give the returner a real chance at the catch even if he does not signal for a "
    "fair catch. Running through him is ten yards and a replay, or an awarded fair catch.",
    "A punt that has not touched anybody is not dead. Once it touches a player from either "
    "team and then hits the ground, it is dead there and it belongs to the receiving team.",
    "If the receiving team muffs it and we catch it in the air, we keep it with a fresh set of "
    "downs. If it touches the ground first, it is dead. In the end zone that is a touchback.",
    "A punt through the back of the end zone comes out to the 14. Punts caught in the end zone "
    "can be returned, and the momentum rule protects a returner whose momentum carries him in.",
]

PUNT_POLICY = [
    ("Inside our own 25", "Punt.",
     "A safety is two points and hands them the ball back. Not worth it."),
    ("Our 25 to the midline", "Go for it with seven or fewer to gain, otherwise punt.",
     "Four downs to gain twenty means fourth down is worth more here than it is in real "
     "football."),
    ("Past the midline", "Always go for it.",
     "A punt from there nets us almost nothing and gives away a down we could have used."),
]

PAT_ROWS = [
    ("Down 6 before the score", "1 point, 3 yards", "We lead by one. Take the sure thing."),
    ("Down 7", "1 point, 3 yards", "Ties the game."),
    ("Down 8", "2 points, 10 yards", "Ties the game."),
    ("Down 9", "3 points, 20 yards", "Ties the game. This is the one people forget exists."),
    ("Down 10", "3 points, 20 yards", "Turns a two score game into a one point game."),
    ("Down 15", "3 points, 20 yards", "Makes it a six point game, so one touchdown wins it."),
    ("Ahead by any amount", "1 point, 3 yards",
     "Never risk a three point try when we are ahead unless it moves us past 3, 6 or 9."),
]

PAT_NOTES = [
    "Three yards is 1 point, ten yards is 2 points, twenty yards is 3 points.",
    "An interception or a fumble recovery on a try is blown dead immediately. There is no "
    "return and no defensive score, so a failed attempt costs us nothing but the points.",
    "A defensive penalty on a failed try means we replay it with the yardage. A defensive "
    "penalty on a successful try means the play just stands.",
    "After the try the ball goes to the other team. There are no kickoffs in this league at all.",
]

CLOCK_NOTES = [
    "The clock runs the whole game except the last two minutes of each half, when it stops for "
    "incompletions, out of bounds, first downs, scores, penalties and change of possession, "
    "and restarts on the snap.",
    "Protecting a lead means using all twenty five seconds, staying inbounds and running the "
    "ball. Four slow plays can burn three minutes.",
    "Chasing means Empty, sideline routes and no huddle. The quarterback may take the snap and "
    "immediately spike it at his own feet to stop the clock. It costs a down and he cannot "
    "hesitate doing it.",
    "Two timeouts per half at thirty seconds each, and unused ones disappear at halftime. Do "
    "not finish the first half with two in your pocket.",
    "Overtime is first and goal from the 10, four downs, and first downs cannot be earned. In "
    "the regular season it ends in a tie after two rounds. One timeout for the whole overtime.",
]

SITU_ROWS = [
    ("Own goal line to our 20", "Bubble, Sting, Jet",
     "Nothing across the middle and nothing behind the line. A safety is two points and gives "
     "them the ball back."),
    ("Our 20 to the midline", "Full menu, this is where we take our shots",
     "Scissors, Boomerang and Omaha live here. Worst case is an incompletion at midfield."),
    ("Midline to their 20", "Flood, Dagger, Snag",
     "Fourth down is aggressive from here. We are past the point where punting helps."),
    ("Their 20 to the goal line", "Bunch Sting, Empty Corner, Bunch Wheel",
     "The field is short so the deep routes die. Win with traffic and back pylon throws."),
    ("1st and 20", "Sting, Jet, Bubble", "Take six and stay ahead of the sticks."),
    ("2nd and 12 or less", "Mesh, Smash, Naked", "One good chunk puts us in 3rd and short."),
    ("2nd and 15 or more", "Dagger, Flood", "We need the whole thing on one snap."),
    ("3rd and 5 or less", "Snag, Bunch Sting, Draw", "High percentage. Take the sure yards."),
    ("3rd and 10 or more", "Flood, Dagger, Verts", "High to low, and no forcing it."),
    ("4th and 5 or less", "Bandit, Draw, Snag", "From our own 25 onward we go for it."),
    ("4th and 12 or more", "Rodeo, or punt if we are inside our own 25", ""),
]

INSTALL = [
    ("Session 1",
     "<p><strong>Rules block, 15 minutes.</strong> The one second freeze, hands behind the "
     "back, flag guarding, and the jewelry and pockets check. These are the penalties that "
     "will cost us games.</p>"
     "<p><strong>Install.</strong> Deuce and Trey alignment. Sting, Bubble, Snag, Smash.</p>"
     "<p><strong>Defense.</strong> Cover Two only. Everyone learns their drop and their "
     "depth.</p>"
     "<p><strong>Finish.</strong> Ten minutes of flag pulling.</p>"),
    ("Session 2",
     "<p><strong>Install.</strong> Mesh, Flood, Dagger, Jet, Naked, plus motion and the man "
     "versus zone read off it.</p>"
     "<p><strong>Defense.</strong> Cover Three and Cover One. Adjustments to trips and "
     "bunch.</p>"
     "<p><strong>Finish.</strong> Two minute drill, live.</p>"),
    ("Session 3",
     "<p><strong>Install.</strong> The red zone package, Bunch Sting, Empty Corner and Bunch "
     "Wheel, plus Verts and Scissors.</p>"
     "<p><strong>Defense.</strong> Zero, Zero Dog and Two Trap.</p>"
     "<p><strong>Finish.</strong> Two trick plays, ten reps each. If the pitch is not clean "
     "ten times in a row, it does not go in the game plan.</p>"),
    ("Every warm up, every week",
     "<p>Five minutes of snap and freeze from the center, five minutes of flag pulling, and "
     "five minutes of routes on air at real depths with the real quarterback.</p>"
     "<p>Those three things fix more of our problems than any new play will.</p>"),
]

CORE_EIGHT_OFF = ("Deuce Sting, Deuce Bubble, Trey Snag, Deuce Smash, Deuce Mesh, Trey Flood, "
                  "Split Jet, Bunch Sting.")
CORE_EIGHT_DEF = ("Cover Two, Cover Three, Cover One. If you know nothing else, know your job "
                  "in Two.")

# Table headers, kept here so the templates stay free of layout data.
H_OFF_POS = ("", "offense", "what the job needs")
H_DEF_POS = ("", "defense", "what the job needs")
H_ROUTES = ("route", "depth", "the break", "coaching cue")
H_CONVERT = ("what you see", "what the route becomes", "why")
H_QB_READ = ("what you see pre-snap", "what it probably is", "what we want on")
H_DEF_DEPTH = ("position", "where you line up", "the rule behind it")
H_PUNT = ("where we are", "what we do", "why")
H_PAT = ("score situation", "take", "result")
H_SITU = ("where we are, down and distance", "what we call", "why")

H_PENALTY = ("penalty", "what it looks like")
