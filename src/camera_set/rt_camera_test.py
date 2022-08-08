from readline import read_init_file
import cv2

DEVICE_ID = 0
IMG_WIDTH = 480
IMG_HEIGHT = 320

def camera_test():
    try:
        rt_img = cv2.VideoCapture(DEVICE_ID)
        rt_img.set(3, IMG_WIDTH)
        rt_img.set(4, IMG_HEIGHT)

        while True:
            # read frames form camera
            _, frame = rt_img.read()

            cv2.imshow('frame',frame)
            if cv2.waitKey(33) == 27:
                break
    except Exception as e:
        print("exit")
    finally:
        cv2.destroyAllWindows()
        rt_img.release()

if __name__ == '__main__':
    camera_test()