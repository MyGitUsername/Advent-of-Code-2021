class Fish:
    def __init__(self, timer):
        self._timer = timer
    
    @property
    def timer(self):
        return self._timer

    # Returns new fish if spawned, else None
    def get_older(self):
        if self._timer == 0:
            self._timer = 6
            return Fish(8)
        else:
            self._timer -= 1
            
    def __eq__(self, o):
        if isinstance(o, Fish):
            return self.timer == o.timer
        return False

    def __repr__(self):
        return str(self._timer)
