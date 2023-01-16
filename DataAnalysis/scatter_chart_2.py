import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置图表标题并给坐标轴加上标签
ax.set_title("Sequares", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("Value's Sequare", fontsize=14)


# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

plt.show()