import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [2,4,9,16,25]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c='red', s=100)

# 设置图表标题并给坐标轴加上标签
ax.set_title("Sequares", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("Value's Sequare", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()

# 第一个实参指定要以什么文件名保存图表，这个文件将存储到scatter_squares.py所在的目录。
# 第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，只需省略这个实参即可。
plt.savefig('scatter_chat.png', bbox_inches='tight')