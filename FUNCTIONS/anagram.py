def is_anagram(s1, s2):
   s1 = s1.lower()
   s2 = list(s2.lower())
   if len(s1) != len(s2):
      return False
   for ch in s1:
      if ch in s2:
         s2.remove(ch)
      else:
         return False
   return  True
print(is_anagram("mid", "dim"))
         

