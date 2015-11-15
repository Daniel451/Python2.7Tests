import cv2
import os


class Recorder:
    def __init__(self, camera=0, counter=0, naming_prefix="cam_record", fdir="img/", width=800, height=600):
        # capture camera input
        self.cap = cv2.VideoCapture(camera)
        self.cap.set(3, width)
        self.cap.set(4, height)

        # capture size

        # counter and file/path settings
        self.counter = counter
        self.naming_prefix = naming_prefix
        self.fdir = fdir

        # check the directory
        self.__check_directory_existance()

        # start capturing
        self.__loop()


    def __loop(self):
        while True:
            # capture each frame
            ret, frame = self.cap.read()

            # frame operations
            frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # display frames
            cv2.imshow("frame (original)", frame)
            cv2.imshow("frame (grey)", frame_grey)

            # listen to user input
            k = cv2.waitKey(1)  # 0 will wait for user input before recording a new frame

            # react to user input
            if k == ord('q'):
                break
            elif k == ord('s'):  # record frame on pressing "s"
                cv2.imwrite(self.__get_current_filename() + ".png", frame)
                cv2.imwrite(self.__get_current_filename() + "_grey.png", frame_grey)
                self.__increase_counter()


    def __get_current_filename(self):
        return self.fdir + self.naming_prefix + "_" + format(self.counter, "07,").replace(",", ".")


    def __increase_counter(self):
        self.counter += 1


    def __check_directory_existance(self):
        if not os.path.exists(self.fdir):
            os.makedirs(self.fdir)


    def __end_program(self):
        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()

