while true:
  print("enter '0' for exit.")
  ch=input("enter character: ")
  if (ch=='0'):
    break
  else:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
      print(ch,"is an alphabet.\n")
    else:
      print(ch,"is not an alphabet.\n")
