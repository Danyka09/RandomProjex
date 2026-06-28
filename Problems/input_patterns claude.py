
# ═══════════════════════════════════════════════════════════════
#  PATTERN 1 — Single value
#  Input looks like:
#    5
# ═══════════════════════════════════════════════════════════════
import sys
input = sys.stdin.readline

n = int(input())


# ═══════════════════════════════════════════════════════════════
#  PATTERN 2 — Multiple values on one line
#  Input looks like:
#    3 7
# ═══════════════════════════════════════════════════════════════
import sys
input = sys.stdin.readline

a, b = map(int, input().split())


# ═══════════════════════════════════════════════════════════════
#  PATTERN 3 — A list of numbers on one line
#  Input looks like:
#    1 4 2 8 5 7
# ═══════════════════════════════════════════════════════════════
import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))


# ═══════════════════════════════════════════════════════════════
#  PATTERN 4 — n, then n lines of single values
#  Input looks like:
#    4
#    3
#    1
#    7
#    2
# ═══════════════════════════════════════════════════════════════
import sys
input = sys.stdin.readline

n = int(input())
values = [int(input()) for _ in range(n)]


# ═══════════════════════════════════════════════════════════════
#  PATTERN 5 — n, then n lines of multiple values
#  Input looks like:
#    3
#    4 7
#    2 9
#    1 3
# ═══════════════════════════════════════════════════════════════
import sys
input = sys.stdin.readline

n = int(input())
pairs = [list(map(int, input().split())) for _ in range(n)]


# ═══════════════════════════════════════════════════════════════
#  PATTERN 6 — n, then n lines of strings (words)
#  Input looks like:
#    3
#    word
#    localization
#    internationalization
# ═══════════════════════════════════════════════════════════════
import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]  # .strip() removes the trailing newline


# ═══════════════════════════════════════════════════════════════
#  PATTERN 7 — No n given, read until EOF
#  Input looks like:
#    word
#    localization
#    internationalization
#    (just stops, no empty line)
# ═══════════════════════════════════════════════════════════════
import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

# or as a one-liner:
lines = [line.strip() for line in sys.stdin]


# ═══════════════════════════════════════════════════════════════
#  PATTERN 8 — Read everything at once, index into it
#  Useful when the structure is messy or you're not sure
#  Works for any input shape
# ═══════════════════════════════════════════════════════════════
import sys

data = sys.stdin.read().split()  # one flat list of every token
idx = 0

n = int(data[idx]); idx += 1
a = int(data[idx]); idx += 1
b = int(data[idx]); idx += 1
