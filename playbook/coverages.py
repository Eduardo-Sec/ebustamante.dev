"""Defensive content: coverages, assignments, technique."""

from .diagrams import diagram

# offense shown faintly on defensive diagrams (2x2 look)
OFF_GHOST = [("gh", -16, 0, "", "off"), ("gh", -9, 0, "", "off"), ("gh", 0, 0, "", "off"),
             ("gh", 9, 0, "", "off"), ("gh", 16, 0, "", "off"), ("gh", 0, -5, "", "off")]

D = []


def cov(**kw):
    D.append(kw)


cov(
    id="two", name="Two", sub="Cover 2, our base", group="Zone",
    tags=["Base call", "Stops the deep ball", "Safe"],
    svg=diagram(OFF_GHOST + [("E", 3, 1.5), ("N", -5, 5), ("M", 5, 5),
                             ("CL", -15, 5), ("CR", 15, 5), ("FS", -9, 13), ("SS", 9, 13)],
    [('CL', [(-15, 5), (-15.5, 10.5)], 'arrow', 'dash'),
     ('CR', [(15, 5), (15.5, 10.5)], 'arrow', 'dash'),
     ('N', [(-5, 5), (-7.5, 9.5)], 'arrow', 'dash'),
     ('M', [(5, 5), (7.5, 9.5)], 'arrow', 'dash'),
     ('FS', [(-9, 13), (-11.5, 17.5)], 'arrow', 'dash'),
     ('SS', [(9, 13), (11.5, 17.5)], 'arrow', 'dash'),
     ("E", [(3, 1.5), (7, 0.5), (8.5, -3.5), (4, -6)], "arrow", "dash")],
                zones=[("z1", -11, 14, 62, 34, ""), ("z2", 11, 14, 62, 34, "")],
                side="def", title="Cover 2"),
    idea="Two safeties split the deep half of the field between them. Four defenders play "
         "underneath zones. One rusher. Nothing gets behind us, and everything short gets "
         "tackled immediately.",
    weak="The deep middle at 12 to 18 yards, and the corner route that lands between the squat "
         "corner and the half safety. If a team keeps hitting those, check to Two Pipe or Three.",
    assign=[
        ("E", "Rush, contain", "Align on the outside shoulder of the widest lineman, one yard off. "
                               "Take an arc three yards wide, you must go AROUND, never through. "
                               "Never let the QB outside you. <strong>Any contact with the QB is "
                               "an automatic first down</strong>, so run to his flags, not his body."),
        ("CL", "Flat, left", "Align 5 to 7 yards deep, inside eye of the widest receiver. Read the QB, "
                             "not the receiver. If a receiver comes to the flat, you own him. If "
                             "nobody comes to the flat, sink to 10 to 12 and get under the out route."),
        ("CR", "Flat, right", "Mirror CL."),
        ("N", "Hook / curl, left", "Align 4 to 5 yards deep over the inside receiver. Drop to 8 to 10 "
                                   "yards, staying between the hash and the numbers. Wall off any "
                                   "crosser coming your way and re-route him."),
        ("M", "Hook / curl, right", "Mirror N. You two are responsible for anything sitting down "
                                    "at 8 to 12 yards in the middle."),
        ("FS", "Deep half, left", "Align 12 to 14 yards deep, about eight yards outside the ball. "
                                  "Backpedal at the snap. Your rule is simple, <strong>nobody gets behind "
                                  "you</strong>. You would rather give up 12 yards than 40."),
        ("SS", "Deep half, right", "Mirror FS. Talk to each other, call out crossers and verticals."),
    ],
    call="Base call. If we say nothing, we are in Two.",
)

