import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents = []
            return drawn
        drawn = []
        for _ in range(num_balls):
            index = random.randint(0, len(self.contents) - 1)
            drawn.append(self.contents.pop(index))
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        success = True
        for color, count in expected_balls.items():
            if drawn.count(color) < count:
                success = False
                break
        if success:
            successes += 1
    return successes / num_experiments
