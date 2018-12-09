start = 'hit'
 end = 'cog'


 def find_path(start, end):
     first = list(start)
     final = list(end)
     if start == end:
         return "start = end"
     else:
         for i in range(len(start)):
             for j in range(ord('a'), ord('z')+1):
                 if first[i] == final[i]:
                     break
                 else:
                     print(''.join(first))
                     first[i] = chr(j)
         print(''.join(first))


 find_path(start, end)