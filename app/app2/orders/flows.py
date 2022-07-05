# П1 or П2 
class OrdersFlow:

    def __init__(self, tau) -> None:
        self.tau = tau
        self.intervals

    @property    
    def intervals(self):
        intervals = []
        for i in range(1,len(self.tau)):
            intervals.append(self.tau[i] - self.tau[i-1])
        return intervals

    @property
    def intervals_len(self):
        return  len(self.intervals or [])