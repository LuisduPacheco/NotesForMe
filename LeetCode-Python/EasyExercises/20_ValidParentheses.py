class Solution:
    def isValid(self, s: str) -> bool:
        open_char = ["{", "[", "("]
        close_char = ["}", "]", ")"]
        characters = open_char + close_char
        temp = []
        
        for c in s:
            if c not in characters:
                print("1")
                return False
            if c == "{":
                temp.append("}")
            if c == "[":
                temp.append("]")
            if c == "(":
                print("se agregó )")
                temp.append(")")
        print(temp)
        for c in s:
            if c not in characters:
                print("2")
                return False
            if c in close_char:
              if c == temp[0]:
                  temp.pop(0)
              else:
                  print("3")
                  return False
        print("A")
        
        return True
    
sol = Solution()
sol.isValid("([])")