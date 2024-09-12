import os
import cv2



pathOut =  '/Users/erickmunz/Documents/DEV/python/OCR/video/out/'
count = 0
counter = 1
dirtolist = '/Users/erickmunz/Documents/VIDEO/'
listing = os.listdir(dirtolist)

vids = [i for i in listing if i.endswith('mp4')]
for vid in vids:
    vid = dirtolist+vid
    cap = cv2.VideoCapture(vid)
    count = 0
    counter += 1
    success = True
    while success:
        success,image = cap.read()
        print('read a new frame:',success)
        if count%1000 == 0 :
             cv2.imwrite(pathOut + 'frame%d.jpg'%count,image)
        count+=1