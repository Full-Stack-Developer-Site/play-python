import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')

# subplots()函数可以在一张图片中绘制一个或多个图表
# fig表示整张图片，ax表示图片中的各个图表
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签1
ax.set_title("Squares", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value's Square", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)


# 打开Matplotlib查看器并显示绘制的图表
plt.show()