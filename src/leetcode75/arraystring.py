class ArrayString:

    @classmethod
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """ LC #1768
            You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

            Return the merged string.
        """
        results = []

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                results.append(word1[i])
            if i < len(word2):
                results.append(word2[i])
            i += 1
        
        return "".join(results)


    @classmethod
    def reverseVowels(self, s: str) -> str:
        """ LC #345
            Given a string s, reverse only all the vowels in the string and return it.

            The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
        """
        vowels = set("a e i o u".split())
        l, r = 0, len(s) - 1
        while l < r:
            print(s[l], ',', s[r])
            if s[l] in vowels and s[r] in vowels:
                tmp = s[l]
                s[l] = s[r]
                s[r] = tmp
                l += 1
                r -= 1
            if s[l] not in vowels:
                l+=1
            if s[r] not in vowels:
                r -= 1