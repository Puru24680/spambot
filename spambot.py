import pyautogui, time
time.sleep(7)
f = open("beemovie", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

