import pprint
ticTakBoard={'Top-L':'X', 'Top-M':' ','Top-R':'O','Mid-L':' ','Mid-M':' ','Mid-R':'X','Low-L':' ','Low-M':'O','Low-R':' '}
pprint.pprint(ticTakBoard)
def printBoard(Board):
    print(Board['Top-L'] + ' | ' + Board['Top-M'] + ' | ' + Board['Top-R'])
    print('---------')
    print(Board['Mid-L'] + ' | ' + Board['Mid-M'] + ' | ' + Board['Mid-R'])
    print('---------')
    print(Board['Low-L'] + ' | ' + Board['Low-M'] + ' | ' + Board['Low-R'])

print(printBoard(ticTakBoard))