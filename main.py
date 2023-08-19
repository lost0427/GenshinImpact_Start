import cv2
from screeninfo import get_monitors
import keyboard
import time
from threading import Thread
from moviepy.editor import VideoFileClip
import numpy as np
from playsound import playsound
from PIL import ImageGrab

video_path = './1/1.mp4'
video_clip = VideoFileClip(video_path)
cap = cv2.VideoCapture(video_path)


def task2():
    cv2.namedWindow('FullScreen', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('FullScreen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('FullScreen', frame)

        if cv2.waitKey(1) & 0xFF == 27:  # 按下ESC键退出
            break

    cap.release()
    cv2.destroyAllWindows()


def task1():
    playsound('./1/1.mp3')


while True:

    monitors = get_monitors()
    if monitors:
        screen_width = monitors[0].width
        screen_height = monitors[0].height

    print('正在检测屏幕...')
    screenshot = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))), cv2.COLOR_BGR2RGB)

    white_pixels = np.count_nonzero(screenshot == [255, 255, 255])
    total_pixels = screenshot.shape[0] * screenshot.shape[1]
    white_percentage = white_pixels / total_pixels * 100

    if white_percentage >= 90:
        try:
            print('原神 启动!')
            t1 = Thread(target=task1)
            t1.start()
            print('111')
            keyboard.press_and_release('win + m')
            t2 = Thread(target=task2)
            t2.start()
            print('222')
            time.sleep(2)

            break

        except:
            print('擦那，出错了')
            break