class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
      pref_str = strs[0]
      len_pref = len(pref_str)

      for s in strs[1:]:
        while pref_str != s[0:len_pref]:
          len_pref -= 1
          if len_pref == 0:
             return ""
          pref_str = pref_str[0:len_pref]
      return pref_str

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))