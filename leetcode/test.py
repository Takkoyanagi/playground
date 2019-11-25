# def lengthOfLongestSubstring(self, s: str) -> int:
#     l, r = 0, 0
#     result = 0
#     letters = set()
#     while r < len(s):
#         if s[r] in letters:
#             letters.remove(s[l])
#             l += 1
#         else:
#             letters.add(i)
#             r += 1
#             result = max(result, r-l)
#     return result
import scipy.stats as st
print(st.norm.cdf(2.58))
