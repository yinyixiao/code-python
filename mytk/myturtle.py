# 导入turtle包的所有内容:
import turtle

# 设置笔刷宽度:
turtle.width(4)

# 前进:
turtle.forward(200)
# 右转90度:
turtle.right(90)

# 笔刷颜色:
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)

turtle.pencolor('green')
turtle.forward(200)
turtle.right(90)

turtle.pencolor('blue')
turtle.forward(100)
turtle.right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()