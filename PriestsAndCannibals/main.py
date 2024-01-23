openList = []
closedListLeft = []  # Closed list for the left bank
closedListRight = []  # Closed List for the right bank


class State:
    p = 3  # This is will always be for the left bank only
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


def generateStatesWhenGoingToTheLeftbank(currentState):
    newStates = []

    p, c = currentState.p, currentState.c

    if (p + 2) <= 3:
        state = State(p + 2, c, 0)
        if not inClosedList(state, closedListLeft):
            newStates.append(state)

    if (c + 2) <= 3:
        state = State(p, c + 2, 0)
        if not inClosedList(state, closedListLeft):
            newStates.append(state)
    if (p + 1) <= 3 and (c + 1) <= 3:
        state = State(p + 1, c + 1, 0)
        if not inClosedList(state, closedListLeft):
            newStates.append(state)

    if (p + 1) <= 3:
        state = State(p + 1, c, 0)
        if not inClosedList(state, closedListLeft):
            newStates.append(state)
    if (c + 1) <= 3:
        state = State(p, c + 1, 0)
        if not inClosedList(state, closedListLeft):
            newStates.append(state)
    for state in newStates:
        print(state)


def generateStateWhenGoingToTheRightbank(currentState):
    newStates = []

    p, c = currentState.p, currentState.c

    if (p - 2) >= 0:
        state = State(p - 2, c, 1)
        if not inClosedList(state, closedListLeft):
            newStates.append(state)

    if (c - 2) >= 0:
        state = State(p, c - 2, 1)
        if not inClosedList(state, closedListLeft):
            newStates.append(state)
    if (p - 1) >= 0 and (c - 1) >= 0:
        state = State(p - 1, c - 1, 1)
        if not inClosedList(state, closedListLeft):
            newStates.append(state)

    if (p - 1) >= 0:
        state = State(p - 1, c, 1)
        if not inClosedList(state, closedListLeft):
            newStates.append(state)
    if (c - 1) >= 0:
        state = State(p, c - 1, 1)
        if not inClosedList(state, closedListLeft):
            newStates.append(state)
    for state in newStates:
        print(state)


state = State(3, 3, 0)
generateStateWhenGoingToTheRightbank(state)
state = State(0, 0, 1)
generateStatesWhenGoingToTheLeftbank(state)


