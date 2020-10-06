#!/usr/bin/python

import collections

class Result:
    def __init__(self, left, right):
        if left is None or right is None:
            raise ValueError("One of the card is empty")
            return

        self.left = left
        self.right = right

    # compare hands. only designed for 5 card hands.
    # return 1(win), 0(lose), -1(tie)
    def compare(self):
        left_value = self.left.getvalue()
        right_value = self.right.getvalue()

        if left_value > right_value:
            return 1
        elif left_value < right_value:
            return 0
        else:
            if left_value == 3:
                return self.compare_two_pair()
            if left_value == 2 or left_value == 4:
                return self.compare_pair()
            return self.compare_cards()

    def compare_cards(self):
        right = self.right.getlist()
        left = self.left.getlist()

        result_right = 0
        result_left = 0
        for value in left:
            result_left = result_left + value
        for value in right:
            result_right = result_right + value

        if result_left > result_right:
            return 1
        elif result_left < result_right:
            return 0
        else:
            return -1

    def compare_pair(self):
        right = self.right.getlist()
        left = self.left.getlist()

        seen_right = set(set([x for x in right if right.count(x) > 1]))
        seen_left = set(set([x for x in left if left.count(x) > 1]))

        x = seen_left.pop()
        y = seen_right.pop()
        if x > y:
            return 1
        elif x < y:
            return 0
        else:
            return -1

    def compare_two_pair(self):
        right = self.right.getlist()
        left = self.left.getlist()

        result_left = 0
        biggest_left = 0
        result_right = 0
        biggest_right = 0
        for value in [item for item, count in collections.Counter(right).items() if count > 1]:
            result_right += value
            if value > biggest_right:
                biggest_right = value
        for value in [item for item, count in collections.Counter(left).items() if count > 1]:
            result_left += value
            if value > biggest_left:
                biggest_left = value

        if biggest_left > biggest_right:
            return 1
        elif biggest_left < biggest_right:
            return 0
        else:
            if result_left > result_right:
                return 1
            elif result_left < result_right:
                return 0
            else:
                return -1
