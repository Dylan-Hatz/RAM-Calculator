import copy
import EasyIterate as EasyIter

#Changing the function into a python understandable version(This part actually happnes later in the code)
def FuncFix():
    FuncList=[]
    for letter in EasyIter.iter(Function):
        FuncList.append(Function[letter])
    for item in EasyIter.iter(FuncList):
        if FuncList[item]=='^':FuncList[item]='**';continue
        if FuncList[item]=='[':FuncList[item]='(';continue
        if FuncList[item]==']':FuncList[item]=')';continue
        if FuncList[item]=='x':
            if FuncList[item-1].isnumeric(): FuncList[item]='*'+copy.deepcopy(FuncList[item])
            elif FuncList[item+1].isnumeric(): FuncList[item]=copy.deepcopy(FuncList[item])+'*'
            continue
    return ''.join(FuncList)

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