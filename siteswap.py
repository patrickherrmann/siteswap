import sys

if (len(sys.argv) >= 4):
    props = int(sys.argv[1])
    maxheight = int(sys.argv[2])
    maxlength = int(sys.argv[3])
    exclude = map(lambda x: int(x), sys.argv[4:])
else:
    props = 4
    maxheight = 6
    maxlength = 5
    exclude = [0]

tossHeights = filter(lambda x: x not in exclude, range(maxheight + 1))
groundState = map(lambda x: x < props, range(maxheight + 1))

def buildSiteswap(pattern, wheel, length):
    availTosses = filter(lambda x: not wheel[x], tossHeights)
    if not wheel[0]: availTosses = availTosses[:1]

    if len(pattern) > 0 and wheel == groundState:
        print "".join(str(x) for x in pattern)
    elif length > 0:
        for toss in availTosses:
            nextPattern = list(pattern)
            nextPattern.append(toss)
            buildSiteswap(nextPattern, performToss(list(wheel), toss), length - 1)

def performToss(wheel, toss):
    wheel[toss] = True
    del wheel[0]
    wheel.append(False)
    return wheel

buildSiteswap([], groundState, maxlength)