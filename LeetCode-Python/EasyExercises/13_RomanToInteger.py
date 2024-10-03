class Solution:
  def romanToInt(self, s: str) -> int:
    values: dict[str, int] = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000
    }

    specials = {
      "IV": 4,
      "IX": 9,
      "XL": 40,
      "XC": 90,
      "CD": 400,
      "CM": 900
    }

    result = 0
    if "IV" in s:
      s = s.replace("IV", "")
      result += 4
    if "IX" in s:
      s = s.replace("IX", "")
      result += 9
    if "XL" in s:
      s = s.replace("XL", "")
      result += 40
    if "XC" in s:
      s = s.replace("XC", "")
      result += 90
    if "CD" in s:
      s = s.replace("CD", "")
      result += 400
    if "CM" in s:
      s = s.replace("CM", "")
      result += 900

    for c in s:
      if c not in values:
        return 0
      result += values[c]
    return result
sol = Solution()
sol.romanToInt("MCMXCIV")
    