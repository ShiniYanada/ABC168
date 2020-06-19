import math

a, b, h, m = list(map(int, input().split()))
deg = 30 * h - 6 * m + 30 * (m / 60.0)
if deg < 0:
  deg += 360
elif deg > 180:
  deg = 360 - deg

cos = math.cos(math.radians(deg))
c_2 = a * a + b * b - 2 * a * b * cos
print(math.sqrt(c_2))
