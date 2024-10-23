import traceback

# ************
# *          *
# *          *
# *          *
# ************

def printBox(symbol,width,height):
    if(len(symbol)!=1):
        try:
            raise Exception('Symbol need to be 1')
        except:
            errorFile=open('C:\\Users\\kanaw\\Downloads\\qwe\\abc.txt','a')
            errorFile.write(traceback.format_exc())
            errorFile.close()
    if(width<2 & height<2):
        try:
            raise Exception("width and height should greater or equal to 2")
        except:
            errorFile=open('C:\\Users\\kanaw\\Downloads\\qwe\\abc.txt','a')
            errorFile.write(traceback.format_exc())
            errorFile.close()
    print(symbol*width)
    
    for i in range(height-2):
        print(symbol+(' '*(width-2))+symbol)
    
    print(symbol*width)

printBox("*",15,5)