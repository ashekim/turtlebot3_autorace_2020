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

class ImageCompensation():
    def __init__(self):
        self.sub_image_type = "compressed"  # "compressed" / "raw"
        self.pub_image_type = "raw"         # "compressed" / "raw"

        # # Create a VideoCapture object
        # cap = cv2.VideoCapture(0)
        # ret, cv_image_original = cap.read()
 
        # # # Check if camera opened successfully
        # # if (cap.isOpened() == False): 
        # #   print("Unable to read camera feed")

        # # if ret == True: 
     
        # # Write the frame into the file 'output.avi'
        # # out.write(frame)

        # # Display the resulting frame    
        # # cv2.imshow('frame',frame)
        # cv2.imwrite('test_py.jpg', cv_image_original)


        # subscribes raw image 
        self.sub_image = rospy.Subscriber('/camera/image_output', Image, self.cbImageCompensation, queue_size = 1)

        # # publishes compensated image in raw type
        # self.pub_image = rospy.Publisher('/camera/image_output', Image, queue_size = 1)

        self.cvBridge = CvBridge()

    def cbImageCompensation(self, msg_img):
        cv_image_compensated = np.copy(cv_image_original)

 
        # converts raw image to opencv image
        cv_image_original = self.cvBridge.imgmsg_to_cv2(msg_img, "bgr8")
        self.sub_image_original = rospy.Subscriber('/camera/image_input', Image, self.cbImageProjection, queue_size=1)
        # if self.pub_image_type == "compressed":
        #     # publishes compensated image in compressed type
        #     self.pub_image.publish(self.cvBridge.cv2_to_compressed_imgmsg(cv_image_compensated, "jpg"))

        # elif self.pub_image_type == "raw":
        #     # publishes compensated image in raw type
        #     self.pub_image.publish(self.cvBridge.cv2_to_imgmsg(cv_image_compensated, "bgr8"))

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('image_compensation_sub')
    node = ImageCompensation()
    node.main()
