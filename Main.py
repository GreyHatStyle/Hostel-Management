import baseGUI
import TeleBot
import multiprocessing

p1 = multiprocessing.Process(target=baseGUI.head_gui)
p2 = multiprocessing.Process(target=TeleBot.main)

if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()

print("done")
