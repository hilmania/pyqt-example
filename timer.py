from PyQt6 import QtCore

class Thread(QtCore.QThread):
    def stop(self):
        self._stopped = True
        print('STOPPING LOOP')

    def run(self):
        self._stopped = False
        counter = 0
        while not self._stopped:
            counter +=1
            print(counter)
            self.msleep(100)

app = QtCore.QCoreApplication(['Test'])

thread = Thread()
thread.finished.connect(app.quit)
QtCore.QTimer.singleShot(2000, thread.stop)
thread.start()

app.exec()
