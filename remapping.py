WIDTH = 100
HEIGHT = 50

TARGET_WIDTH = 10
TARGET_HEIGHT = 5

w_ratio = WIDTH // TARGET_WIDTH # 10
h_ratio = HEIGHT // TARGET_HEIGHT # 10

# def populate(i,j):



mapped_grid = [[populate(i,j) for j in range(TARGET_WIDTH)] for i in range(TARGET_HEIGHT)]