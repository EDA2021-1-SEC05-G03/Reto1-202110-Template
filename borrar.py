from statistics import mode
x = [{"id": "opmmmmmpp"}, {"id": "p"}, {"id": "o"}, {"id": "d"}, {"id": "h"}, {"id": "l"}, {"id": "m"}, {"id": "s"}]
for i in x:
  print(mode(i["id"]))