openList = []
closedListLeft = []  # Closed list for the left bank
closedListRight = []  # Closed List for the right bank


class State:
    p = 3  # This is for the left bank only
    c = 3
    total_cost = -1
    boatDirection = -1  # 0 boat is in the left bank  and 1 means boat is in the right bank

    def __init__(self, p, c, bd):
        self.p = p
        self.c = c
        self.boatDirection = bd

    def __eq__(self, other):
        return self.p == other.p and self.c == other.c

    def __str__(self):
        return f"""
        Left Bank : {self.p}M {self.c}C
        Right Bank : {3 - self.p}M {3 - self.c}C
        Boat Direction : {"R" if self.boatDirection else "L"}
        """


currentLeftBank = State(0, 0, 0)
currentRightBank = State(0, 0, 0)


def inClosedList(current_state, closedList):
    for state in closedList:
        if current_state == state:
            return True
    return False


def isAValidState(state):
    pl = state.p
    cl = state.c
    pr = 3 - state.p
    cr = 3 - state.c

    if cr > pr > 0:  # This is to handle the edge case in which the priest might not be there in the bank at all
        return False
    if cl > pl > 0:
        return False

    return True


def generateStatesWhenGoingToTheLeftbank(currentState):
    newStates = []

    p, c = currentState.p, currentState.c

    if (p + 2) <= 3:
        state = State(p + 2, c, 0)
        if not inClosedList(state, closedListLeft) and isAValidState(state):
            newStates.append(state)

    if (c + 2) <= 3:
        state = State(p, c + 2, 0)
        if not inClosedList(state, closedListLeft) and isAValidState(state):
            newStates.append(state)
    if (p + 1) <= 3 and (c + 1) <= 3:
        state = State(p + 1, c + 1, 0)
        if not inClosedList(state, closedListLeft) and isAValidState(state):
            newStates.append(state)

    if (p + 1) <= 3:
        state = State(p + 1, c, 0)
        if not inClosedList(state, closedListLeft) and isAValidState(state):
            newStates.append(state)
    if (c + 1) <= 3:
        state = State(p, c + 1, 0)
        if not inClosedList(state, closedListLeft) and isAValidState(state):
            newStates.append(state)
    return newStates


def generateStateWhenGoingToTheRightbank(currentState):
    newStates = []

    p, c = currentState.p, currentState.c

    if (p - 2) >= 0:
        state = State(p - 2, c, 1)
        if not inClosedList(state, closedListLeft) and isAValidState(state):
            newStates.append(state)

    if (c - 2) >= 0:
        state = State(p, c - 2, 1)
        if not inClosedList(state, closedListLeft) and isAValidState(state):
            newStates.append(state)
    if (p - 1) >= 0 and (c - 1) >= 0:
        state = State(p - 1, c - 1, 1)
        if not inClosedList(state, closedListLeft) and isAValidState(state):
            newStates.append(state)

    if (p - 1) >= 0:
        state = State(p - 1, c, 1)
        if not inClosedList(state, closedListLeft) and isAValidState(state):
            newStates.append(state)
    if (c - 1) >= 0:
        state = State(p, c - 1, 1)
        if not inClosedList(state, closedListLeft) and isAValidState(state):
            newStates.append(state)

    return newStates


state = State(3, 3, 0)

closedListRight.append(state)
openList.append(state)

while state != State(0, 0, 1):
    if state.boatDirection == 0:
        newStates = generateStateWhenGoingToTheRightbank(state)
        openList.extend(newStates)
        for genState in newStates:
            openList.extend(generateStatesWhenGoingToTheLeftbank(genState))

    else:
        newStates = generateStateWhenGoingToTheRightbank(state)
        openList.extend(newStates)
        for genState in newStates:
            openList.extend(generateStateWhenGoingToTheRightbank(genState))


    break

for state in openList:
    print(state)