class BullyAlgorithm:
    def __init__(self, processes, coordinator=None):
        self.p, self.c = processes, coordinator or max(processes)

    def is_alive(self, pid): return pid in self.p

    def hold_election(self, initiator):
        print(f"Process {initiator} starts election.")
        higher = [p for p in self.p if p > initiator]
        if not higher:
            self.c = initiator
            print(f"Process {initiator} becomes the new coordinator.")
        else:
            [print(f"Process {initiator} sends election to {p}.") for p in higher]
            responses = [p for p in higher if self.is_alive(p)]
            if responses:
                print(f"Process {initiator} gets responses from: {responses}")
                self.hold_election(max(responses))
            else:
                self.c = initiator
                print(f"No higher processes responded. Process {initiator} becomes coordinator.")

# Usage
BullyAlgorithm([1, 2, 3, 5, 6]).hold_election(3)


# python bully.py          

