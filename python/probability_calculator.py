# https://replit.com/@VincentEdwards1/boilerplate-probability-calculator

# This is a project from freecodecamp.org. 
# This program determines the approximate probability of drawing certain balls randomly from a hat. 
# It contains a Hat class and an experiment function. 

import copy
import random


class Hat:
    def __init__(self, **ball_and_amount):
        contents = []
        for ball, amount in ball_and_amount.items():
            contents.extend([ball] * amount)
        self.contents = contents

    def draw(self, amount: int) -> list:
        '''Remove the argument amount of balls from the hat and return them in a list of strings. If the argument exceeds the available quantity, all the balls are returned.'''
        drawn_balls = []
        for i in range(min(amount, len(self.contents))):
            n = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(n))
        return drawn_balls

    def get_contents_dict(self) -> dict:
        '''Return the contents of the hat as a dictionary of ball (key) amount (value) pairs.'''
        return self.ball_list_to_dict(self.contents)

    @staticmethod
    def ball_list_to_dict(ball_list: list) -> dict:
        '''Return the items in the argument ball_list as a dictionary of ball (key) amount (value) pairs.'''
        ball_dict = {}
        for ball in ball_list:
            ball_dict[ball] = ball_dict.get(ball, 0) + 1
        return ball_dict

    def __repr__(self):
        return f'Hat(**{self.get_contents_dict()})'


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    '''Return the experimentally determined probability of drawing at least expected_balls from hat when num_balls_drawn are pulled out by performing num_experiments trials.'''
    success_count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat) #another way to deep copy Hat objects is with eval(repr(hat))
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = hat.ball_list_to_dict(drawn_balls)
        if all(amount <= drawn_balls_dict.get(ball, 0) for ball, amount in expected_balls.items()): success_count += 1
    return success_count / num_experiments



if __name__ == "__main__":
    # random.seed(95)
    hat = Hat(blue=4, red=2, green=6)
    probability = experiment(
        hat=hat,
        expected_balls={"blue": 2,
                        "red": 1},
        num_balls_drawn=4,
        num_experiments=3000)
    print("Probability:", probability)