cov(
    id="pipe", name="Two Pipe", sub="Tampa 2", group="Zone",
    tags=["Kills the seam", "Kills 4 verts"],
    svg=diagram(OFF_GHOST + [("E", 3, 1.5), ("N", -5, 5), ("M", 0, 5),
                             ("CL", -15, 5), ("CR", 15, 5), ("FS", -10, 13), ("SS", 10, 13)],
    [('CL', [(-15, 5), (-15.5, 10.5)], 'arrow', 'dash'),
     ('CR', [(15, 5), (15.5, 10.5)], 'arrow', 'dash'),
     ('N', [(-5, 5), (-6.5, 9.5)], 'arrow', 'dash'),
     ('M', [(0, 5), (0, 16.5)], 'arrow', 'dash'),
     ('FS', [(-10, 13), (-12.5, 17.5)], 'arrow', 'dash'),
     ('SS', [(10, 13), (12.5, 17.5)], 'arrow', 'dash'),
     ("E", [(3, 1.5), (7, 0.5), (8.5, -3.5), (4, -6)], "arrow", "dash")],
                zones=[("z1", -12, 14, 58, 32, ""), ("z2", 12, 14, 58, 32, ""),
                       ("z3", 0, 13, 34, 40, "")],
                side="def", title="Tampa 2"),
    idea="Cover 2 with one change, M sprints straight down the middle of the field to 15 yards "
         "and covers the pipe. That closes the one hole in Cover 2 and turns four verticals "
         "into a bad play for them.",
    weak="The two hook zones at 8 to 10 yards are now emptier. Teams that run drags and digs will "
         "get 8 yards at a time. That is a trade we are happy to make.",
    assign=[
        ("M", "Run the pipe", "At the snap, turn and sprint up the middle of the field to 15+ "
                              "yards, staying between the two safeties. Eyes on the QB. This is "
                              "a conditioning assignment, you have to actually get there."),
        ("E", "Rush, contain", "Same as Two."),
        ("CL", "Flat, left", "Same as Two, 5 to 7 yards, sink if nobody threatens the flat."),
        ("CR", "Flat, right", "Same as Two."),
        ("N", "Hook, middle-left", "You are now alone underneath the middle. Drop to 8 to 10 and "
                                   "wall crossers."),
        ("FS", "Deep half, left", "Same as Two, but you can squeeze a yard wider knowing M has "
                                  "the middle."),
        ("SS", "Deep half, right", "Same as FS."),
    ],
    call="Call it when they line up in Empty or when they have hit us on a seam.",
)

cov(
    id="three", name="Three", sub="Cover 3", group="Zone",
    tags=["Vs shot teams", "Vs Empty", "Nothing over the top"],
    svg=diagram(OFF_GHOST + [("E", 3, 1.5), ("N", -8, 5), ("M", 0, 5), ("SS", 8, 5),
                             ("CL", -15, 9), ("CR", 15, 9), ("FS", 0, 13)],
    [('CL', [(-15, 9), (-16, 16)], 'arrow', 'dash'),
     ('CR', [(15, 9), (16, 16)], 'arrow', 'dash'),
     ('FS', [(0, 13), (0, 17.5)], 'arrow', 'dash'),
     ('N', [(-8, 5), (-11, 9.5)], 'arrow', 'dash'),
     ('SS', [(8, 5), (11, 9.5)], 'arrow', 'dash'),
     ('M', [(0, 5), (0, 9.5)], 'arrow', 'dash'),
     ("E", [(3, 1.5), (7, 0.5), (8.5, -3.5), (4, -6)], "arrow", "dash")],
                zones=[("z1", -13, 15, 52, 30, ""), ("z2", 0, 15, 52, 30, ""),
                       ("z3", 13, 15, 52, 30, "")],
                side="def", title="Cover 3"),
    idea="Three defenders split the deep field into thirds, three defenders play underneath, "
         "one rushes. Every deep window has a body in it. This is the call when a team wants "
         "to throw it over our heads.",
    weak="The flat and the 10 to 14 yard out route. A good flood concept, three routes at three "
         "depths to one side, is the exact play that beats this. If they run it twice, check "
         "to Two.",
    assign=[
        ("CL", "Deep third, left", "Align 7 to 9 yards deep with OUTSIDE leverage on the widest "
                                   "receiver. At the snap, open and bail, get depth first, "
                                   "questions later. Stay on top of the deepest receiver in your "
                                   "third by three yards."),
        ("CR", "Deep third, right", "Mirror CL."),
        ("FS", "Deep middle", "Align 10 to 12 yards deep in the middle of the field. Backpedal and "
                              "read the QB's shoulders. You are the last line, never let a post "
                              "or a seam get behind you."),
        ("N", "Curl / flat, left", "Align 4 to 5 yards over the inside receiver. Drop toward the curl "
                                   "at 10 yards, then break out to the flat when the QB's shoulders "
                                   "turn that way. Curl first, flat second, not the other way around."),
        ("SS", "Curl / flat, right", "Mirror N."),
        ("M", "Hook, middle", "Drop to 8 to 10 in the middle. Wall off crossers, take away the dig."),
        ("E", "Rush, contain", "Same arc rush. Keep the QB in the pocket, if he escapes, "
                               "everyone's zone breaks down."),
    ],
    call="Call it on 2nd &amp; long, against Empty, and against any team with one receiver "
         "clearly faster than our corners.",
)

