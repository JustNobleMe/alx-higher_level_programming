# s1 = "Best"
# s2 = s1
# print(s1 is s2)

# l1 = [1, 2, 3]
# l2 = l1
# print(l1 is l2)

# l1 = [1, 2, 3]
# l2 = l1
# l1 = l1 + [4]
# print(l1)

# def increment(n):
#     n += 1
#     return n

# a = 1

# print(increment(a))

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)