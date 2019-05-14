# primes = [1, 4, 5, 8, 67, 546, 87]
#
# print(len(primes))
#
# for index in range(len(primes)):
#     print(primes[index])
#
# for p in primes:
#     print(p)

# n = 5
# values = [None] * 5
# values2 = [0] * 5
# print(values)
#
# values3 = [z for z in range(9)]
# print(values3)
#
# values4 = [z + 1 for z in range(9)]
# print(values4)

# values5 = [int(z) for z in input().split()]
# print(values5)

values6 = [1, 4, 5, 8, 67, 546, 87]
print(values6[5:1:-1])
print(4 in values6)
print(4555 not in values6)
values6 += [123, 456]
print(sorted(values6))
print(values6)
values6.sort()
print(values6)
