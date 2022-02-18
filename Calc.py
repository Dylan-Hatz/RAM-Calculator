import copy
import math

#Changing the function into a python understandable version(This part actually happnes later in the code)
def FuncFix():
    FuncList=[]
    for letter in range(len(Function)): FuncList.append(Function[letter])
    for item in range(len(FuncList)):
        if FuncList[item]=='^': FuncList[item]='**';continue
        if FuncList[item]=='[': FuncList[item]='(';continue
        if FuncList[item]==']': FuncList[item]=')';continue
        if FuncList[item].lower() == 'p': FuncList[item]=='math.pi'; FuncList[item].pop(item+1)
        if FuncList[item].lower()=='s':
            FuncList[item]='math.sqrt'
            if FuncList[item+1].lower()=='q':FuncList.pop(item+1);FuncList.pop(item+2);FuncList.pop(item+3)
            if FuncList[item-1] in ['x','math.pi'] or FuncList[item-1].isnumeric():FuncList[item]='*'+FuncList[item]
        if FuncList[item].lower() in ['x','math.pi']:
            if item != 0:
                if FuncList[item-1].isnumeric() or FuncList[item-1] in ['x','math.pi']: FuncList[item]='*'+copy.deepcopy(FuncList[item])
            if item != len(FuncList)-1:
                if FuncList[item+1].isnumeric() or FuncList[item-1] in ['x','math.pi']: FuncList[item]=copy.deepcopy(FuncList[item])+'*'
            continue
    return ''.join(FuncList)

while True:
    #Setting up Choices
    Function=input('Function: ')
    Divisions=int(input('Divisions: '))
    Start=float(input('Start: '))
    End=float(input('End: '))
    Interval=(End-Start)/Divisions
    Points,Midpoints=[],[]
    #Where the actual function fixing happens
    FixedFunction=FuncFix()
    #Finding the value the points of all of the dividing lines and the midpoints of the function and multiplying the height of the rectangles by their width
    for point in range(Divisions+1):
        x=Start+(Interval*point)
        Points.append(eval(FixedFunction)*Interval)
        x=x+(Interval/2)
        Midpoints.append(eval(FixedFunction)*Interval)
    #Adding the widths of the appropriate rectangles and displays them
    print('MRAM: '+str(sum([Midpoints[i] for i in range(Divisions)])))
    print('LRAM: '+str(sum([Points[i] for i in range(Divisions)])))
    print('RRAM: '+str(sum([Points[i+1] for i in range(Divisions)])))
    input('Press Enter to continue...')