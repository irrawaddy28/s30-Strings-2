'''
28 Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Let M = len(needle), N = len(character)
Solution
1. Sliding window: For each character starting from index i of the haystack string, get the next M-1 characters of haystack (by slicing haystack, i.e., haystack[i:i+M]) to extract a substring of length M, and then check if it matches the needle string. If there's a match, the function returns the current index i. If there is no match, increase i to i+1 and slice again. If we reach the end of the haystack then we return -1 as the needle was not found.

Thus, at each index i, we perform a string match between the substring of haystack and needle which takes O(M) time. The index i itself runs from 0 to N-M which is O(N-M). Thus, the total time is O((N-M)*M) = O(NM - M^2) = O(NM)

Time: O(NM), Space: O(1)

2. KMP (Knuth-Morris-Pratt) algorithm:
KMP algorithm is a bit complicated and may be done at a later stage.
https://blog.seancoughlin.me/find-the-index-of-the-first-occurrence-in-a-string-naive-and-kmp-solutions
https://www.youtube.com/watch?v=GTJr8OvyEVQ
https://www.youtube.com/watch?v=JoF0Z7nVSrA
Time: O(N+M), Space: O(1)
'''


def strStrSlidingWindow(haystack: str, needle: str) -> int:
    ''' Time: O(NM), Space: O(1) '''
    if not needle:
        return 0

    M = len(needle)
    N = len(haystack)
    start = -1
    for hi in range(N-M+1): # O(N)
        if haystack[hi:hi+M] == needle: # O(M)
            start = hi
            break
    return start

def run_strStr():
    tests = [("sadbutsad", "sad", 0), ("leetcode","leeto", -1), ('aaaab', 'aab', 2), ("aaaaa","bba", -1), ("icecreamice", "mice", 7), ]
    for test in tests:
        haystack, needle, ans = test[0], test[1], test[2]
        print(f"\nNeedle = {needle}")
        print(f"Haystack = {haystack}")
        for method in ['SlidingWindow']:
            if method == 'SlidingWindow':
                index = strStrSlidingWindow(haystack, needle)
            print(f"{method}: Index of Needle in Haystack = {index}")
            success = (ans == index)
            print(f"Pass: {success}")
            if not success:
                return

run_strStr()