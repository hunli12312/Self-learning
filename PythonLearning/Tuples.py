import matplotlib.pyplot as plt
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_numbers.sort()
friends2 = friends.copy()
lucky_numbers.reverse()
lucky_numbers.pop()
print(friends2)
print(lucky_numbers)

coordinates = [(4,5),(1,1), (9,9)]#can not change, x axis
coordinates2 = [(1,1),(3,1),(5,2)]#y axis
#two line, one line is (4,1) (1,3) (9,5)
#one lien is (5,1) (1,1) (9,2)
plt.plot(coordinates,coordinates2)
plt.show()
print(coordinates)
