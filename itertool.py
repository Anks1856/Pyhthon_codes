import itertools

List = [[1, 2], [5, 6], [7, 8]]

ans = list(itertools.chain.from_iterable(List))
print(ans)