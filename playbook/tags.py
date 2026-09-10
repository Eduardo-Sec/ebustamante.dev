"""Filter metadata, beginner explainers, glossary, penalty chart and drills.

PLAY_META is keyed by the play id in plays.py. Everything in here is optional, so a
play with no entry still renders, it just will not show up under any filter.

Vocabulary used by the filters, keep new entries inside these lists or the chips in
the filter bar will not match anything.

  depth      quick, intermediate, deep
  family     pass, run, screen, trick
  beats      man, cover 2, cover 3, cover 4, blitz
  situations 1st down, 3rd & short, 3rd & long, red zone, goal line, 2 minute, backed up
  formation  Deuce, Trey, Bunch, Empty, Split
"""

DEPTHS = ["quick", "intermediate", "deep"]
FAMILIES = ["pass", "run", "screen", "trick"]
BEATS = ["man", "cover 2", "cover 3", "cover 4", "blitz"]
SITUATIONS = ["1st down", "3rd & short", "3rd & long", "red zone", "goal line",
              "2 minute", "backed up"]
FORMATIONS = ["Deuce", "Trey", "Bunch", "Empty", "Split"]

FILTER_GROUPS = [
    ("depth", "how far", DEPTHS),
    ("family", "type", FAMILIES),
    ("beats", "beats", BEATS),
    ("situ", "situation", SITUATIONS),
    ("form", "formation", FORMATIONS),
]


def _m(depth, family, form, beats, situ, basics):
    return {"depth": depth, "family": family, "form": form,
            "beats": beats, "situ": situ, "basics": basics}


