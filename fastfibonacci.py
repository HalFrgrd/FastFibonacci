
cache = {0:0, 1:1}
def f(n):
	try:
		return cache[n]
	except KeyError:
		cache[n] = f(n-1) + f(n-2)
		return cache[n]

print(f(99))