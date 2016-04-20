import cv2
#import cv2.cv as cv
from time import time
boxes = []
start_x_pos,start_y_pos=-1,-1
end_x_pos,end_y_pos=-1,-1
def on_mouse(event, x, y, flags, params):
    # global img
    global start_x_pos,start_y_pos,end_x_pos,end_y_pos
    t = time()
    #start_x_pos=0
    #start_y_pos=0
    if event == cv2.EVENT_LBUTTONDOWN:
         #print 'Start Mouse Position: '+str(x)+', '+str(y)
         start_x_pos=x
         start_y_pos=y
         print('Start Mouse Position: '+str(x)+', '+str(y))
         print('Start Pos Down: '+str(start_x_pos)+', '+str(start_y_pos))
         sbox = [x, y]
         boxes.append(sbox)
         print('Count:'+str(count))
         print('sbox:'+str(sbox))

    elif event == cv2.EVENT_LBUTTONUP:
        #print 'End Mouse Position: '+str(x)+', '+str(y)
        print('Start Pos Up: '+str(start_x_pos)+', '+str(start_y_pos))
        if start_x_pos==x and start_y_pos==y:
            print('Please drag and move your mouse!')
            return
            
        print('End Mouse Position: '+str(x)+', '+str(y))

        end_x_pos,end_y_pos=x,y
        
        ebox = [x, y]
        boxes.append(ebox)
        print('boxes:'+str(boxes))
        #cv2.rectangle(img,(start_x_pos,start_y_pos),(x,y),(0,255,0),-1)
        
        crop = img[boxes[-2][1]:boxes[-1][1],boxes[-2][0]:boxes[-1][0]]

        cv2.imshow('crop',crop)
        
        k =  cv2.waitKey(0) & 0xFF
        if ord('r')== k:
            cv2.imwrite('Crop'+str(t)+'.jpg',crop)
            print("Written to file")

count = 0
while(1):
    count += 1
    img = cv2.imread('images/fruits.jpg',0)
    # img = cv2.blur(img, (3,3))
    img = cv2.resize(img, None, fx = 1.0,fy = 1.0)

    cv2.namedWindow('real image')
    cv2.setMouseCallback('real image', on_mouse, 0)
    
    #if end_x_pos>-1:
    #    print('END Pos: '+str(end_x_pos)+', '+str(end_y_pos))
    #    cv2.rectangle(img,(start_x_pos,start_y_pos),(end_x_pos,end_y_pos),(0,255,0),3)
    
    cv2.imshow('real image', img)
    if count < 50:
        if cv2.waitKey(20) & 0xFF == 27:
            cv2.destroyAllWindows()
            break
    elif count >= 50:
        if cv2.waitKey(20) & 0xFF == 27:
            cv2.destroyAllWindows()
            break
        count = 0
