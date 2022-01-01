TIMER_UNTIL_SPAWN = 6
TIMER_NEW_FISH = 8

class Fish:

    def __init__(self, timer):
        self._timer = timer

    @property
    def timer(self):
        return self._timer

    @timer.setter
    def timer(self, timer):
        self._timer = timer

    # Returns new fish if spawned, else None
    def get_older(self):
        if self._timer == 0:
            self._timer = TIMER_UNTIL_SPAWN
            return Fish(TIMER_NEW_FISH)
        else:
            self._timer -= 1
            
    def will_spawn_another_fish(self, curr_day, total_days):
        days_left_in_simulation = total_days - curr_day
        return self.timer < days_left_in_simulation

    # Returns the total number of fish spawned including self
    def simulate_days(self, curr_day, total_days):
        if (self.will_spawn_another_fish(curr_day, total_days)):
            sim_days = self.timer + 1
            curr_day += sim_days
            self.timer = TIMER_UNTIL_SPAWN
            return self.simulate_days(curr_day, total_days) + Fish(TIMER_NEW_FISH).simulate_days(curr_day, total_days)
        else:
            return 1

    def __hash__(self):
        return hash((self._timer))

    def __eq__(self, o):
        if isinstance(o, Fish):
            return self.timer == o.timer
        return False

    def __repr__(self):
        return str(self._timer)