PLAY_META = {
    "sting": _m(
        "quick", "pass", "Deuce", ["man", "blitz"], ["1st down", "backed up"],
        "Two receivers on each side run the same pair of routes, one cutting in and one "
        "cutting out. The defender covering them can only take one. Whichever one he does "
        "not take is the throw. Nothing about this play is complicated, it is just fast."),
    "bubble": _m(
        "quick", "screen", "Deuce", ["cover 3", "cover 4"], ["1st down", "backed up"],
        "A screen is a short throw where the yards come after the catch rather than from "
        "the throw itself. We cannot block with our hands in this league, so instead the "
        "outside receiver sprints deep and drags his defender away, and the catch happens "
        "in the space he left behind."),
    "snag": _m(
        "quick", "pass", "Trey", ["man", "cover 2", "cover 3"],
        ["3rd & short", "red zone", "1st down"],
        "Three receivers on one side at three different heights, one deep, one at six "
        "yards, one right at the sideline. Two defenders cannot stand at three heights, so "
        "one of the three is always open. The quarterback picks by watching the defender "
        "closest to the sideline."),
    "smash": _m(
        "intermediate", "pass", "Deuce", ["cover 2", "cover 3", "man"],
        ["1st down", "3rd & long"],
        "One receiver stops at six yards, the one outside him runs deep toward the corner "
        "of the field. The defender has to choose short or deep. This is the same idea as "
        "Sting but stretched up the field instead of across it."),
    "mesh": _m(
        "intermediate", "pass", "Deuce", ["man", "blitz"],
        ["1st down", "3rd & short", "red zone"],
        "Two receivers run straight across the field in opposite directions and pass within "
        "a yard of each other. If the defenders are in man coverage they have to go around "
        "each other to keep up, and one of them loses. Nobody is blocking, the traffic just "
        "happens."),
    "flood": _m(
        "intermediate", "pass", "Trey", ["cover 3", "cover 2", "cover 4"],
        ["3rd & long"],
        "Send three receivers to one side of the field at three depths. Zone defenses only "
        "put two defenders on that side, so it is three against two and somebody is free. "
        "That is the whole idea, and it is why this is our best play against a team sitting "
        "in zone."),
    "dagger": _m(
        "deep", "pass", "Trey", ["cover 3", "man"], ["3rd & long"],
        "One receiver runs straight up the middle to pull the deep defender with him, and a "
        "second receiver cuts into the exact spot the first one just emptied. It is a two "
        "man play where the first guy is bait."),
    "verts": _m(
        "deep", "pass", "Empty", ["cover 2", "cover 3"], ["3rd & long", "2 minute"],
        "Five receivers run straight up the field. Defenses only have three or four players "
        "deep, so somebody is uncovered by arithmetic. The quarterback counts the deep "
        "defenders before the snap and throws to whichever lane has nobody standing in it."),
    "scissors": _m(
        "deep", "pass", "Deuce", ["cover 2", "man"], ["1st down"],
        "Two receivers cross each other about twelve yards downfield, one heading for the "
        "middle and one for the sideline. The single deep defender behind them can only "
        "follow one. Whichever he leaves is a big play."),
    "drive": _m(
        "intermediate", "pass", "Trey", ["cover 4", "cover 2"], ["3rd & long", "2 minute"],
        "When a defense drops four players deep to stop big plays, the middle of the field "
        "at ten yards is completely empty. This play puts two receivers in that empty space "
        "at two different depths and takes the yards the defense is giving away."),
    "wheel": _m(
        "deep", "pass", "Bunch", ["man"], ["red zone", "3rd & long"],
        "A wheel route starts out looking like a short throw to the sideline and then turns "
        "straight up the field. From a bunch, where three receivers stand close together, "
        "the defender has to fight through two other bodies to keep up and by then it is "
        "too late."),
    "stinggo": _m(
        "deep", "pass", "Deuce", ["man", "cover 2"], ["1st down"],
        "A double move. The receiver runs the first five yards of a route we have already "
        "completed twice, gets the defender to plant his feet expecting it again, then runs "
        "past him. It only works because of the plays we ran earlier, so never call it in "
        "the first quarter."),
    "jet": _m(
        "quick", "run", "Split", ["blitz", "cover 2"], ["1st down", "3rd & short"],
        "One player is already running sideways at full speed when the ball is snapped, "
        "takes a handoff and turns the corner. The defense cannot chase the quarterback and "
        "defend the sideline at the same time."),
    "rodeo": _m(
        "quick", "run", "Split", ["cover 4", "cover 3"], ["3rd & short", "goal line"],
        "A draw is a run that looks like a pass. The quarterback stands still for two counts "
        "so every defender turns and runs backwards, then he takes off through the space "
        "they just left. Nobody is required to rush him in this league, so this happens more "
        "than you would think."),
    "naked": _m(
        "intermediate", "pass", "Split", ["man", "cover 3"], ["1st down"],
        "Play action means faking a run and then throwing. Here the quarterback fakes the "
        "sweep, runs the opposite way, and throws on the move. The defenders who chased the "
        "fake are now behind the play."),
    "rzsting": _m(
        "quick", "pass", "Bunch", ["man", "blitz"], ["red zone", "goal line"],
        "Close to the goal line there is no room for deep routes, so we win with traffic. "
        "Three receivers standing within four yards of each other release in three "
        "directions and the defenders run into each other."),
    "fade": _m(
        "quick", "pass", "Empty", ["man"], ["red zone", "goal line"],
        "A fade is a ball thrown high and outside where only your receiver can reach it. "
        "From five wide the defense has to cover the whole end zone, and the back corner is "
        "the hardest spot on the field to defend."),
    "ladder": _m(
        "deep", "trick", "Deuce", ["cover 4", "cover 3"], ["3rd & long", "2 minute"],
        "A receiver catches a normal short pass, every defender runs at him, and he flips "
        "the ball backwards to a teammate already sprinting past. Backward passes are "
        "unlimited in this league and a dropped one is not a turnover, so the downside is "
        "small."),
    "special": _m(
        "deep", "trick", "Deuce", ["cover 3", "cover 4"], ["1st down"],
        "The quarterback tosses the ball backwards to a receiver, which does not count as a "
        "pass. The defense sees a short play and runs forward. That receiver then throws the "
        "real pass deep to somebody nobody is covering any more."),
    "boomerang": _m(
        "deep", "trick", "Split", ["man", "cover 3"], ["1st down"],
        "Hand the ball off, let the defense commit to the run, then have the runner flip it "
        "back to the quarterback who throws it deep. Two exchanges means two chances to drop "
        "it, but a dropped ball is dead where it lands and we keep it."),
    "zorro": _m(
        "intermediate", "trick", "Split", ["man", "cover 2"], ["1st down"],
        "It is the jet sweep, exactly the same, until the runner stops and throws instead. "
        "Every defender is chasing him with their back to the field. This only works if we "
        "have actually been running the sweep for real."),
    "bandit": _m(
        "quick", "trick", "Split", ["blitz"], ["3rd & short", "goal line"],
        "The ball is snapped straight to the running back with no handoff at all, so it is "
        "moving forward the instant it is live. The quarterback lines up off to the side as "
        "a decoy. Short yardage only."),
}

