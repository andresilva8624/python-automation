import pyautogui
import time

# Steps for the automation proccess

# Step 1 - Enter the company's website: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pyautogui.write -> Writes a text
# pyautogui.click -> Clicks somewhere in the screen with your cursor location
# pyautogui.press -> Presses 1 key only
# pyautogui.hotkey -> Presses a combination of keys

pyautogui.PAUSE = 0.4

# Open browser
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Enter link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)

# Step 2 - Login

# Select the email bar
pyautogui.click(x=663, y=511)
# Write your email
pyautogui.write("andresilva@email.com")
# Go to the next bar
pyautogui.press("tab")
# Write your password
pyautogui.write("password")
# Go to the next bar
pyautogui.press("tab")
# Enter with the login button
pyautogui.press("enter")

time.sleep(1)

# Step 3 - Import and register the product database

import pandas

table = pandas.read_csv("products.csv")

print(table)

# Step 4 - Register product

# For loop to go through every row in table
for row in table.index:
    # Click on the code bar
    pyautogui.click(x=658, y=362)
    # Get the value code that we want to fill
    code = table.loc[row, "codigo"]
    # Fill the bar
    pyautogui.write(str(code))
    # Go to the next bar
    pyautogui.press("tab")
    # Fill the remaining info
    pyautogui.write(str(table.loc[row, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[row, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[row, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[row, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[row, "custo"]))
    pyautogui.press("tab")
    obs = table.loc[row, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(table.loc[row, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Scroll up to top of the page
    pyautogui.scroll(5000)

    # Step 5 - For loop to repeat the registration for all the products

