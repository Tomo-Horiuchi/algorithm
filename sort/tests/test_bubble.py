import random

import bubble


class TestSort:

    def test_bubble_sort(self):
        
        nums = [random.randint(0, 1000) for i in range(10)]
        assert in_order(nums) is False
        sorted_nums = bubble.bubble_sort(nums)
        assert in_order(sorted_nums) is True
        


def in_order(nums: list[int]) -> bool:
        """[ソートが出来ているかの検証]

        Args:
            nums (List[int]): [検証対象]

        Returns:
            bool: [検証結果]
        """
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))