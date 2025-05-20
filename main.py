import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep

#working of webcam
cap=cv2.VideoCapture(0)
cap.set(3, 1280)  #width and hd resolution
cap.set(4 ,720) #height and video resolution

detector=HandDetector(detectionCon=0.8)
keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
]
finalText=""

def draw(img,buttonList, activeButton=None ,clickedButton=None):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size

        if button == clickedButton:
            color = (0, 0, 0)  # Black for clicked
        elif button == activeButton:
            color = (200, 200, 200)  # Light Gray for active
        else:
            color = (100, 100, 100)  # Dark Gray for inactive
        cv2.rectangle(img, button.pos, (x + w, y + h),color, cv2.FILLED)  # Rectangular button-for the keys
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),
                    3)  # PUT TEXT INSIDE TEH RECTANGLE

    return img

class Button():
    def __init__(self,pos,text,size=[85,85]):
        self.pos=pos
        self.text=text
        self.size=size




# myButton=Button([100,100],"Q")   can use list instead of individual printing
buttonList=[]

for i in range(len(keys)):
    for x, key in enumerate(keys[i]):
        buttonList.append(Button([100 * x + 50, 100 * i + 50], key))



while True:
    success,img=cap.read()
    img = cv2.flip(img, 1)
    # img=detector.findHands(img)

    hands, img = detector.findHands(img)    #to capture hands


    #Create class for buttons for better use!
    #
    # cv2.rectangle(img,(100,100),(200,200),(255,0,255),cv2.FILLED)    #Rectangular button-for the keys
    # cv2.putText(img,"Q",(120,185),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),4) #PUT TEXT INSIDE THE RECTANGLE
    #
    activeButton = None
    clickedButton = None

    if hands:
        for hand in hands:
            lmList = hand['lmList']
            if lmList:
                # Check for distance between index (8) and middle (12) fingers
                length, _, _ = detector.findDistance(lmList[8][0:2], lmList[12][0:2], img)
                # print(length) # added to help with adjusting threshold

                index_finger_tip = lmList[8]

                for button in buttonList:
                    x, y = button.pos
                    w, h = button.size

                    if (x < index_finger_tip[0] < x + w and y < index_finger_tip[1] < y + h):
                        activeButton = button

                        if length < 20:  # Adjust threshold as needed
                            clickedButton = button # Mark this button as clicked
                            finalText+=button.text
                            sleep(0.15)


            cv2.rectangle(img, (50,350), (700,450), (175,0,175), cv2.FILLED)  # Rectangular button-for the keys
            cv2.putText(img,finalText, (60,430), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)  # PUT TEXT INSIDE TEH RECTANGLE

    #USE THIS IS CVZONE-OLDER VERSION IS USED(1.4.1)
    # if lmList:
    #     for  button in buttonList:
    #         x,y=button.pos
    #         w,h=button.size
    #
    #
    #         if( x<lmList[8][0]<x+w  and y<lmList[8][1]<y+h):
    #             cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255),
    #                           cv2.FILLED)  # Rectangular button-for the keys
    #             cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),
    #                         3)  # PUT TEXT INSIDE TEH RECTANGLE


    img=draw(img, buttonList, activeButton,clickedButton)



    cv2.imshow("Image",img)
    cv2.waitKey(1)
