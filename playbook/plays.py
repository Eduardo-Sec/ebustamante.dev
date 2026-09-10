"""Offensive content: formations, plays, assignments."""

from .diagrams import (diagram, go, stemgo, hitch, slant, out, indig, corner,
                       post, flat, swing, drag, wheel, comeback, double)

# ---------------------------------------------------------------- alignments
# (tag, x, depth)
DEUCE = [("X", -16, 0), ("H", -9, -1.5), ("C", 0, 0), ("QB", 0, -5),
         ("R", 3.5, -5), ("Y", 9, 0), ("Z", 16, 0)]
TREY = [("X", -16, 0), ("C", 0, 0), ("QB", 0, -5), ("R", -3.5, -5),
        ("Y", 7, 0), ("H", 11.5, -1.5), ("Z", 16.5, 0)]
TREY_L = [("Z", 16, 0), ("C", 0, 0), ("QB", 0, -5), ("R", 3.5, -5),
          ("Y", -7, 0), ("H", -11.5, -1.5), ("X", -16.5, 0)]
BUNCH = [("X", -16, 0), ("C", 0, 0), ("QB", 0, -5), ("R", -3.5, -5),
         ("Y", 8, 0), ("H", 10.5, -2.5), ("Z", 13.5, 0)]
EMPTY = [("X", -17, 0), ("H", -10, -1.5), ("C", 0, 0), ("QB", 0, -5),
         ("Y", 8, 0), ("R", 12.5, -1.5), ("Z", 17, 0)]
SPLIT = [("X", -16, 0), ("C", 0, 0), ("QB", 0, -5), ("H", -3.5, -6),
         ("R", 3.5, -6), ("Y", 8, 0), ("Z", 16, 0)]

FORMATIONS = [
    {
        "name": "Deuce",
        "sub": "2x2, our base",
        "svg": diagram(DEUCE, [], title="Deuce formation"),
        "text": "Two receivers each side, R offset behind the QB. Balanced, the defense "
                "cannot cheat coverage to one side without opening the other. Everything "
                "in the quick game and the mirrored concepts comes out of this.",
        "who": "On the line, C, X, Y and Z. Off the line, QB, H and R.",
    },
    {
        "name": "Trey",
        "sub": "3x1, trips",
        "svg": diagram(TREY, [], title="Trey formation"),
        "text": "Three to one side, X isolated backside. Zone teams have to put three "
                "defenders on three receivers, which leaves X one-on-one with no help. "
                "Flip the call to \"Trey Left\" and everything mirrors.",
        "who": "On the line, C, X, Y and Z. Off the line, QB, H and R.",
    },
    {
        "name": "Bunch",
        "sub": "3x1 tight, pick package",
        "svg": diagram(BUNCH, [], title="Bunch formation"),
        "text": "Y, Z and H stacked within four yards of each other. Man coverage defenders "
                "run into each other trying to stay on their guy, and we never have to throw "
                "a block to make it happen. This is our red-zone formation.",
        "who": "On the line, C, X, Y and Z. Off the line, QB, H and R. H aligns two yards "
               "behind the gap between Y and Z.",
    },
    {
        "name": "Empty",
        "sub": "5 wide, nobody in the backfield",
        "svg": diagram(EMPTY, [], title="Empty formation"),
        "text": "Every skill player split out. The defense has to declare what it is before "
                "the snap, which makes this the easiest formation for the QB to read. "
                "Two-minute offense and long-yardage package.",
        "who": "On the line, C, X, Y and Z. Off the line, QB, H and R (both aligned as slots, "
               "one full step behind the ball).",
    },
    {
        "name": "Split",
        "sub": "2 backs, run and play-action",
        "svg": diagram(SPLIT, [], title="Split backs formation"),
        "text": "H and R side by side six yards deep. Two run threats in opposite "
                "directions freeze the linebackers, which is the whole point, every "
                "play-action shot we have comes off this look.",
        "who": "On the line, C, X, Y and Z. Off the line, QB, H and R.",
    },
]

# ---------------------------------------------------------------- plays
P = []


def play(**kw):
    P.append(kw)


