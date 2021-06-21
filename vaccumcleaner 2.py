floor=[[1,0,0,0],
       [0,1,0,1],
       [1,0,1,1]]
def clean(floor):
    m=len(floor[0])
    n=len(floor)
    no_of_tiles=m*n
    
    tiles_checked=0
    
    row=0
    col=0
    while tiles_checked<no_of_tiles:
        print_floor(floor,row,col)
        if floor[row][col]==1:
            floor[row][col]=0
            print('sucked the dirt')
        else:
            print('already clean')
            
        if row % 2==0:
            if col<m-1:
                col+=1
                else:
                row+=1
        elif row % 2==1:
            if 0<col:
                col-=1
            else:
                row +=1
        tiles_checked +=1
        print('-------')
        print('cleaned!!!')
    def print_floor(floor,row,col):
        temp=floor[row][col]
        floor[row][col] = 'VC'
        for x in floor:
            pringt(x)
        floor[row][col] = temp
        clean(floor)
