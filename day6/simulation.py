from file_reader import FileReader

class Simulation:
    def __init__(self, fishes, days):
        self.fishes = fishes
        self.days = days

    def run(self):
        new_fishes = []

        for _ in range(0, self.days):
            for fish in self.fishes:
                spawned = fish.get_older()
                if spawned:
                    new_fishes.append(spawned)

            self.fishes = self.fishes + new_fishes
            new_fishes = []

        return self.fishes


if __name__ == "__main__":
    fishes = FileReader('input.txt').process_file()
    simulation = Simulation(fishes, 100)

    res = simulation.run()
    print(len(res))
