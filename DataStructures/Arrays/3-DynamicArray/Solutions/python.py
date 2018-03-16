N, nQueries = input().strip().split(' ')
queries = []
for x in range(int(nQueries)):
  arr = list(map(int, input().strip().split(' ')))
  queries.append(arr)
        
def calculate(N, nQueries, queries):
  seqList = [[] for _ in range(N)]
  lastAnswer = 0


  for c in range(int(nQueries)):
    currentQuery = queries[c]
    Q = currentQuery[0]
    x = currentQuery[1]
    y = currentQuery[2]
        
    if Q == 1:
      seq = ((x ^ lastAnswer)%N)

      seqList[seq].append(y)
      
    if Q == 2:
      seq = ((x^lastAnswer)%N)
      element = (y%len(seqList[seq]))
      lastAnswer = seqList[seq][element]
      print(lastAnswer)

calculate(int(N), int(nQueries),queries)
