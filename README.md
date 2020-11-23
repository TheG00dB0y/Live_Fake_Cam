# Live_Fake_Cam
A user interactive live cam manipulating based on Tkinter and pyfakecam API in linux. The user can currently store video frames, replay the saved frames, add lag to the video output , add stuck ,add black screen. The code can be further improved based on the requirements. 

## installation

```
# use git to install the latest version
git clone https://github.com/TheG00dB0y/Live_Fake_Cam

pip install numpy opencv-python pillow
apt-get install v4l2loopback-utils
apt-get install ffmpeg # useful for debugging

#Creating virtual cam with custom camera label and device number
sudo modprobe v4l2loopback video_ncr=<Number> card_label="<label Name>"
```
## v4l2loopback usefull commands


```
#Show all video devices
ls -ltrh /dev/video*

#Removing the real cam for debugging
modprobe -r uvcvideo
#Adding back the real cam to devices
modprobe uvcvideo

#Adding virtual cams (Fake cam) as devices
modprobe v4l2loopback devices=1
#removing all fake cams
modprobe -r v4l2loopback

#Creating virtual cam with custom camera label and device number
sudo modprobe v4l2loopback video_ncr=<Number> card_label="<label Name>"

```