cov(
    id="four", name="Four", sub="Quarters / prevent", group="Zone",
    tags=["4th &amp; long", "End of half", "No big plays"],
    svg=diagram(OFF_GHOST + [("E", 3, 1.5), ("N", -5, 5), ("M", 5, 5),
                             ("CL", -15, 11), ("CR", 15, 11), ("FS", -6, 12), ("SS", 6, 12)],
    [('CL', [(-15, 11), (-16, 16.5)], 'arrow', 'dash'),
     ('CR', [(15, 11), (16, 16.5)], 'arrow', 'dash'),
     ('FS', [(-6, 12), (-6, 17)], 'arrow', 'dash'),
     ('SS', [(6, 12), (6, 17)], 'arrow', 'dash'),
     ('N', [(-5, 5), (-10, 9)], 'arrow', 'dash'),
     ('M', [(5, 5), (10, 9)], 'arrow', 'dash'),
     ("E", [(3, 1.5), (7, 0.5), (8.5, -3.5), (4, -6)], "arrow", "dash")],
                zones=[("z1", -15, 16, 44, 26, ""), ("z2", -5, 16, 44, 26, ""),
                       ("z3", 5, 16, 44, 26, ""), ("z4", 15, 16, 44, 26, "")],
                side="def", title="Cover 4"),
    idea="Four defenders deep, two underneath, one rushing. We concede everything under 10 yards "
         "and take away every deep throw. Remember, they need 20 yards for a first down. Making "
         "them complete four 6-yard passes in a row is a win for us.",
    weak="Everything short. The shallow cross and the dig at 11 yards will be open. Do not call "
         "this on 3rd &amp; 5.",
    assign=[
        ("CL", "Deep quarter, outside left", "Align 10 to 11 yards deep. Backpedal. You have "
                                             "everything deep and outside on your side. Do not "
                                             "come up on a short throw until the ball is in "
                                             "the air."),
        ("CR", "Deep quarter, outside right", "Mirror CL."),
        ("FS", "Deep quarter, inside left", "Align 12 yards deep, inside the hash. Take the "
                                            "second receiver if he goes vertical."),
        ("SS", "Deep quarter, inside right", "Mirror FS."),
        ("N", "Underneath, left half", "You are covering half the field underneath by yourself. "
                                       "Stay at 8 to 10 yards, keep everything in front, and rally "
                                       "to the catch."),
        ("M", "Underneath, right half", "Mirror N. Communicate on crossers, hand them off."),
        ("E", "Rush, contain", "Slow, controlled rush. Keep the QB in front of you and make him "
                               "hold the ball."),
    ],
    call="4th &amp; 12+, last play of a half, or when we are up two scores inside two minutes.",
)

cov(
    id="one", name="One", sub="Man free", group="Man",
    tags=["3rd down", "Tight coverage", "Needs a rush"],
    svg=diagram(OFF_GHOST + [("E", 3, 1.5), ("CL", -15, 6), ("N", -9, 5), ("M", 9, 5),
                             ("CR", 15, 6), ("SS", 0, 7), ("FS", 0, 14)],
    [('CL', [(-15, 6), (-16, 1.2)], 'arrow', 'dash'),
     ('CR', [(15, 6), (16, 1.2)], 'arrow', 'dash'),
     ('N', [(-9, 5), (-9, 1.2)], 'arrow', 'dash'),
     ('M', [(9, 5), (9, 1.2)], 'arrow', 'dash'),
     ('SS', [(0, 7), (0, 2)], 'arrow', 'dash'),
     ('FS', [(0, 14), (0, 18)], 'arrow', 'dash'),
     ("E", [(3, 1.5), (7, 0.5), (8.5, -3.5), (4, -6)], "arrow", "dash")],
                side="def", title="Cover 1 man free"),
    idea="Everyone covers a man, FS plays centre field over the top, SS floats underneath as a "
         "robber and takes the center's free release. Tight coverage that forces the QB to hold "
         "the ball.",
    weak="Mesh and any crossing concept. Bunch formations. If they cross two receivers, "
         "communicate and switch rather than chasing through traffic.",
    assign=[
        ("CL", "Man on the widest receiver, left", "Align 5 to 7 yards off with INSIDE leverage, "
                                                   "FS has the deep middle, so you take away the "
                                                   "outside. Eyes on his hips, never on the QB."),
        ("CR", "Man on the widest receiver, right", "Mirror CL."),
        ("N", "Man on the inside receiver, left", "Align 4 to 5 yards off, inside leverage. If he "
                                                  "crosses the formation, call \"cross\" and pass "
                                                  "him to M."),
        ("M", "Man on the inside receiver, right", "Mirror N."),
        ("SS", "Robber / center + QB spy", "Align 6 to 7 yards deep in the middle. Take the center "
                                           "when he releases. If the QB takes off running, you "
                                           "are the one who pulls his flag."),
        ("FS", "Deep middle, help over the top", "12 to 14 yards, middle of the field. Read the QB's "
                                                 "eyes and go help whichever corner is losing. "
                                                 "You are the free player, be greedy about the ball."),
        ("E", "Rush, contain", "In man coverage the rush matters more than anywhere else. Get "
                               "there, but around, never through."),
    ],
    call="3rd &amp; 6 or less, and any time we clearly have better athletes than they do.",
)

