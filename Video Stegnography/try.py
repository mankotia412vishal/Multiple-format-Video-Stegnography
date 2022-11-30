import cv2
# a=cv2.imread('./data.jpeg')
a=cv2.imread('./car.jpeg')
# a=cv2.resize(a,(500,500))
print(a.shape)

cv2.imshow("dd",a)
cv2.waitKey(0)

# cap=cv2.VideoCapture('./hid2.gif')
# length = int(cap. get(cv2. CAP_PROP_FRAME_COUNT))
# print(length)
# while(cap. isOpened()):
#     ret, frame = cap. read()
#     if ret == True:
#         # frame = cv2. resize(frame, (500, 500))
#         cv2. imshow('frame',frame)
#         # count+=1
#         print(frame.shape)
#         if cv2. waitKey(10) & 0xFF == ord('q'):
#             break
#     else:
#         break