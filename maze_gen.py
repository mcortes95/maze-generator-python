from PIL import Image, ImageDraw


def gen_blank_maze(width,height):
    buff=Image.new("RGB",(width,height))
    drawing=ImageDraw.Draw(buff)
    drawing.point([0,1],(255,255,255))
    drawing.point([width-1,height-2],(255,255,255))
    buff.resize((width*8,height*8)).show()
    buff.close()
    return buff

def dfs_gen(img):
    walls_list=[]
    walls_list.append([0,1])
    print(get_walls(img,walls_list[0])) 


    #return ")"

def get_walls(maze,cell):
    walls=[]
    walls.append([cell[0]+1,cell[1]])
    walls.append([cell[0]-1,cell[1]])
    walls.append([cell[0],cell[1]+1])
    walls.append([cell[0],cell[1]-1])

    return walls


new_img=gen_blank_maze(125,100)
dfs_gen(new_img)
