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
from scipy.stats import chi2, t
# print((1-st.norm.cdf(8.125))*2)
# print(st.norm.pdf(-8.125))

# calc z-score from power
print(st.norm.ppf(0.90))

# p_values = scipy.stats.norm.sf(abs(z_scores)) #one-sided

# p_values = st.norm.sf(abs(0.80))*2  # twosided
# print(p_values)

# print(1-chi2.cdf(5.89, 3))
# print((t.cdf(-1.54, 49))*2)
# t-test confidence interval
# print(t.interval(0.90, 14))
