import time,webbrowser, pyautogui
def webbrowsing():
    url="https://www.google.com/"
    webbrowser.open(url)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'w')