import pyautogui

pyautogui.click(600,500)
pyautogui.typewrite('Hello world',interval=0.2)
print(pyautogui.position())

pyautogui.typewrite(['a','b','left','left','X','Y'],interval=1)

print(pyautogui.KEYBOARD_KEYS)
pyautogui.screenshot('c:\\Users\\kanaw\\OneDrive\\Desktop\\Smita\\Python\\Python-Project\\screenshotExample.png')