# --- QUICK GAME -------------------------------------------------------------
play(
    id="sting", group="Quick game", name="Deuce Sting", call="&ldquo;Deuce Sting&rdquo;",
    tags=["Off man", "Cover 1", "Beats pressure", "1st &amp; 20"],
    time="Ball out in 1.5 seconds",
    svg=diagram(DEUCE, [
        ("X", slant(-16, 0, +1, depth=3, run=9)),
        ("H", flat(-9, -1.5, -1, run=7, rise=4)),
        ("Z", slant(16, 0, -1, depth=3, run=9)),
        ("Y", flat(9, 0, +1, run=8, rise=4)),
        ("R", swing(3.5, -5, +1)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], title="Deuce Sting"),
    why="Slant-and-arrow to both sides. The slant beats a corner who is backpedalling, "
        "the arrow beats a corner who jumps the slant. One defender, two routes, and "
        "the throw is out before any rush can matter.",
    when="First down, after a penalty, any time they are rushing two, and any time a "
         "corner is playing more than six yards off.",
    read="Pick a side pre-snap off the corner's leverage. Corner inside-shaded → throw the "
         "arrow. Corner outside-shaded or deep → throw the slant. Catch, hitch, throw, "
         "if you take a third step you are late.",
    assign=[
        ("X", "Slant", "Widen your split to the numbers. Three hard steps upfield, then break "
                       "flat inside at 3 yards. Do not round it. Catch it with your body between "
                       "the ball and the defender and turn upfield immediately."),
        ("Z", "Slant", "Mirror X on the other side. Same split, same three steps, same 3-yard break."),
        ("H", "Arrow", "Push flat toward the sideline, gaining depth to about 4 yards by the time "
                       "you are outside the numbers. Head around early, this ball comes out fast."),
        ("Y", "Arrow", "Mirror H. Cheat your alignment in a yard so you have room to run to."),
        ("R", "Swing", "Open to the right and run a flat arc to the sideline. You are the "
                       "outlet, square your shoulders to the QB once you are outside."),
        ("C", "Snap, sit at 5", "Snap it clean, then release straight up 5 yards and stop, facing "
                                "the QB. You are the last resort when everything else is covered."),
        ("QB", "Catch and throw", "Read one corner, one time. If the ball is not gone on your "
                                  "second step, you called this play wrong."),
    ],
    coach="This play exists so we never get stuck in a long down. Two of these in a row on "
          "first and second down puts us in 3rd &amp; short with the whole playbook open.",
)

play(
    id="bubble", group="Quick game", name="Deuce Bubble", call="&ldquo;Deuce Bubble Right&rdquo;",
    tags=["Zone", "Free yards", "Backed up"],
    time="Ball out in 1.2 seconds",
    svg=diagram(DEUCE, [
        ("Y", swing(9, 0, -1)),
        ("Z", stemgo(16, 0, 15)),
        ("H", stemgo(-9, -1.5, 15)),
        ("X", stemgo(-16, 0, 15)),
        ("R", flat(3.5, -5, +1, run=8, rise=2)),
        ("C", hitch(0, 0, depth=4), "bar"),
    ], notes=[(0, -7.5, "Z and X run their defenders off. Nobody blocks.")],
        title="Deuce Bubble"),
    why="We cannot block downfield with our hands, so the way we clear space is with routes. "
        "Z runs straight up the field and takes his corner with him. Y catches it in the "
        "vacated grass with a ten-yard head start on anyone who can catch him.",
    when="Any time the defense leaves the outside receiver's defender at 8+ yards, and every "
         "single time we are backed up inside our own 10.",
    read="Pre-snap only. Count defenders outside the hash to that side. Two defenders and "
         "two receivers, throw it. Three defenders, check to the other side or run Sting.",
    assign=[
        ("Y", "Bubble", "Open away from the line of scrimmage, belly back a yard, then run "
                        "flat to the sideline. Catch it on the move going forward, never stop "
                        "your feet to catch a bubble."),
        ("Z", "Clear vertical", "Sprint straight up the field at full speed for 15 yards. You "
                                "are not getting the ball. Your job is to make your corner turn "
                                "and run. If you jog, the play dies."),
        ("X", "Clear vertical", "Same as Z on the backside. Take your man deep."),
        ("H", "Clear vertical", "Straight up the seam. Occupy the safety."),
        ("R", "Flat, stay stationary at the numbers", "Release to the flat and get set. If you are "
                                                      "already stopped and Y runs past you, that is "
                                                      "legal screening. If you are moving into a "
                                                      "defender, that is a 10-yard penalty."),
        ("C", "Snap, sit at 4", "Snap and settle in the middle as the outlet."),
        ("QB", "Catch and fire", "Throw it slightly in front of Y, at his numbers. Lead him to "
                                 "the sideline, not to his back shoulder."),
    ],
    coach="Averages 6 to 8 yards for free against most zone looks. On a field where 20 yards is a "
          "first down, two bubbles is a first down.",
)

play(
    id="snag", group="Quick game", name="Trey Snag", call="&ldquo;Trey Snag&rdquo;",
    tags=["Any coverage", "3rd &amp; medium", "Triangle read"],
    time="Ball out in 2 seconds",
    svg=diagram(TREY, [
        ("Z", corner(16.5, 0, depth=9, run=6, rise=8)),
        ("Y", [(7, 0), (7, 5), (5.5, 6)], "bar"),
        ("H", flat(11.5, -1.5, +1, run=8, rise=3)),
        ("X", hitch(-16, 0, depth=6), "bar"),
        ("R", drag(-3.5, -5, +1, depth=3, run=14)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], title="Trey Snag"),
    why="Three routes, three depths, one side of the field, corner high, snag in the middle, "
        "flat low. Two defenders cannot cover three levels. This is the most reliable "
        "third-down play in football and it works against man or zone.",
    when="3rd &amp; 4 to 3rd &amp; 10. Also our go-to on the 20-yard-line when we need "
         "exactly one chunk.",
    read="Read the outside defender (the corner or flat player). If he sinks with the corner "
         "route, throw the flat. If he jumps the flat, throw the snag behind him. If both are "
         "covered, the corner route is one-on-one, take the shot.",
    assign=[
        ("Z", "Corner", "Inside release, stem to 9 yards, then break at 45° for the sideline "
                        "and keep climbing. Look over your outside shoulder. Cheat your split "
                        "in three yards so you have room to break to."),
        ("Y", "Snag", "Push to 5 to 6 yards like a slant, then sit down in the first open grass "
                      "and turn back to the QB. Against man, keep drifting away from your "
                      "defender. Against zone, freeze and show your hands."),
        ("H", "Flat", "Immediate release to the sideline at 2 to 3 yards of depth. Get your head "
                      "around by the time you are past Y. You will be wide open more than you "
                      "expect."),
        ("X", "Backside hitch", "Six yards, stop, turn in. If they leave you one-on-one with no "
                                "safety over the top, tell the QB before the snap and we will "
                                "convert this to a fade."),
        ("R", "Shallow cross", "Run underneath everything at 3 yards, all the way across. You "
                               "are the answer when the QB is flushed."),
        ("C", "Snap, sit at 5", "Snap, release straight, settle facing the QB."),
        ("QB", "Outside defender", "One defender decides this. Do not stare at the corner route, "
                                   "read the flat defender and throw off him."),
    ],
    coach="If the flat throw gets us 5 on 3rd &amp; 8, that is a bad play. Make the read off the "
          "flat defender, not off panic.",
)

# --- DROPBACK ---------------------------------------------------------------
play(
    id="smash", group="Dropback", name="Deuce Smash", call="&ldquo;Deuce Smash&rdquo;",
    tags=["Cover 2", "Cover 3", "Off man"],
    time="2.5 seconds",
    svg=diagram(DEUCE, [
        ("Z", corner(16, 0, depth=10, run=6, rise=8)),
        ("Y", hitch(9, 0, depth=6), "bar"),
        ("X", corner(-16, 0, depth=10, run=-6, rise=8)),
        ("H", hitch(-9, -1.5, depth=6), "bar"),
        ("R", swing(3.5, -5, +1)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], title="Deuce Smash"),
    why="Corner over hitch, run to both sides at once. Against Cover 2 the corner sits at "
        "5 to 7 yards and the safety plays the deep half, the corner route lands in the hole "
        "between them, which is the single softest spot in that coverage.",
    when="Any time we see two safeties. Also excellent against a corner who is squatting "
         "on our quick game after Sting has worked twice.",
    read="Read the deep safety to one side. If he stays wide and over the top of the corner "
         "route, throw the hitch underneath. If he squeezes to the middle, throw the corner. "
         "Two safeties means one of them has to be wrong, pick that side pre-snap.",
    assign=[
        ("Z", "Corner", "Stem hard at the corner's inside shoulder for 10 yards to make him "
                        "open his hips inside, then break out and up at 45°. Ball comes over "
                        "your outside shoulder toward the sideline."),
        ("X", "Corner", "Mirror image on the left."),
        ("Y", "Hitch", "Exactly 6 yards. Sink your hips, stop, come back one step toward the "
                       "QB, show your hands. Never drift, the QB is throwing to a spot."),
        ("H", "Hitch", "Mirror Y."),
        ("R", "Swing", "Outlet to the right. If nobody covers you, you will get 8 yards."),
        ("C", "Snap, sit at 5", "Middle outlet."),
        ("QB", "Safety on the strong side", "High to low. Corner first, hitch second, swing third. "
                                            "If the ball is not out by your third hitch step, "
                                            "take off, nobody is allowed to touch you."),
    ],
    coach="The corner route needs a real stem. If Z drifts outside from the start, the corner "
          "never turns and the throw is not there.",
)

play(
    id="mesh", group="Dropback", name="Deuce Mesh", call="&ldquo;Deuce Mesh&rdquo;",
    tags=["Man coverage", "Cover 0", "Bunch-beater"],
    time="2.5 to 3 seconds",
    svg=diagram(DEUCE, [
        ("H", drag(-9, -1.5, +1, depth=5, run=20)),
        ("Y", drag(9, 0, -1, depth=6.5, run=20)),
        ("X", stemgo(-16, 0, 17)),
        ("Z", stemgo(16, 0, 17)),
        ("R", swing(3.5, -5, +1)),
        ("C", hitch(0, 0, depth=4), "bar"),
    ], notes=[(0, 12.5, "X and Z must run off, or the safeties rob the mesh.")],
        title="Deuce Mesh"),
    why="Two crossers running opposite directions about a yard apart. In man coverage the two "
        "defenders have to choose between running into each other or going around, and either "
        "way somebody comes free. Nobody blocks anybody, the traffic does the work legally.",
    when="Any time they are in man. Any time a defender follows H across on motion. Also our "
         "best answer to an all-out rush.",
    read="Pre-snap, motion H and watch. If a defender travels with him, this is man and this "
         "play is the call. Post-snap read the first crosser to clear the mesh point.",
    assign=[
        ("H", "Under crosser (5 yards)", "Push to 5 yards, then run flat across the field. You go "
                                         "UNDER Y. Tight enough that you could touch him. Do not "
                                         "slow down and do not look for the ball until you are past "
                                         "the center."),
        ("Y", "Over crosser (6.5 yards)", "You go OVER H. Same speed rule, sprint through the mesh "
                                          "point. Against zone, sit down in the first window past "
                                          "the middle. Against man, keep running to the sideline."),
        ("X", "Clear vertical", "Full speed straight up. You are holding the safety. If you dog it, "
                                "that safety drops down and blows this play up."),
        ("Z", "Clear vertical", "Same. Take the top off."),
        ("R", "Swing / checkdown", "Slide to the right flat. If both crossers are covered, you are "
                                   "the ball."),
        ("C", "Snap, sit at 4", "Snap, then settle right behind the mesh as the emergency outlet."),
        ("QB", "First crosser out", "Eyes on the mesh point. Throw the crosser who comes out clean "
                                    "and lead him, he is running, so the ball goes in front of him."),
    ],
    coach="The number one way this play fails is the crossers slowing down at the mesh point. "
          "Run through it. Number two is X and Z jogging their clear-outs.",
)

play(
    id="flood", group="Dropback", name="Trey Flood", call="&ldquo;Trey Flood&rdquo;",
    tags=["Cover 3", "Any zone", "3rd &amp; long"],
    time="3 seconds",
    svg=diagram(TREY, [
        ("Z", corner(16.5, 0, depth=10, run=5, rise=9)),
        ("Y", out(7, 0, depth=9, run=10, dirn=1)),
        ("H", swing(11.5, -1.5, +1)),
        ("X", post(-16, 0, depth=11, run=9, rise=7, dirn=1)),
        ("R", drag(-3.5, -5, +1, depth=3, run=12)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], notes=[(-1, -7.5, "Three routes, three depths. Zone covers two.")],
        title="Trey Flood"),
    why="Deep corner, intermediate out, shallow swing, all to the same side. Cover 3 has "
        "exactly two defenders to that side of the field. Three into two does not go.",
    when="3rd &amp; 8 or longer. Any time we see a single deep safety in the middle with the "
         "corners bailing.",
    read="High to low, and be strict about it. Corner first, if he is open it is a touchdown. "
        "Out second, that is the completion most of the time. Swing third. Do not skip the "
        "corner just because the out is easier.",
    assign=[
        ("Z", "Corner", "Cheat your split in 2 yards. Stem to 10, break to the sideline and "
                        "climb toward the pylon. This is a vertical route to the corner, not "
                        "a flat out route."),
        ("Y", "Deep out", "Cheat your split in. Stem 9 yards hard upfield, sell vertical with "
                          "your eyes, then a flat 90° break to the sideline. Snap your head "
                          "around the instant you break."),
        ("H", "Swing", "Flat and wide immediately. Get outside the numbers and square up to the "
                       "QB. If the corner comes down to you, the out behind you is wide open, "
                       "keep running and pull him out."),
        ("X", "Backside post", "Stem 11 yards, break at 45° across the middle. If the single-high "
                               "safety chases the flood, you are running into an empty field. "
                               "Tell the QB pre-snap if you have one-on-one."),
        ("R", "Shallow cross", "Underneath at 3 yards, opposite the flood, as the scramble outlet."),
        ("C", "Snap, sit at 5", "Middle outlet."),
        ("QB", "Corner → out → swing", "Work the outside defender. If he gets depth to take the "
                                       "out, throw the swing. If he sits on the swing, the out is "
                                       "open all day."),
    ],
    coach="This is our best zone-beater and it should be our most-called play against a team "
          "that lives in Cover 3.",
)

play(
    id="dagger", group="Dropback", name="Trey Dagger", call="&ldquo;Trey Dagger&rdquo;",
    tags=["Cover 3", "Cover 1", "Chunk play"],
    time="3 seconds",
    svg=diagram(TREY, [
        ("H", stemgo(11.5, -1.5, 18, lean=-2)),
        ("Y", indig(7, 0, depth=13, run=-16, dirn=1)),
        ("Z", out(16.5, 0, depth=5, run=5, dirn=1)),
        ("X", comeback(-16, 0, depth=13, dirn=-1)),
        ("R", flat(-3.5, -5, -1, run=7, rise=2)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], notes=[(0, 19.5, "H clears the middle. Y runs into that space.")],
        title="Trey Dagger"),
    why="H runs a seam straight through the middle of the field and drags the deep middle "
        "defender with him. Y then runs a dig at 13 yards into exactly the grass H just "
        "emptied. It is a two-man play that manufactures a 15-yard completion on command.",
    when="2nd &amp; long, 3rd &amp; 10 to 15. Any time a safety is playing the middle of the "
         "field at 10 yards or less.",
    read="Watch the middle safety. He carries H → throw the dig. He sits at 10 and reads you "
         "→ throw the seam over his head to H.",
    assign=[
        ("H", "Seam / clear", "Sprint up the seam and lean slightly inside so the middle safety "
                              "has to honour you. You are the decoy 80% of the time and the "
                              "touchdown the other 20%, run it like the touchdown every rep."),
        ("Y", "Dig at 13", "Stem 13 yards straight upfield with your eyes up, then break flat "
                           "inside at 90°. Do not break early, the whole play depends on you "
                           "being behind the linebackers and under the safety."),
        ("Z", "Quick out at 5", "Hold the corner low and wide. You are the answer if they rush "
                                "everybody."),
        ("X", "Backside comeback", "Stem to 13, plant, and come back downhill to 10 toward the "
                                   "sideline. Your defender is in a full sprint, this is free "
                                   "separation."),
        ("R", "Flat left", "Outlet away from the concept."),
        ("C", "Snap, sit at 5", "Middle outlet."),
        ("QB", "Middle safety", "Take your time. This one needs the full three seconds and you "
                                "cannot be touched, so let it develop."),
    ],
    coach="Twenty yards is our first down. This play is designed to get all of it on one snap.",
)

play(
    id="verts", group="Dropback", name="Empty Verts", call="&ldquo;Empty Verts&rdquo;",
    tags=["Cover 2", "Cover 3", "2-minute"],
    time="2.5 seconds, on rhythm",
    svg=diagram(EMPTY, [
        ("X", stemgo(-17, 0, 18)),
        ("H", stemgo(-10, -1.5, 18, lean=1.5)),
        ("Y", stemgo(8, 0, 18, lean=-1.5)),
        ("R", stemgo(12.5, -1.5, 18)),
        ("Z", stemgo(17, 0, 18)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], notes=[(0, -7.5, "Five verticals against four deep defenders.")],
        title="Empty Verts"),
    why="Five receivers running vertically at a maximum of four deep defenders. There is no "
        "coverage in football that covers five verticals with seven players and still gets to "
        "the QB. This is a math play.",
    when="3rd &amp; 15+, end of half, and any time we need a shot. Also the best play to find "
         "out what coverage a team actually plays.",
    read="Count deep defenders as you walk to the line. Two deep → throw a seam between them "
         "(H or Y). Three deep → throw the seam bender between the corner and the middle "
         "safety, or take the outside if the corner squeezes. One deep → the two seams are "
         "one-on-one, pick the better matchup. Four deep → check to Snag.",
    assign=[
        ("X", "Outside vertical", "Stay outside the numbers. Do not drift into the middle of "
                                  "the field. Look for the ball at 15 yards over your outside "
                                  "shoulder."),
        ("Z", "Outside vertical", "Same on the right."),
        ("H", "Seam, bend to the middle", "Sprint up the seam. If you see two safeties, bend "
                                          "toward the middle of the field between them. If you "
                                          "see one safety in the middle, stay in the seam and "
                                          "run away from him."),
        ("Y", "Seam, bend to the middle", "Mirror H. You and H should not end up on top of each "
                                          "other, stay about 8 yards apart."),
        ("R", "Vertical, then settle at 12", "Run vertical. If nobody carries you, sit down at "
                                             "12 yards in the open window and show your hands."),
        ("C", "Snap, sit at 5", "Snap and settle underneath. Against an all-out rush you are the "
                                "hot throw, get your head around fast."),
        ("QB", "Count the deep defenders", "Pre-snap count, then throw on rhythm. Ball comes out "
                                           "at the top of the drop. Do not hold this, five "
                                           "verticals with a scramble is a broken play."),
    ],
    coach="This play is also our best diagnostic. Run it once early and we will know exactly "
          "what they play deep for the rest of the game.",
)

play(
    id="scissors", group="Dropback", name="Deuce Scissors", call="&ldquo;Deuce Scissors&rdquo;",
    tags=["Cover 2", "Single high", "Shot play"],
    time="3 seconds",
    svg=diagram(DEUCE, [
        ("Z", post(16, 0, depth=10, run=-10, rise=8, dirn=1)),
        ("Y", corner(9, 0, depth=12, run=9, rise=7, dirn=1)),
        ("X", slant(-16, 0, +1, depth=3, run=9)),
        ("H", flat(-9, -1.5, -1, run=7, rise=4)),
        ("R", swing(3.5, -5, +1)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], notes=[(1, -7.5, "Z and Y cross at 12. The safety takes one.")],
        title="Deuce Scissors"),
    why="The outside receiver runs a post, the slot runs a corner, and they cross. One safety "
        "has to choose. Whichever one he does not take is a 25-yard completion.",
    when="Any time we get a two-high look and we want a shot. Also great in the middle of the "
         "field on 1st &amp; 20 when they are not expecting a deep ball.",
    read="Isolate the safety on the right. He goes to the post → throw the corner. He widens "
         "to the corner → throw the post. If he stays flat-footed, take the post.",
    assign=[
        ("Z", "Post", "Cheat your split in 2 yards. Hard vertical stem to 10, then break 45° "
                      "across the field. Keep climbing, a flat post gets intercepted."),
        ("Y", "Corner (deeper)", "You break AFTER Z, at 12 yards, and you cross behind him. Stem "
                                 "inside first to sell the post, then break out. Timing is "
                                 "everything, if you break at the same depth as Z you collide."),
        ("X", "Slant", "Backside man-beater. If they are in man with no help, this is the "
                       "cheap 8 yards."),
        ("H", "Arrow", "Backside outlet to the sideline."),
        ("R", "Swing", "Late outlet right."),
        ("C", "Snap, sit at 5", "Middle outlet."),
        ("QB", "One safety, two routes", "Do not throw this off your back foot. Step into it. "
                                         "If neither is open, the backside slant is still there."),
    ],
    coach="Call this right after Smash has made them widen their safety. Same look, different "
          "answer.",
)

play(
    id="drive", group="Dropback", name="Trey Drive", call="&ldquo;Trey Drive&rdquo;",
    tags=["Cover 4", "Prevent", "Zone"],
    time="3 seconds",
    svg=diagram(TREY, [
        ("Y", indig(7, 0, depth=11, run=-14, dirn=1)),
        ("H", drag(11.5, -1.5, -1, depth=3.5, run=20)),
        ("Z", stemgo(16.5, 0, 17)),
        ("X", post(-16, 0, depth=9, run=8, rise=8, dirn=1)),
        ("R", flat(-3.5, -5, -1, run=8, rise=2)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], title="Trey Drive"),
    why="A shallow cross under a deep dig, both breaking into the middle. When a defense drops "
        "four players deep to stop our shots, the middle of the field at 10 yards is completely "
        "empty. Drive takes the yards they are giving away.",
    when="Any time they go to a four-deep prevent look, end of half, 4th &amp; long, or "
         "after we hit a deep ball on them.",
    read="Read the middle linebacker. He drops deep → throw the shallow underneath him. He sits "
         "flat → throw the dig behind him. If a safety jumps the dig, X's post is behind everyone.",
    assign=[
        ("Y", "Dig at 11", "Vertical stem to 11 yards, then a flat 90° break across the middle. "
                           "Keep running through the catch, this is a 6-yard-after-catch route."),
        ("H", "Shallow cross", "Get to 3 to 4 yards immediately and run flat across the whole field, "
                               "climbing a yard as you go. Stay under the linebackers. If the "
                               "QB scrambles, keep crossing."),
        ("Z", "Clear vertical", "Take the corner deep and get out of the middle."),
        ("X", "Backside post", "Stem 9, break across at 45°. The home-run option if a safety bites."),
        ("R", "Flat left", "Outlet."),
        ("C", "Snap, sit at 5", "Middle outlet."),
        ("QB", "Middle linebacker", "High to low, dig then shallow. This one is a rhythm throw, "
                                    "hit the dig as Y's head comes around."),
    ],
    coach="Against a prevent, taking 12 yards four times in a row is faster than one incomplete "
          "bomb. Trust the underneath throw.",
)

# --- SHOTS ------------------------------------------------------------------
play(
    id="wheel", group="Shot plays", name="Bunch Post-Wheel", call="&ldquo;Bunch Wheel&rdquo;",
    tags=["Man coverage", "Cover 1", "Touchdown play"],
    time="3.5 seconds",
    svg=diagram(BUNCH, [
        ("Y", post(8, 0, depth=11, run=-10, rise=8, dirn=1)),
        ("H", wheel(10.5, -2.5, +1, top=18)),
        ("Z", drag(13.5, 0, -1, depth=4, run=16)),
        ("X", stemgo(-16, 0, 16)),
        ("R", flat(-3.5, -5, -1, run=8, rise=2)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], notes=[(4, -7.5, "Bunch traffic, nobody blocks, they just collide.")],
        title="Bunch Post-Wheel"),
    why="From a bunch, H runs to the flat and then turns up the sideline. His defender has to "
        "fight through two other bodies to stay with him, and by the time he is out of the "
        "traffic H has ten yards of green. The wheel is open more often than any route we run.",
    when="Man coverage, especially at the 20-yard line and in. Also our favourite call after "
         "they have seen the bunch flat route once.",
    read="Wheel first. Post second. If both are covered, Z's drag is coming across underneath.",
    assign=[
        ("H", "Wheel", "Run flat to the sideline for 5 yards like a normal flat route, sell it, "
                       "then turn upfield and sprint. Stay a yard inside the sideline so the QB "
                       "has room to lay it outside you. Look over your outside shoulder at 12 yards."),
        ("Y", "Post", "Stem 11 yards, then break across at 45°. You are pulling the deep safety "
                      "away from the wheel. Run it like you want it."),
        ("Z", "Drag", "Release inside and run across at 4 yards. Your path through the bunch is "
                      "what makes H's defender go around."),
        ("X", "Clear vertical", "Take the backside corner deep and keep him out of the play."),
        ("R", "Flat left", "Outlet if the QB has to move."),
        ("C", "Snap, sit at 5", "Middle outlet."),
        ("QB", "Wheel, then post", "This is a touch throw over the top, not a fastball. Put it on "
                                   "the sideline at 20 yards and let H run to it."),
    ],
    coach="Nobody in this bunch may initiate contact. We are not picking, we are running routes "
          "close together and letting them sort it out. Hands in, no shoulders.",
)

play(
    id="stinggo", group="Shot plays", name="Deuce Sting-Go", call="&ldquo;Deuce Sting-Go&rdquo;",
    tags=["Double move", "Counterpunch", "Cover 1"],
    time="3.5 seconds",
    svg=diagram(DEUCE, [
        ("Z", double(16, 0, 5, -1, 17, 0)),
        ("Y", double(9, 0, 5, 5, 17, 1)),
        ("X", hitch(-16, 0, depth=6), "bar"),
        ("H", drag(-9, -1.5, +1, depth=4, run=14)),
        ("R", flat(3.5, -5, +1, run=8, rise=2)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], notes=[(0, -7.5, "Only after the short route has already worked.")],
        title="Deuce Sting-Go"),
    why="Same first five yards as Sting. Show the break, get the defender to plant his feet, "
        "then run past him. A double move only works if we have earned it with the real route "
        "first, which is why this is a second-half call.",
    when="After we have completed the same short route twice to the same defender and he has "
         "started to jump it.",
    read="Pre-snap, pick the defender who has been jumping our routes. Throw it to him. If he "
         "does not bite, the ball goes to the backside hitch, nothing forced.",
    assign=[
        ("Y", "Out and up", "Break the out at 5 yards, NOT 8. Sell it with your head and your "
                            "hands, show your palms like the ball is coming. Two steps, then "
                            "turn and go. Look over your outside shoulder at 15 yards."),
        ("Z", "Slant and go", "Three hard steps, plant inside like the slant, get his hips turned, "
                              "then push back vertical outside him."),
        ("X", "Hitch", "The safe answer. If nobody bites on the double moves, this ball is coming "
                       "to you at 6 yards, be ready."),
        ("H", "Drag", "Cross underneath at 4 yards as the outlet."),
        ("R", "Flat right", "Outlet."),
        ("C", "Snap, sit at 5", "Middle outlet."),
        ("QB", "The defender who has been cheating", "Give it the full count. Nobody can touch you, "
                                                     "so let the double move finish. Throw it deep "
                                                     "and outside, worst case it is incomplete."),
    ],
    coach="Set it up first. A double move on the first drive is a wasted play.",
)

# --- RUN GAME ---------------------------------------------------------------
play(
    id="jet", group="Run game", name="Split Jet", call="&ldquo;Split Jet Right&rdquo;",
    tags=["Run", "Motion", "Gets the edge"],
    time="Instant",
    svg=diagram(SPLIT, [
        ("H", [(-3.5, -6), (-1, -5.2), (3, -5.2), (9, -3), (15, 2)], "arrow"),
        ("QB", [(0, -5), (-1.5, -5.5)], "arrow", "dash"),
        ("Z", [(16, 0), (16, 6)], "arrow"),
        ("Y", [(8, 0), (11, 5)], "arrow"),
        ("R", [(3.5, -6), (-4, -4)], "arrow"),
        ("X", [(-16, 0), (-16, 6)], "arrow"),
    ], notes=[(-2, -8.5, "H is at full speed at the snap. Motion is legal.")],
        title="Split Jet"),
    why="The defense cannot rush and defend the edge at the same time. H is at full speed "
        "before the ball is snapped. If the edge defender takes a rush lane inside, this is "
        "an easy 10 yards.",
    when="Any time the rusher is coming hard off one edge. Any time a defense is playing all "
         "seven defenders deeper than 5 yards. Also the play that makes every play-action "
         "call believable.",
    read="Pre-snap. Look at the edge defender to the jet side. If he is inside the last receiver "
         "or rushing upfield, hand it off. If he is sitting outside, check to the other side.",
    assign=[
        ("H", "Jet motion, take the handoff", "Start your motion on the QB's first call and run "
                                              "FLAT behind him, not downhill. Take the ball at "
                                              "full speed, get outside the last defender's shoulder, "
                                              "then turn upfield. Do not cut back into the crowd."),
        ("QB", "Hand it, then fake the boot", "Turn and give it clean with two hands, then carry "
                                              "out a bootleg away from the play. Your fake is why "
                                              "Split Naked works later."),
        ("Y", "Get set outside", "Release to the edge and STOP moving before H arrives. A "
                                 "stationary body in a defender's path is legal screening, and a "
                                 "moving one is a 10-yard penalty."),
        ("Z", "Run off the corner", "Straight up the field. Take your defender out of the run fit."),
        ("X", "Run off the corner", "Same, backside."),
        ("R", "Fake opposite", "Take a hard step the other way to hold the backside defender, "
                               "then get set."),
        ("C", "Snap, then get set downfield", "Snap it and release to the play side, then stop. "
                                              "Do not chase and do not push anybody."),
    ],
    coach="Legal blocking here is standing still in the right place. Tell everyone to get to the "
          "spot early and freeze.",
)

play(
    id="rodeo", group="Run game", name="Split Draw", call="&ldquo;Split Draw&rdquo;",
    tags=["QB run", "3rd &amp; short", "Beats a deep drop"],
    time="Instant",
    svg=diagram(SPLIT, [
        ("QB", [(0, -5), (0, -3), (2, 1), (3, 8)], "arrow"),
        ("H", [(-3.5, -6), (-9, -4)], "arrow"),
        ("R", [(3.5, -6), (9, -4)], "arrow"),
        ("X", stemgo(-16, 0, 14)),
        ("Z", stemgo(16, 0, 14)),
        ("Y", [(8, 0), (8, 5)], "bar"),
    ], notes=[(0, -8.5, "Nobody has to rush here. If they drop 7, run it.")],
        title="Split Draw"),
    why="The rules say the QB does not have to be rushed in order to run. Some defenses will "
        "drop all seven and dare us to throw. This is how we make them pay, hold the ball for "
        "two counts, let everyone turn their back, and run through the middle.",
    when="3rd &amp; 4 or less. Any time a defense drops seven. Any time the rushers are running "
         "hard upfield past the QB.",
    read="Count the rushers. Zero or one rusher and everyone else backpedalling → run it. Two "
         "or more rushers → check to Sting.",
    assign=[
        ("QB", "Hold two counts, then go", "Stand tall, look downfield, pump once if you want. "
                                           "Then step up and run north. Slide out of bounds or "
                                           "spin, no diving, no hurdling, no flag guarding. "
                                           "Protect the ball with two hands in traffic."),
        ("H", "Widen left, get set", "Take two steps to the flat and stop. You are occupying the "
                                     "edge defender's eyes."),
        ("R", "Widen right, get set", "Same on the right."),
        ("X", "Clear vertical", "Full speed deep. Take your man with you."),
        ("Z", "Clear vertical", "Same."),
        ("Y", "Sit at 5", "Hold the middle linebacker with a route he has to respect, then get "
                          "out of the QB's running lane."),
        ("C", "Snap and get out of the way", "Snap it, take two steps to the left, and freeze. "
                                             "Do not wander into the running lane."),
    ],
    coach="Flag-guarding is a 10-yard penalty and it is called a lot. Coach the QB, hands off the "
          "flags, spin instead of stiff-arm, and get down when the play is over.",
)

play(
    id="naked", group="Run game", name="Split Naked", call="&ldquo;Split Naked Left&rdquo;",
    tags=["Play action", "Man or zone", "Explosive"],
    time="3 seconds",
    svg=diagram(SPLIT, [
        ("H", [(-3.5, -6), (-1, -5.2), (4, -5.2), (10, -4)], "arrow", "dash"),
        ("QB", [(0, -5), (-2, -6), (-8, -6), (-12, -4)], "arrow"),
        ("Y", drag(8, 0, -1, depth=5, run=18)),
        ("X", comeback(-16, 0, depth=12, dirn=-1)),
        ("Z", post(16, 0, depth=11, run=-13, rise=7, dirn=1)),
        ("R", flat(3.5, -6, -1, run=12, rise=4)),
    ], notes=[(-3, -8.5, "Fake the jet, boot away, throw on the run.")],
        title="Split Naked"),
    why="Everything looks like Jet. The linebackers chase, the safety squeezes down, and the QB "
        "is running the other way with three receivers open in front of him. This is our best "
        "explosive play because it uses their aggression against them.",
    when="Right after Jet has worked twice. 1st &amp; 20 in the middle of the field. Any time a "
         "linebacker is over-running the sweep.",
    read="On the run, work back to front, comeback then drag then flat. If nothing is open, keep running "
         ", you are outside the rush and nobody may touch you.",
    assign=[
        ("QB", "Fake jet, boot left", "Sell the handoff with both hands and your eyes, then get "
                                      "your shoulders around and run to the left flat. Throw on "
                                      "the move with your feet under you. If nothing is open at "
                                      "the sideline, run, the first down beats the bad throw."),
        ("H", "Fake the jet, keep running", "Sell the sweep all the way to the sideline. You will "
                                            "take at least one defender with you."),
        ("Y", "Deep drag", "Cross at 5 yards toward the boot side and keep climbing. You are the "
                           "primary, you should be running into open grass at 10 yards."),
        ("X", "Comeback", "Stem to 12 and come back downhill toward the sideline. You are the "
                          "deep option on the boot side."),
        ("Z", "Backside post", "Cross the field. If the safety chases the boot, you are the "
                               "touchdown."),
        ("R", "Flat to the boot side", "Get outside fast and turn to face the QB at 3 yards. You "
                                       "are his easy first down."),
        ("C", "Snap and get set", "Snap, then release opposite the boot and stop moving."),
    ],
    coach="The fake is the play. If the QB does not sell it with his eyes, this is just a slow "
          "rollout.",
)

# --- RED ZONE ---------------------------------------------------------------
play(
    id="rzsting", group="Red zone", name="Bunch Sting", call="&ldquo;Bunch Sting&rdquo;",
    tags=["Goal line", "Man coverage", "Inside the 5"],
    time="1.5 seconds",
    svg=diagram(BUNCH, [
        ("Z", slant(13.5, 0, -1, depth=2, run=8)),
        ("Y", flat(8, 0, +1, run=9, rise=2)),
        ("H", [(10.5, -2.5), (10.5, 1), (10.5, 5)], "bar"),
        ("X", slant(-16, 0, +1, depth=2, run=8)),
        ("R", flat(-3.5, -5, -1, run=8, rise=2)),
        ("C", hitch(0, 0, depth=3), "bar"),
    ], title="Bunch Sting"),
    why="Inside the 5 there is no room for deep routes, so we win with traffic. Three receivers "
        "in a four-yard box release in three different directions and man defenders collide.",
    when="Goal to go, inside the 5. Also the 3-yard PAT.",
    read="Flat first, it is the easiest completion. If they widen for the flat, throw the slant "
         "behind it. If they collapse, H is sitting at 5 in the end zone.",
    assign=[
        ("Z", "Quick slant", "Two steps and break inside flat. You are running behind Y's flat "
                             "release. Catch it and get the ball across the line."),
        ("Y", "Flat", "Immediate release to the corner of the end zone at 2 yards of depth. Head "
                      "around instantly."),
        ("H", "Sit at 5 in the end zone", "Release straight through the traffic and stop at 5 "
                                          "yards deep in the end zone. Show your hands and do "
                                          "not drift."),
        ("X", "Backside slant", "One-on-one answer if they overload the bunch."),
        ("R", "Flat left", "Outlet."),
        ("C", "Snap, sit at 3", "Snap and settle at the goal line."),
        ("QB", "Flat → slant → H", "Fast. This ball is out before the rush arrives. Throw it "
                                   "low and away from the defender, an incompletion inside the "
                                   "5 is fine, an interception is not."),
    ],
    coach="Reminder for the 3-yard PAT, this is a one-point play. Do the math on the "
          "scoreboard before you call it.",
)

play(
    id="fade", group="Red zone", name="Empty Corner", call="&ldquo;Empty Corner&rdquo;",
    tags=["Goal line", "Press man", "2-point / 3-point PAT"],
    time="2 seconds",
    svg=diagram(EMPTY, [
        ("Z", corner(17, 0, depth=5, run=3, rise=6)),
        ("X", corner(-17, 0, depth=5, run=-3, rise=6)),
        ("R", flat(12.5, -1.5, +1, run=6, rise=3)),
        ("H", flat(-10, -1.5, -1, run=6, rise=3)),
        ("Y", [(8, 0), (8, 6)], "bar"),
        ("C", hitch(0, 0, depth=3), "bar"),
    ], title="Empty Corner"),
    why="Five receivers, no backfield, so the defense has to cover every blade of grass in a "
        "small space. The back-pylon corner route is the throw a defender in press coverage "
        "cannot see coming.",
    when="Goal to go against press man. The 10-yard PAT (2 points) and the 20-yard PAT "
         "(3 points).",
    read="Pick your matchup before the snap. Corner playing inside → back pylon. Corner playing "
         "outside → Y sitting in the middle.",
    assign=[
        ("Z", "Back-pylon corner", "Outside release, stem to 5, then break for the back pylon. "
                                   "Look over your outside shoulder. High-point it, this ball is "
                                   "thrown where only you can get it."),
        ("X", "Back-pylon corner", "Mirror on the left."),
        ("R", "Flat", "Occupy the flat defender and pull him away from the corner route."),
        ("H", "Flat", "Same on the left."),
        ("Y", "Sit at 6 in the middle", "Release and settle in the middle of the end zone. Against "
                                        "zone you are usually the open man."),
        ("C", "Snap, sit at 3", "Goal-line outlet."),
        ("QB", "Your best matchup", "Ball outside and up, away from the defender's inside hand. "
                                    "Two feet in bounds, remind the receivers."),
    ],
    coach="Extra-point math, 3 yards is 1 point, 10 yards is 2 points, 20 yards is 3 points. Down 9? "
          "Score and take the 20-yard try to tie it.",
)

# --- TRICK PLAYS ------------------------------------------------------------
TRICK = []


def trick(**kw):
    TRICK.append(kw)


trick(
    id="ladder", group="Trick", name="Rodeo (Hook &amp; Ladder)", call="&ldquo;Rodeo&rdquo;",
    tags=["4th &amp; long", "End of half", "Low risk"],
    legal="This is legal. The forward pass to Y is our one forward pass. The pitch to H is BACKWARD, "
          "so it does not count as a second forward pass. And if H drops it, a fumble is dead "
          "where it hits the ground and <strong>we keep the ball</strong>, this play cannot "
          "turn the ball over.",
    svg=diagram(DEUCE, [
        ("Y", hitch(9, 0, depth=11), "bar"),
        ("H", [(-9, -1.5), (-2, 3), (5, 9), (11, 11.5)], "arrow", "dash"),
        ("Z", stemgo(16, 0, 18)),
        ("X", stemgo(-16, 0, 18)),
        ("R", flat(3.5, -5, +1, run=8, rise=2)),
        ("C", hitch(0, 0, depth=5), "bar"),
    ], notes=[(0, -7.5, "Y catches at 11, then pitches BACKWARD to H.")],
        title="Rodeo hook and ladder"),
    why="Y catches a routine hitch at 11 yards. Every defender collapses on him to pull the flag. "
        "H is already running full speed behind him and takes a backward pitch into an empty "
        "sideline.",
    when="4th &amp; 15 or more. Last play of a half. Any time we have already completed two "
         "hitches to Y and the defense is flying up to it.",
    assign=[
        ("Y", "Hitch at 11, then pitch", "Catch it, turn upfield one step so they commit to you, "
                                         "then flip it backward and underhand to H. The pitch "
                                         "must be behind you or level, never forward."),
        ("H", "Run the ladder", "Start toward the middle at the snap and time your path to arrive "
                                "just behind and outside Y as he catches it. Full speed. Take the "
                                "pitch and run for the sideline, not the middle."),
        ("Z", "Clear vertical", "Take the deep defender out of the picture."),
        ("X", "Clear vertical", "Same."),
        ("R", "Flat right", "Stay out of the pitch lane."),
        ("C", "Snap, sit at 5", "Emergency outlet if the hitch is not there."),
        ("QB", "Hitch on time", "Throw the hitch on rhythm at 11 yards. Nothing fancy, the "
                                "trick happens after the catch."),
    ],
    coach="Practise the pitch ten times before we ever call it. If the pitch goes forward it is "
          "an illegal forward pass. If it hits the ground it is just a dead ball and our next down.",
)

trick(
    id="special", group="Trick", name="Omaha Special (double pass)", call="&ldquo;Omaha&rdquo;",
    tags=["Shot", "Once per game", "Cover 3"],
    legal="This is legal. The QB's flip to H must be clearly BACKWARD, that is a lateral, not a pass. "
          "H's throw downfield is then our one and only forward pass. If the flip is even "
          "slightly forward, we have thrown two forward passes and it is a penalty.",
    svg=diagram(DEUCE, [
        ("QB", [(0, -5), (-4, -6)], "arrow", "dash"),
        ("H", [(-9, -1.5), (-6, -4), (-4, -6.5), (-2, -6.5)], "arrow", "dash"),
        ("X", [(-16, 0), (-16, 5), (-15, 17)], "arrow"),
        ("Z", stemgo(16, 0, 18)),
        ("Y", drag(9, 0, -1, depth=4, run=14)),
        ("R", flat(3.5, -5, +1, run=8, rise=2)),
        ("C", hitch(0, 0, depth=4), "bar"),
    ], notes=[(-1, -8.8, "QB flips BACKWARD  •  H throws the forward pass.")],
        title="Omaha double pass"),
    why="The defense sees a swing pass to H behind the line and every defender in the secondary "
        "drives forward. X, who has been running a lazy route, turns on the jets and there is "
        "nobody within twenty yards of him.",
    when="Once a game, in the middle of the field, on 1st or 2nd down when they are not expecting "
         "it. Never in our own end.",
    assign=[
        ("QB", "Backward flip to H", "Turn and toss it clearly behind H, soft, two hands, chest "
                                     "high. Then get set and go stand still. Do not run downfield."),
        ("H", "Catch, look, throw", "Come back behind the line to catch it. Take two steps toward "
                                    "the sideline to sell a run, get your eyes up, and throw X's "
                                    "go route. <strong>You must throw from behind the line of "
                                    "scrimmage.</strong> If X is covered, tuck it and run."),
        ("X", "Lazy stem, then go", "Jog the first three steps like you are blocking or running a "
                                    "hitch, then sprint. Sell it, this whole play is your acting. "
                                    "Look over your inside shoulder at 20 yards."),
        ("Z", "Clear vertical", "Take the deep defender on your side out of the middle."),
        ("Y", "Drag", "Cross underneath as H's safety valve."),
        ("R", "Flat right", "Second outlet, get in H's vision fast."),
        ("C", "Snap, sit at 4", "Snap and stay behind the line."),
    ],
    coach="Whoever throws the second pass needs to actually be able to throw. Pick that guy in "
          "practice, not in the huddle.",
)

trick(
    id="boomerang", group="Trick", name="Boomerang (flea flicker)", call="&ldquo;Boomerang&rdquo;",
    tags=["Shot", "Off the run game", "Single high"],
    legal="This is legal. The handoff to R is a forward handoff behind the line, which the rules allow. "
          "R's pitch back to the QB is backward. The QB's deep ball is our one forward pass.",
    svg=diagram(SPLIT, [
        ("QB", [(0, -5), (-1, -4.5)], "arrow", "dash"),
        ("R", [(3.5, -6), (1, -4), (-1, -4), (0, -5.5)], "arrow", "dash"),
        ("Z", post(16, 0, depth=13, run=-11, rise=6, dirn=1)),
        ("X", stemgo(-16, 0, 18)),
        ("Y", drag(8, 0, -1, depth=5, run=15)),
        ("H", flat(-3.5, -6, -1, run=9, rise=3)),
    ], notes=[(0, -8.8, "Hand it, take it back, then throw it deep.")],
        title="Boomerang flea flicker"),
    why="Safeties in this league come downhill on the run fast because the run is real. Give the "
        "ball, take it back, and throw over the top of a safety who is already at 5 yards.",
    when="After Jet or Draw has gained yards. Best on 1st or 2nd down in the middle of the field, "
         "with a single deep safety.",
    assign=[
        ("QB", "Give, take, throw", "Full handoff mechanics, the fake has to be real. Take the "
                                    "pitch back, reset your feet, and throw the post. Do not "
                                    "throw it flat-footed, step into it."),
        ("R", "Take it and give it back", "Take the handoff, take two hard steps downhill so the "
                                          "linebackers commit, then flip it back underhand to the "
                                          "QB. Backward only."),
        ("Z", "Deep post", "Run it like a normal vertical for 13 yards, do not tip the play by "
                           "running deeper than usual, then break across at 45° behind the safety."),
        ("X", "Clear vertical", "Run off your corner and hold him."),
        ("Y", "Drag", "Cross at 5 as the outlet when the shot is not there."),
        ("H", "Flat", "Sell the run fake, then get to the flat as the checkdown."),
        ("C", "Snap and get set", "Snap it and stop. Do not release downfield early."),
    ],
    coach="Two exchanges means two chances to drop it. Remember, a dropped ball is dead where it "
          "lands and we keep it. Worst case is a loss of yards, not a turnover.",
)

trick(
    id="zorro", group="Trick", name="Zorro (reverse pass)", call="&ldquo;Zorro&rdquo;",
    tags=["Shot", "Off Jet", "Man coverage"],
    legal="This is legal. The handoff to H is behind the line. H's throw is the one forward pass, and "
          "it must be released from behind the line of scrimmage.",
    svg=diagram(SPLIT, [
        ("H", [(-3.5, -6), (0, -5.2), (5, -5), (11, -4.5)], "arrow"),
        ("QB", [(0, -5), (-3, -6.5), (-8, -6)], "arrow", "dash"),
        ("Y", [(8, 0), (8, 4), (4, 12), (-2, 16)], "arrow"),
        ("Z", [(16, 0), (16, 6), (16, 15)], "arrow"),
        ("X", drag(-16, 0, +1, depth=6, run=13)),
        ("R", [(3.5, -6), (-2, -4)], "arrow"),
    ], notes=[(2, -8.8, "H takes the jet, then throws back to Y.")],
        title="Zorro reverse pass"),
    why="It is Jet, which we have already run, until H pulls up. Every defender is chasing the "
        "sweep with their backs turned. Y has released quietly up the seam and bent across the "
        "field into a completely empty middle.",
    when="After Jet has gained yards at least twice. 2nd &amp; medium, middle of the field.",
    assign=[
        ("H", "Take the jet, then throw", "Run the sweep exactly like Jet, same speed, same path. "
                                          "At 3 yards from the sideline, plant, get your eyes up, "
                                          "and throw Y's crosser. <strong>Stay behind the line.</strong> "
                                          "If Y is covered, run it, you are already on the edge."),
        ("QB", "Give and boot away", "Clean handoff, then boot the opposite way to occupy the "
                                     "backside defender."),
        ("Y", "Sneak up the seam, bend across", "Release quietly at three-quarter speed for 4 yards "
                                                "so nobody carries you, then bend across the middle "
                                                "climbing to 15. Get your head around early, H is "
                                                "not a quarterback and needs a big target."),
        ("Z", "Clear vertical", "Sprint deep and take the deep defender out of the middle."),
        ("X", "Drag", "Cross underneath toward the throwing side as the safe outlet."),
        ("R", "Fake and get set", "Fake opposite, then stop moving."),
        ("C", "Snap and get set", "Snap and freeze. Nobody blocks downfield while moving."),
    ],
    coach="This is the highest-upside trick play we have because the run action is genuine. It "
          "only works if Jet has been real all game.",
)

trick(
    id="bandit", group="Trick", name="Bandit (direct snap)", call="&ldquo;Bandit&rdquo;",
    tags=["Short yardage", "4th &amp; 2", "Tempo"],
    legal="This is legal. The snap goes to R, who is off the line and stationary, and he is more than "
          "two yards behind the ball. The rules only forbid a direct snap to the quarterback, "
          "a snap to a player on the line, and a snap to a player in motion.",
    svg=diagram([("X", -16, 0), ("C", 0, 0), ("QB", -7, -1), ("R", 0, -5),
                 ("H", 4, -5), ("Y", 8, 0), ("Z", 16, 0)], [
        ("R", [(0, -5), (1, -2), (3, 2), (5, 7)], "arrow"),
        ("H", [(4, -5), (9, -4)], "arrow"),
        ("Y", [(8, 0), (10, 4)], "arrow"),
        ("Z", stemgo(16, 0, 14)),
        ("X", stemgo(-16, 0, 14)),
    ], notes=[(-7, -3.5, "QB aligns as a wing"), (0, -8.5, "Snap goes straight to R. No exchange.")],
        title="Bandit direct snap"),
    why="No handoff means no time wasted. On 4th &amp; 2 the ball is moving forward the instant "
        "it is snapped, and the defense is still identifying who has it.",
    when="4th &amp; 2 or less. Also good on the 3-yard PAT.",
    assign=[
        ("R", "Take the snap and go", "Align 5 yards behind the ball, dead still for a full second. "
                                      "Catch it and go straight north off Y's hip. No dancing. "
                                      "Two hands on the ball."),
        ("QB", "Align as a wing, run a route", "Line up 7 yards to the left, off the line. You are "
                                               "a decoy and an outlet. Stay within 15 yards of the "
                                               "ball or it is a 5-yard penalty."),
        ("H", "Get set on the edge", "Release outside and stop moving before R gets there."),
        ("Y", "Get set inside", "Two steps to the play side and freeze. Hands behind your back."),
        ("Z", "Clear vertical", "Take your defender deep."),
        ("X", "Clear vertical", "Same."),
        ("C", "Snap it back 5 yards, clean", "This is the whole play. Practise this exact snap. "
                                             "Through the legs or side-pitch, but the ball must be "
                                             "still on the ground until you snap it."),
    ],
    coach="Everyone freezes for one full second before the snap or this is a false start. Count it "
          "out loud in practice.",
)


# Attach filter metadata and the beginner explainers.
from .tags import decorate  # noqa: E402

decorate(P)
decorate(TRICK)
