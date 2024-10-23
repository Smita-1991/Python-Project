import webbrowser,sys

address=''
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    
print(address)

webLink='https://www.google.com/maps/place/'+str(address)
print("address is:",webLink)
    
webbrowser.open('https://www.google.com/maps/place/'+str(address))
print(sys.argv)