S = input()

counter = 0

for i in range(len(S)):

  # Aを見つけた場合
  if S[i] == 'A':

    # 
    for j in range(i + 1, len(S) - i):

      if S[j] == 'B':

        if j + (j - i) > len(S) - 1:

          break

        if S[j + (j - i)] == 'C':

          counter += 1

print(counter)
