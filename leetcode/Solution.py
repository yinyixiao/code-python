# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums))[i + 1:]:
                if nums[i] + nums[j] == target:
                    return [i, j]

    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
    """

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r = re
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        if (carry > 0):
            r.next = ListNode(1)
        return re.next

    # 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_number = 0
        number = 0
        test = ''
        for i in s:
            if i not in test:
                test += i
                number += 1

            else:
                if number >= max_number:
                    max_number = number
                index = test.index(i)
                test = test[(index + 1):] + i
                number = len(test)
        if number > max_number:
            max_number = number
        return max_number


s = Solution()
print(s.find_longest_no_repeat_substr("abcabcbb"))
