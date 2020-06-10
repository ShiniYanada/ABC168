n = int(input()) % 10
output = 'hon'

if n == 3:
  output = 'b' + output[1:]
elif n in [0, 1, 6, 8]:
  output = 'p' + output[1:]

print(output)
