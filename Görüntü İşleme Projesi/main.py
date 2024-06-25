import cv2
import numpy as np

backsub = cv2.createBackgroundSubtractorKNN()
##backsub = cv2.createBackgroundSubtractorMOG2(detectShadows=False)



capture = cv2.VideoCapture("video1.mp4")

sayac=0
sol = 0
sag = 0

if capture:
  while True:
    ret, frame = capture.read()
    if ret:
        fgmask = backsub.apply(frame, None, 0.01)
        #cv2.line(frame, (0, 350), (1555, 350), (0, 255, 0), 2)
        #cv2.line(frame, (0, 360), (1555, 360), (0, 255, 0), 2)
        #cv2.line(frame, (430, 50), (430, 500), (0, 255, 0), 2)

        contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        try: hierarchy = hierarchy[0]
        except: hierarchy = []
        for contour, hier in zip(contours, hierarchy):

            (x,y,w,h) = cv2.boundingRect(contour)

            if w > 40 and h > 40:
                print("W: " + str(w) + "  H: " + str(h))
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                if y>350 and y<360:
                    if x+w<430:
                        sol+=1
                    else:
                        sag+=1
                    sayac+=1

        cv2.putText(frame,"Toplam : "+str(sayac), (390, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        cv2.putText(frame, "Sag : " + str(sag), (650, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        cv2.putText(frame, "Sol : " + str(sol), (150, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

        cv2.imshow("Takip", frame)
        cv2.imshow("Arka Plan Cikar", fgmask)

    key = cv2.waitKey(60)
    if key == ord('q'):
            break
capture.release()
cv2.destroyAllWindows()