COVERAGE_BASICS = {
    "two": "Zone coverage means each defender guards an area of grass rather than a person. "
           "In Cover 2, two players split the deep part of the field in half between them "
           "and four more cover the short areas. It gives up short catches and almost never "
           "gives up a long one.",
    "pipe": "Same as Cover 2 with one change. The middle linebacker sprints straight up the "
            "middle of the field instead of staying short, which plugs the one gap Cover 2 "
            "leaves open.",
    "three": "Three defenders split the deep field into thirds instead of halves. More "
             "coverage deep, less coverage short. Call it against a team that keeps throwing "
             "over our heads.",
    "four": "Four defenders deep and only two short. We are openly giving them short catches "
            "and taking away everything long. Since they need twenty yards for a first down, "
            "making them do it in five yard pieces is usually a win for us.",
    "one": "Man coverage means you follow one person wherever he goes. Cover 1 is man on "
           "everybody with one extra defender free in the deep middle as a safety net.",
    "zero": "Man coverage on all six eligible receivers with nobody left over. Tight "
            "coverage, no help anywhere, and one missed step is a touchdown. Best used near "
            "the goal line where there is nowhere deep to run.",
    "dog": "A blitz. Two rushers instead of one, so the quarterback has half the usual time. "
           "We accept that one receiver is left uncovered because the throw should not have "
           "time to happen.",
    "trap": "A bluff. The corners line up deep so it looks like they are worried about a long "
            "pass, then jump the short throw the moment the quarterback commits to it. This "
            "is how we get interceptions.",
}

