import pyfakewebcam
import numpy as np
import time
import timeit
import cv2


from tkinter import *
import time

from PIL import Image

class MyLoop():
    def __init__(self, root):
        self.running = True
        self.aboutToQuit = False
        self.root = root
        self.count = 0
        self.r_count = 0
        self.inter = 1
        self.root.bind("<space>", self.switch)
        self.root.bind("<Escape>", self.exit) 
        self.root.bind("<s>",self.store)
        self.root.bind("<d>",self.replay)
        self.root.bind("<x>",self.lag)

        self.frame_store = []
        self.store = False
        self.replay = False
        self.lag_flag = False
        
        while not self.aboutToQuit:
            self.root.update() # always process new events
			#Changes  1 2 3
            self.inter = (self.inter % 3) + 1
            if( (self.running and not(self.lag_flag)) or (self.inter % 3 == 0 and self.running)):
                #Do Loop
                #if self.lag_flag:
                #time.sleep(1/6)
                ret, frame = vid.read()
                #Converted to PIL image
                im0 = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                im0 = np.array(im0)
                #im0 = cv2.resize(im0, (640, 480)) 
                cam.schedule_frame(im0)
                self.img = im0
                #Video store
                if self.store:
                  #print("S",end = "")
                  self.count += 1
                  #print(self.count)
                  self.frame_store.append(im0)
                  if(self.count % 1000 == 0):
                     print(self.count)
                  if(self.count >6000):
                     print("Storing Stops exceeded limit")
                     self.store = not(self.store)
                #time.sleep(.1)

            else : # If paused
                #time.sleep(.1)
                time.sleep(1/7)
                #Replay Stored frame
                if self.replay and not(self.store):
                   #vid.release()
                   if(self.count > 0):
                      im0 =  self.frame_store[self.r_count]
                      if self.r_count == self.count -1:
                         for i in range(20):
                             cam.schedule_frame(im0)
                             time.sleep(1/8)
                      cam.schedule_frame(im0)
                      self.r_count = (self.r_count + 1) % self.count
                   else:
                      print("Replay Stops")
                      self.replay = not(self.replay)
                   

    def switch(self, event):
        if not(self.replay):
           print(['Unpaused','Paused'][self.running])
           self.running = not(self.running)

    def exit(self, event):
        vid.release()
        print("Exiting")
        self.aboutToQuit = True
        self.root.destroy()
    def store(self,event):
        print(['Storing','Storing Stops'][self.store])
        if not(self.store):
           self.frame_store = []
           self.count = 0
           self.r_count = 0
        print(self.count)
        self.store = not(self.store)
    def replay(self,event):
        ret, frame = vid.read()
        self.running = False
        print(['Replay Start','Replay Stops'][self.replay])
        print(self.r_count,end= ":  ")
        print(self.count)
        self.replay = not(self.replay)
        #print("paused")
        self.lag_flag = True
        #vid = cv2.VideoCapture(0)
        #cam = pyfakewebcam.FakeWebcam('/dev/video7', 640, 480)
    def lag(self,event):
        print(['Lag on','Lag off'][self.lag_flag])
        self.lag_flag = not(self.lag_flag)

#im1 for black screen        
#im1 = np.zeros((480,640,3), dtype=np.uint8)
cam = pyfakewebcam.FakeWebcam('/dev/video2', 640, 480)
#cam = pyfakewebcam.FakeWebcam('/dev/video7', 1280, 720)
cam.print_capabilities()
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_BUFFERSIZE, 1)


root = Tk()
MyLoop(root)
root.mainloop()