cov(
    id="zero", name="Zero", sub="Everybody covered", group="Man",
    tags=["Goal line", "Match all six", "No help"],
    svg=diagram(OFF_GHOST + [("E", 3, 1.5), ("CL", -15, 5), ("N", -9, 4), ("M", 9, 4),
                             ("CR", 15, 5), ("SS", 0, 5), ("FS", 0, 9)],
    [('CL', [(-15, 5), (-16, 1.2)], 'arrow', 'dash'),
     ('CR', [(15, 5), (16, 1.2)], 'arrow', 'dash'),
     ('N', [(-9, 4), (-9, 1.2)], 'arrow', 'dash'),
     ('M', [(9, 4), (9, 1.2)], 'arrow', 'dash'),
     ('SS', [(0, 5), (-2, 1.5)], 'arrow', 'dash'),
     ('FS', [(0, 9), (0, 1.5)], 'arrow', 'dash'),
     ("E", [(3, 1.5), (7, 0.5), (8.5, -3.5), (4, -6)], "arrow", "dash")],
                side="def", title="Cover 0"),
    idea="One rusher, six defenders on six eligible receivers, including the center. Nobody is "
         "free anywhere, which means the QB has to make a perfect throw against tight coverage. "
         "Best used in a short field where there is no room to run away from us.",
    weak="No help over the top at all. One missed step is a touchdown. Also vulnerable to picks "
         "out of a bunch, so we banjo it (see below).",
    assign=[
        ("CL", "Man, widest left", "Align 4 to 5 yards. In the red zone there is no deep threat, so "
                                   "get closer and take away the inside."),
        ("CR", "Man, widest right", "Mirror CL."),
        ("N", "Man, inside left", "Tight. If they bunch, call \"banjo\", you take the first "
                                  "receiver out, M takes the second."),
        ("M", "Man, inside right", "Mirror N."),
        ("SS", "Man on the back / third receiver", "Whoever is left in the backfield is yours. "
                                                   "If he stays in, become a QB spy."),
        ("FS", "Man on the center", "The center is eligible in this league and he releases free "
                                    "on almost every play. Take him and take away the easy outlet."),
        ("E", "Rush, contain", "Same arc rush."),
    ],
    call="Goal line, 4th &amp; 1, and PAT attempts.",
)

cov(
    id="dog", name="Zero Dog", sub="Two rushers", group="Pressure",
    tags=["3rd &amp; long", "Change-up", "Risky"],
    svg=diagram(OFF_GHOST + [("E", 4, 1.5), ("N", -4, 1.5), ("CL", -15, 5), ("M", 9, 4),
                             ("CR", 15, 5), ("SS", -9, 5), ("FS", 0, 10)],
    [('CL', [(-15, 5), (-16, 1.2)], 'arrow', 'dash'),
     ('CR', [(15, 5), (16, 1.2)], 'arrow', 'dash'),
     ('SS', [(-9, 5), (-9, 1.2)], 'arrow', 'dash'),
     ('M', [(9, 4), (9, 1.2)], 'arrow', 'dash'),
     ('FS', [(0, 10), (0, 1.5)], 'arrow', 'dash'),
     ("E", [(4, 1.5), (8, 0.5), (9.5, -3.5), (5, -6)], "arrow", "dash"), ("N", [(-4, 1.5), (-8, 0.5), (-9.5, -3.5), (-5, -6)], "arrow", "dash")],
                side="def", title="Zero Dog two-rusher pressure"),
    idea="Two rushers off both edges. The QB has half the time he expects. We accept that the "
         "center will be uncovered, a 5-yard completion to the center on 3rd &amp; 12 is a win.",
    weak="The center and any quick screen. Never call this twice in a row, and never call it "
         "when they only need a few yards.",
    assign=[
        ("E", "Rush, right edge", "Wide arc. You have contain, the QB does not get outside you."),
        ("N", "Rush, left edge", "Mirror E. You two are squeezing him from both sides toward the "
                                 "middle where the coverage is. Do not cross each other's faces."),
        ("CL", "Man, widest left", "You have no help. Play inside leverage and trust the rush."),
        ("CR", "Man, widest right", "Mirror CL."),
        ("SS", "Man, inside left", "Tight man. Ball comes out fast so jump the short route."),
        ("M", "Man, inside right", "Mirror SS."),
        ("FS", "Man on the back, then the center", "Take the back. If he stays in, get to the "
                                                   "center, he is the hot throw."),
    ],
    call="3rd &amp; 10+, or immediately after a defensive penalty when they expect us to be soft.",
)

