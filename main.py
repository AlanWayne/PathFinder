import math
import pygame as pg
import random

scr_width = 640
scr_height = 640

screen = pg.display.set_mode((scr_width, scr_height))
run = True

def dist(ax,ay,bx,by):
    a = math.fabs(bx - ax)
    b = math.fabs(by - ay)
    return math.sqrt(a * a + b * b)

width = 25
height = 25

spr_size = scr_width / width

grid = [[0] * width for i in range(height)]

start_x = 0
start_y = 0
end_x = width - 1
end_y = height - 1

if start_x < end_x:
    step_x = 1
else:
    step_x = -1
    
if start_y < end_y:
    step_y = 1
else:
    step_y = -1

for i in range(start_x, end_x + step_x, step_x):
    for j in range(start_y, end_y + step_y, step_y):
        grid[i][j] += max(math.fabs(i - start_x), math.fabs(j - start_y))

for i in range(start_x, end_x + step_x, step_x):
    for j in range(start_y, end_y + step_y, step_y):
        grid[i][j] += round(dist(i,j,end_x,end_y),1)
    
for i in range(width):
    for j in range(height):
        if random.randint(1,100) < 40 and i != start_x and i != end_x and j != start_y and j != end_y:
            grid[i][j] = 1000
    
route = []
sx = start_x
sy = start_y

trys = 0

while sx != end_x and sy != end_y and trys < 100000:
    trys += 1
#for k in range(500):
    check_x = []
    check_y = []
    
    if sx < width - 1:
        check_x.append(sx+1)
        check_y.append(sy)
    if sx > 0:
        check_x.append(sx-1)
        check_y.append(sy)
    if sy < height - 1:
        check_x.append(sx)
        check_y.append(sy+1)
    if sy > 0:
        check_x.append(sx)
        check_y.append(sy-1)
    if sx < width - 1 and sy < height - 1:
        check_x.append(sx+1)
        check_y.append(sy+1)
    if sx > 0 and sy < height - 1:
        check_x.append(sx-1)
        check_y.append(sy+1)
    if sx < width - 1 and sy > 0:
        check_x.append(sx+1)
        check_y.append(sy-1)
    if sx > 0 and sy > 0:
        check_x.append(sx-1)
        check_y.append(sy-1)
    
    c = 0
    weight = 1000
    for i in range(len(check_x)):
        if grid[check_x[i]][check_y[i]] < weight:
            weight = grid[check_x[i]][check_y[i]]
            c = i
            
    pg.draw.line(screen,(255,255,255),(spr_size / 2 + spr_size*sx,spr_size / 2 + spr_size*sy),(spr_size / 2 + spr_size*check_x[c],spr_size / 2 + spr_size*check_y[c]),2)
    grid[sx][sy] = 888
    sx = check_x[c]
    sy = check_y[c]
    
    for i in range(width):
        for j in range(height):
            if grid[i][j] > 100 and grid[i][j] < 900:
                grid[i][j] -= 1
    
    
        
    
for p in range(width):
    print(grid[p])
    
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for i in range(width):
        for j in range(height):
            if (i == start_x and j == start_y):
                pg.draw.circle(screen,(50,50,200),(spr_size / 2 + i * spr_size, spr_size / 2 + j * spr_size), spr_size * 0.20)
            elif (i == end_x and j == end_y):
                pg.draw.circle(screen,(200,50,50),(spr_size / 2 + i * spr_size, spr_size / 2 + j * spr_size), spr_size * 0.20)
            elif (grid[i][j] > 999):
                pg.draw.circle(screen,(200,200,200),(spr_size / 2 + i * spr_size, spr_size / 2 + j * spr_size), spr_size * 0.50)
            else:
                pg.draw.circle(screen,(0,0,0),(spr_size / 2 + i * spr_size, spr_size / 2 + j * spr_size), spr_size * 0.20)
            
    pg.display.flip()
    
    # check out