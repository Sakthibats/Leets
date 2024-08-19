class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        for string in strs[1:]:
            # Find the common prefix between the current prefix and the next string
            while string[:len(prefix)] != prefix:
                # Shorten the prefix by one character until they match
                prefix = prefix[:-1]
                # If prefix becomes empty, there's no common prefix
                if not prefix:
                    return ""
        return prefix
