#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright 2018 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

# Author: Will Son, Ashe Kim

import rospy
import numpy as np
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage
from dynamic_reconfigure.server import Server


class ImagePublish():
    def __init__(self):
        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()    
        # Write the frame into the file 'output.avi'
        # out.write(frame)
    
        # Display the resulting frame    
        # cv2.imshow('frame',frame)
        cv2.imwrite('test_py.jpg', frame)
        img = cv2.imread('~/catkin_ws/test_py.jpg', cv2.IMREAD_COLOR)
     
        bridge = CvBridge()
        image_message = bridge.cv2_to_compressed_imgmsg(img, "bgr8")
        image_pub = rospy.Publisher("image_topic",CompressedImage, queue_size = 1)
        image_pub.publish(image_message)
      
    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('pub_image')
    node = ImagePublish()
    node.main()
