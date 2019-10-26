from typing import List
import random

# Fisher Yates Algorithm

# Time Complexity
# O(n)
# Runs in linear time, as generating random index and swapping two vals
# Can be done in constant time

# Space Complexity
# O(n)
# Managed to avoid using linear space on the auxillary array from the brute
# force approach, however, still need it for the reset!!


class Shuffler():
    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        """Resets the array to its original configuration and returns it"""
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        """Returns a random shuffling of the array"""

        for i in range(len(self.array)):
            print(f'i {i}')
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array


if __name__ == '__main__':
    nums = [1, 2, 7, 9, 4]
    obj = Shuffler(nums)
    param1 = obj.reset()
    param2 = obj.shuffle()
