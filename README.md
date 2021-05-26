YOLOv4_depth
=====
預先安裝內容如下
----
1. Cuda 10.2以上
2. OpenCV 3.2以上
2. Ros melodic
3. cv_bridge(for use python3)
4. Realsense driver


本人裝置環境,可參考
----
1. Cuda 11.0 or 10.2
2. OpenCV 3.2
2. Ros melodic
3. cv_bridge(for use python3)
4. Realsense driver v2.45
5. realsense-ros (build3.2.0)

以上安裝教學可參考
請詳閱[ubuntu18.04 install](https://www.notion.so/ubuntu18-04_install-6cb8f5133616448abfe6428ff8cc8c78)


如何使用
----
1. clone
```bash
cd ~/<catkin_workspace>/src/
git clone ...
cd yolov4_depth/darknet_ros
git clone https://github.com/AlexeyAB/darknet.git
```
2. 安裝realsense-ros及clone darknet,並編譯
```bash
cd ~/<catkin_workspace>/src/
git clone https://github.com/IntelRealSense/realsense-ros.git
catkin_init_workspace 
cd ..
sudo apt-get install ros-melodic-ddynamic-reconfigure
catkin_make clean
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
catkin_make install
```
## download weight
```bash
cd <catkin_workspace>/src/darknet_ros/darknet_ros/yolo_network_config/weights
# yolo v4
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
# yolo v4 tiny
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights
```

3. 實際測試
```bash
roslaunch realsense2_camera rs_rgbd.launch
roslaunch darknet_ros yolo_v4_tiny.launch
```
## 讀取距離資訊
1.use pyrealsense
```bash
roslaunch realsense2_camera rs_rgbd.launch
rosrun get_rs_image Get_depth.py 
```
2.use realsense ros
```bash
roslaunch realsense2_camera rs_rgbd.launch
rosrun test_rs_img get_rs_module_img.py 
```
## 讀取人的距離資訊
```bash
roslaunch realsense2_camera rs_rgbd.launch
roslaunch yolo_detection yolo_get_person_depth.launch 
```

>>2021/05/20 更新
1.readme markdown 
