import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# plt.plot(x,y)
# plt.show()
# x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# y = [5, 7, 8, 6, 4]
# plt.title('Weekly sales')
# plt.xlabel('Days of the week')
# plt.ylabel('Number of sales')
# plt.plot(x, y, marker='o', color='b', linestyle='-')
# plt.show()

x = ['A', 'B', 'C', 'D', 'E']
y = [5, 7, 8, 6, 4]
plt.title('Product Sales')
plt.xlabel('Products')
plt.ylabel('Number of Sales')
plt.bar(x, y, color='blue')
plt.show()