cov(
    id="trap", name="Two Trap", sub="Corner bait", group="Zone",
    tags=["Turnover call", "Vs quick game", "Once a game"],
    svg=diagram(OFF_GHOST + [("E", 3, 1.5), ("N", -5, 5), ("M", 5, 5),
                             ("CL", -15, 8), ("CR", 15, 8), ("FS", -9, 13), ("SS", 9, 13)],
    [('CL', [(-15, 8), (-17.5, 2.5)], 'arrow', 'dash'),
     ('CR', [(15, 8), (17.5, 2.5)], 'arrow', 'dash'),
     ('N', [(-5, 5), (-7.5, 9.5)], 'arrow', 'dash'),
     ('M', [(5, 5), (7.5, 9.5)], 'arrow', 'dash'),
     ('FS', [(-9, 13), (-11.5, 17.5)], 'arrow', 'dash'),
     ('SS', [(9, 13), (11.5, 17.5)], 'arrow', 'dash'),
     ("E", [(3, 1.5), (7, 0.5), (8.5, -3.5), (4, -6)], "arrow", "dash")],
                zones=[("z1", -11, 14, 62, 34, ""), ("z2", 11, 14, 62, 34, "")],
                notes=[(0, -7.5, "Corners show deep, then jump the flat.")],
                side="def", title="Cover 2 trap"),
    idea="Looks exactly like Two, but the corners align deeper, 8 yards, showing a bail, and "
         "then drive hard on the flat or bubble the second the QB's shoulders turn. This is how "
         "we get an interception against a team that lives on quick throws.",
    weak="If we jump and they throw the go route behind us, it is a touchdown unless the safety "
         "is disciplined. Safeties, no peeking.",
    assign=[
        ("CL", "Show deep, trap the flat", "Align 8 yards with outside leverage and open your hips "
                                           "like you are bailing. Watch the QB. The instant he "
                                           "loads a quick throw outside, plant and drive downhill "
                                           "through the receiver's upfield shoulder, catch it, "
                                           "do not just knock it down."),
        ("CR", "Show deep, trap the flat", "Mirror CL."),
        ("FS", "Deep half, no peeking", "You have everything behind the trap. If your corner "
                                        "guesses wrong you are the only thing between them and "
                                        "six points. Stay at 13+."),
        ("SS", "Deep half, no peeking", "Mirror FS."),
        ("N", "Hook / curl, left", "Same as Two, wall the crossers."),
        ("M", "Hook / curl, right", "Same as Two."),
        ("E", "Rush, contain", "Rush hard. The whole play depends on the QB throwing quickly."),
    ],
    call="Once a game, after they have completed three or more quick outs or bubbles on us.",
)

# ------------------------------------------------------------------ adjustments
ADJUSTMENTS = [
    ("Trips (three receivers to one side)",
     "In zone, the corner away from the trips has nobody within fifteen yards, bring him toward "
     "the middle and play the deep third or half from there. In man, call \"solo\", CL locks on "
     "the isolated receiver with no help and everyone else slides to the trips."),
    ("Bunch (three receivers stacked)",
     "Never chase men through a bunch, you will collide and they will be open. Call \"banjo\": "
     "N takes the first receiver who releases outside, M takes the first inside, SS takes the "
     "leftover. Or just check to Two and play zone."),
    ("Empty (nobody in the backfield)",
     "No run threat and no play-action, so drop everybody. Check to Three or Two Pipe and rush "
     "one. Do not blitz Empty, they have six routes ready for it."),
    ("Two backs / heavy run look",
     "Check to Two. Corners squat at 5. Somebody must have eyes on the sweep, the edge defender "
     "away from the rush keeps outside contain and does not chase inside."),
    ("Motion across the formation",
     "The defender covering the motion man travels in man, and we bump one over in zone. Say it "
     "out loud, \"motion, travel\" or \"motion, bump\". Silence is how we get someone uncovered."),
    ("They are hunting the extra point",
     "Interceptions on a PAT are dead immediately, no return, no score. So on a PAT, play the "
     "ball aggressively, there is no downside to gambling on it."),
]


# Attach the beginner explainers.
from .tags import decorate_coverages  # noqa: E402

decorate_coverages(D)
