import matplotlib.pyplot as plt
import numpy as np
import time

# 初始小组分数
group_names = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
group_scores = [10, 20, 30, 40, 50]  # 假设初始分数

# 绘制初始柱状图
def draw_barchart(scores):
    plt.figure(figsize=(10, 6))
    plt.bar(group_names, scores, color='blue')

    for i in range(len(scores)):
        plt.text(i, scores[i] + 1, str(scores[i]), ha='center')  # 在每个柱状上显示分数

    plt.ylim(0, max(scores) + 20)  # 设置Y轴上限
    plt.title("Group Scores")
    plt.xlabel("Groups")
    plt.ylabel("Scores")
    
    plt.show()

# 增加分数并重新绘制图形
def update_score(group_index, score_increment):
    global group_scores
    group_scores[group_index] += score_increment

    draw_barchart(group_scores)

# 初始绘制
draw_barchart(group_scores)

# 测试添加分数到1号小组
time.sleep(2)  # 暂停以模拟动画效果
update_score(0, 10)  # 给1号小组增加10分

