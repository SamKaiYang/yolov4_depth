#!/usr/bin/env python3
import sys
sys.path.insert(0, '/opt/installer/open_cv/cv_bridge/lib/python3/dist-packages/')
import rospy
import cv2
from get_rs_image import Get_image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

if __name__ == '__main__':
    rospy.init_node('get_d435i_module_image', anonymous=True)
    listener = Get_image()
    
    while not rospy.is_shutdown():
        listener.display_mode = 'depth'
        
        if(listener.display_mode == 'rgb')and(type(listener.cv_image) is np.ndarray):
            print("rgb")
            cv2.imshow("rgb module image", listener.cv_image)
        elif(listener.display_mode == 'depth')and(type(listener.cv_depth) is np.ndarray): 
            print("depth")
            if(type(listener.cv_image) is np.ndarray):
                cv2.imshow("rgb module image", listener.cv_image)
                print(("111111"))
                img_color = np.asanyarray(listener.cv_image)  # 把图像像素转化为数组
                img_depth = np.asanyarray(listener.cv_depth)  # 把图像像素转化为数组
                cv2.circle(img_color, (300, 250), 8, [255, 0, 255], thickness=-1)
                cv2.putText(img_color, "Distance/mm:"+str(img_depth[300, 250]), (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, [255, 0, 255])
        else:
            pass

        #depth =listener.Cal_depth_normal(listener.cv_depth)
        cv2.waitKey(1)

    rospy.spin()