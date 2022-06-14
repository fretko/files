filename=input()
if "MZ" or "ZM" in filename:
  print(filename[0:2])
  print('executable, OS Windows')
else: 
  print('non-executable')
