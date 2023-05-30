class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        for letter in s:
            letters.append(letter)

        unique_letters = list(set(letters))

        freq_count = []
        for letter in unique_letters:
            freq_count.append(s.count(letter))

        sorted_letters = [letter for _,letter in sorted(zip(freq_count,unique_letters),reverse=True)]

        final_display = []

        for letter in sorted_letters:
            count = s.count(letter)
            for i in range(count):
                final_display.append(letter)

        return ''.join(final_display)