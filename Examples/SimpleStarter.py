from microbit import *
import bitbotXL as bot

go = False

while True:
    if go == True:
        bot.move_forward(50, 500)
        bot.turn_left(50, 500)
    
    distance = bot.get_distance()
    display.scroll(distance)

    if button_a.was_pressed():
            if go == True:
                go = False
            else:
                go = True
    sleep(200)