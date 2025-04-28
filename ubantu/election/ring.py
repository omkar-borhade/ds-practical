class RingAlgorithm:
    def __init__(self, processes):
        self.ring = sorted(processes)
        self.coordinator = None

    def is_alive(self, pid): return pid in self.ring

    def hold_election(self, initiator):
        print(f"Process {initiator} starts election.")
        election = [initiator]
        idx = self.ring.index(initiator)
        while True:
            idx = (idx + 1) % len(self.ring)  
            nxt = self.ring[idx]             
            if nxt == initiator:              
                break
            print(f"Election message from {election[-1]} to {nxt}")
            election.append(nxt)

        #while (nxt := self.ring[(idx := (idx + 1) % len(self.ring))]) != initiator:
        #    print(f"Election message from {election[-1]} to {nxt}")
        #    election.append(nxt)
        self.coordinator = max(election)
        print(f"Process {self.coordinator} is elected as the new coordinator.")

# Usage
RingAlgorithm([1, 2, 4, 6]).hold_election(2)
#  python ring.py   

