numbers = list(range(1, 101))

result = [n for n in numbers if n % 5 == 0]

print(result)

x = [[0 for _ in range(4)] for _ in range(5)]

print(x)

number = [4]

for value in range(5):

    for number in range(4):
     print(number)

x = []
n = [0] * 4

for _ in range (5):
    x.append(n)

    print(x)

score = (1, 2, 3, "jabson")
print(type(score))

scores = (1, 2, 3, "ola")
single_tuple = (1,)

scores = list(scores)
scores[3] = "Jay"
scores = tuple(scores)

print(scores.count(2))
print(scores)

list = [1, 2, 3, 5, "Samson", 8.7, "Ola"]

list[3] = 4
list[4] = "Tayo"

print(list)

print(f"[{'jabson': 20}]")
print((f"[{2.5: 20.2f}] {'jabson': 20}"))

tuple2 = (1, 2, 3, [2, 4, 6], "Bolu", "9.5")

tuple2[3][2] = 10
tuple2[3].append(5)
tuple2[3].extend([6, 7, 9])

print(tuple2)

numbers = [1, 2, 3, 4, 5]
print(6 not in numbers)
print(6 in range(len(numbers)))