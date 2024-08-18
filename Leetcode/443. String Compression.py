class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars.append("EXIT")
        prev = chars[0]
        count = 0
        index = 0
        for ind, char in enumerate(chars):
            if char == prev:
                count +=1
            else:
                chars[index] = prev
                index+=1
                if count>1:
                    for num_string in str(count):
                        chars[index] = num_string
                        index += 1
                prev = char
                count = 1
        return index