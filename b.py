s=input("Enter a string")
while s!='':
   slen0=len(s)
   ch=s[0]
   s=s.replace(ch,'')
   slen1=len(s)
   if slen1==slen0-1:
      print("first non repeating character",ch)
      break
   else:
      print("non repeating character")