GLOSSARY = [
    ("Line of scrimmage",
     "The imaginary line across the field where the ball is sitting. Neither team crosses it "
     "until the ball is snapped."),
    ("Zone line to gain",
     "Our version of a first down marker. The field is cut into four twenty yard zones and we "
     "get four downs to reach the next line, not ten yards."),
    ("Snap",
     "The center handing the ball backwards between his legs to start the play. In this "
     "league it has to travel at least two yards."),
    ("Shotgun",
     "The quarterback standing several yards behind the center instead of right up against "
     "him. It is the only legal setup here."),
    ("Two point stance",
     "Standing up with your hands off the ground. Required for everyone before every snap."),
    ("Eligible receiver",
     "Anyone allowed to catch a forward pass. In this league that is all seven of us, "
     "including the center."),
    ("Route",
     "The path a receiver runs. Every route is a promise about where you will be and when."),
    ("Stem",
     "The straight part of a route before the cut. A good stem makes the defender turn and "
     "run before you break."),
    ("Break",
     "The moment you change direction. That is where separation is created, not with raw "
     "speed."),
    ("Release",
     "How you get off the line past the defender in front of you, inside or outside."),
    ("Cushion",
     "The gap between a defender and the receiver he is covering. Managing it is the whole "
     "job in man coverage."),
    ("Leverage",
     "Which shoulder a defender is standing on. Inside leverage means he is protecting the "
     "middle and giving you the sideline."),
    ("Man coverage",
     "Each defender is responsible for one specific person and follows him everywhere."),
    ("Zone coverage",
     "Each defender is responsible for an area, and covers whoever runs into it."),
    ("Safety",
     "A defender who starts deep, behind everybody else. Counting how many there are is the "
     "first thing the quarterback does."),
    ("Seam",
     "The vertical lane between the middle of the field and the sideline. It is where zone "
     "defenses are thinnest."),
    ("Flat",
     "The short area near the sideline, within about five yards of the line of scrimmage."),
    ("Hook or curl zone",
     "The short middle area, roughly eight to twelve yards deep, where receivers sit down "
     "against zone."),
    ("Deep half, third, quarter",
     "How many pieces the deep part of the field has been split into, which tells you which "
     "coverage you are facing."),
    ("Blitz",
     "Sending more than one rusher at the quarterback. It gets there faster and leaves "
     "somebody uncovered."),
    ("Contain",
     "The rusher's job of never letting the quarterback escape to the outside."),
    ("Spy",
     "A defender assigned to watch the quarterback and nothing else, in case he runs."),
    ("Robber",
     "A defender with no assigned man who floats underneath looking for a ball to "
     "intercept."),
    ("Hot route",
     "The quick throw a receiver converts to when he sees extra rushers coming. Nobody calls "
     "it, you just see it and do it."),
    ("Checkdown",
     "The safe short throw the quarterback takes when the real reads are covered."),
    ("Progression",
     "The order the quarterback looks at receivers. First, second, checkdown, then run."),
    ("High low",
     "Putting two receivers at two different depths on one defender so he has to pick one."),
    ("Flood",
     "Putting three receivers at three depths on one side of the field. Zone cannot cover it."),
    ("Clear out",
     "A route run purely to drag a defender away from where the ball is actually going. If "
     "you jog it, the play dies."),
    ("Rub or pick",
     "Two receivers running close together so their defenders collide. Legal here as long as "
     "nobody actually blocks anybody."),
    ("Motion",
     "A player moving sideways before the snap. Watching whether a defender follows him is "
     "how we tell man from zone."),
    ("Play action",
     "Faking a run before throwing, to pull the defenders forward."),
    ("Boot",
     "The quarterback running to one side of the field after a fake, throwing on the move."),
    ("Draw",
     "A run disguised as a pass."),
    ("Double move",
     "Faking one route and then running a different, deeper one. Only works after the real "
     "route has already worked."),
    ("Scramble rules",
     "What every receiver does once the quarterback leaves the pocket. Deep stays deep, "
     "intermediate breaks to the sideline he is running toward, shallow comes back to him."),
    ("Chunk play",
     "Any single play that gains twelve or more. We need one per drive because a first down "
     "is twenty yards."),
    ("Flag guarding",
     "Using your hand, arm or body to stop somebody pulling your flag. Ten yards, and it gets "
     "called constantly."),
]

PENALTY_5 = [
    ("Illegal equipment", "Jewelry, an untucked shirt, pockets, a flag covered by clothing."),
    ("Delay of game", "More than twenty five seconds from the referee marking it ready."),
    ("Substitution infraction", "Coming on or off outside a dead ball."),
    ("Encroachment", "Crossing into the neutral zone before the snap. Dead ball."),
    ("False start", "Moving after the one second freeze. Dead ball, and the one we will get "
                    "most often."),
    ("Illegal snap", "Moving the ball before the actual snap, or snapping to someone on the "
                     "line or in motion. Dead ball."),
    ("Player not within 15 yards of the ball", "No hiding a receiver by the sideline."),
]

