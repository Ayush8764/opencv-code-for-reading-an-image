import cv2

img = cv2.imread('quote.jpg')
x = 100
y = 200
cv2.rectangle(img,(x,y),(x+100,y+100),(255,255,255),-5)

while True:
    cv2.imshow('Quote Image',img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()


