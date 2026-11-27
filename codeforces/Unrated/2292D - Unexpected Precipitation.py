import sys


def solve():
  data = sys.stdin.read().split()
  if not data:
    return

  t = int(data[0])
  idx = 1
  out = []

  for _ in range(t):
    n = int(data[idx])
    idx += 1

    x = list(map(int, data[idx : idx + n]))
    idx += n
    y = list(map(int, data[idx : idx + n]))
    idx += n

    dp = 0
    for i in range(n - 1, -1, -1):
      a = x[i] - y[i]
      dp = max(a + dp, -dp)

    if dp > 0:
      out.append("Sunny")
    elif dp < 0:
      out.append("Aubrey")
    else:
      out.append("Draw")

  sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
  solve()