PENALTY_10 = [
    ("Roughing the passer", "Any contact at all with the quarterback. Automatic first down."),
    ("Defensive pass interference", "Contact that stops a receiver catching it. Automatic "
                                    "first down."),
    ("Offensive pass interference", "Pushing off downfield before the ball is touched. Loss "
                                    "of down."),
    ("Flag guarding", "Swatting, stiff arming, running bent over, lowering your head."),
    ("Illegal flag belt removal", "Pulling the belt of somebody who does not have the ball."),
    ("Illegally secured belt on a touchdown", "Loss of down and no score."),
    ("Illegal blocking", "Hands out, moving into a defender, or blocking downfield while "
                         "still moving."),
    ("Obstruction or holding the runner", "Grabbing anything other than the flag."),
    ("Attempt to steal the ball", "Swiping at the ball instead of the belt. Measured from the "
                                  "end of the run."),
    ("Tackling, tripping, clipping, hurdling", "Any of it. Flagrant versions get you thrown "
                                               "out."),
    ("Unnecessary contact", "Contact with an opponent who is already on the ground."),
    ("Unsportsmanlike conduct", "Taunting or excessive celebration. Judgment call, cannot be "
                                "protested."),
    ("Spiking, kicking or throwing the ball during a dead ball", "Hand it to the official."),
    ("Fair catch interference", "Not giving the punt returner a chance at the ball."),
    ("Running a play after declaring a punt", "There is no such thing as a fake punt here."),
    ("Two or more consecutive encroachments", "The second one costs ten instead of five."),
]

DRILLS = [
    ("Snap and freeze",
     "Five minutes, every warm up",
     "Line up, hold dead still for a full second on a count, then snap. The one second rule "
     "is the penalty we will get flagged for most, and it is fixed entirely by repetition. "
     "Add the center's side pitch and the five yard direct snap to the same block."),
    ("Routes on air at real depth",
     "Five minutes, every warm up",
     "Cones at 5, 8, 11 and 13 yards. Receivers run the route tree with the actual "
     "quarterback throwing. The point is depth accuracy, not catching. If two receivers run "
     "the same route at different depths, we have a problem worth fixing before a game does "
     "it for us."),
    ("Flag pull circuit",
     "Ten minutes, every practice",
     "Ball carrier runs at three quarter speed inside a ten yard box, defender breaks down "
     "at two yards and pulls. Coach the hips, not the ball. Second rep, defender starts with "
     "bad angle and has to use the sideline."),
    ("Coverage recognition",
     "Ten minutes",
     "Line up seven defenders in one of our eight calls, quarterback has five seconds to say "
     "the coverage out loud before the snap. Rotate through Two, Three, One and Zero. This is "
     "the single highest value drill for the quarterback and it needs no throwing."),
    ("Mesh and pitch",
     "Ten minutes",
     "Crossers at full speed through the mesh point without slowing down or colliding. Then "
     "ten clean backward pitches for Rodeo. Ten in a row clean or the trick play does not go "
     "in the game plan."),
    ("Two minute, live",
     "End of every practice",
     "Ball on our own 20, ninety seconds, one timeout. Offense has to score. It forces tempo, "
     "the spike, sideline routes and clock awareness all at once, and it is the closest thing "
     "to a real game we can simulate at practice."),
]

CARD_PLAYS = ["sting", "bubble", "snag", "smash", "mesh", "flood", "jet", "rzsting"]
CARD_COVERAGES = ["two", "three", "one"]


def decorate(items):
    """Merge PLAY_META into the play dicts, in place."""
    for p in items:
        meta = PLAY_META.get(p["id"])
        if not meta:
            continue
        p["depth"] = meta["depth"]
        p["family"] = meta["family"]
        p["form"] = meta["form"]
        p["beats"] = meta["beats"]
        p["situ"] = meta["situ"]
        p["basics"] = meta["basics"]
        # Pipe separated, not space separated. Several filter values contain a
        # space of their own ("cover 2", "3rd & long"), so the separator has to
        # be a character that cannot appear inside a value.
        p["f_beats"] = "|".join(meta["beats"])
        p["f_situ"] = "|".join(meta["situ"])
    return items


def decorate_coverages(items):
    for c in items:
        c["basics"] = COVERAGE_BASICS.get(c["id"], "")
    return items
