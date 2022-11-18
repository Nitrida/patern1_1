import threading
import time


class Download_Class(threading.Thread):

    def run(self):
        print('Загрузка ')
        for i in range(1, 6):
            self.i = i
            time.sleep(2)

        return 'какойто текст'


class Work_Class(threading.Thread):
    def run(self):
        for i in range(1, 6):
            print('Working_Class загрузка класса: %i(%i)' % (i, dow.i))
            time.sleep(1)
            dow.join()

        print('Выполнено')


dow = Download_Class()
dow.start()

time.sleep(1)

wor = Work_Class()
wor.start()

wor1 = Work_Class()
wor1.start()

t3 = Work_Class()
t3.start()