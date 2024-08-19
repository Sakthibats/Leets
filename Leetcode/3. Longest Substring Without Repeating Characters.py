class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
            return len(s)
        hasht = {}
        start = 0
        maxx = 0
        for i, item in enumerate(s):
            if item in hasht:
                start = max(start, hasht[item]+1)
            hasht[item] = i
            maxx = max(maxx, i-start+1)
        return maxx
            