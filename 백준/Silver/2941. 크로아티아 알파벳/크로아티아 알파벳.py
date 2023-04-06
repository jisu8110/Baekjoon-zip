arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

msg = input()

for i in arr :
  msg = msg.replace(i, '*')
print(len(msg))