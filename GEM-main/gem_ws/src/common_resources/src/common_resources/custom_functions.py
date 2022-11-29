#!/usr/bin/env python3

import cv2
import socket
import dynamic_reconfigure.client
from sensor_msgs.msg import CameraInfo
import traceback
import rospy
import multiprocessing
import os
import pipes
import threading
import sys

def init_window(win_name, height=500, width=500, x=0, y=0):
    """Initialized a window for image

    Initialized a window with a predefined size and position. It returns a true flag after the function is called

    Parameters
    ----------
    win_name : str
        The window name
    height : int, optional
        The window height
    width : int, optional
        The window width
    x : int, optional
        The position of the window along the x axis
    y : int, optional
        The position of the window along the y axis

    """

    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(win_name, 500, 500)
    cv2.moveWindow(win_name, 0, 0)

    return True

def get_ip(prefix="", dots=False):
    """Get the marospy.Publisherchine in a network

    The return IP will in a string and all dots are removed by default
    
    Parameters
    ----------
    prefix: str
        A string to be added in front of the IP
    dots: bool
        True for returning with dots

    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        mach_ip = str(s.getsockname()[0])
        if not dots:
            mach_ip = mach_ip.replace('.','')
        mach_ip = prefix + mach_ip
    except:
        mach_ip = "NUC_0000000"

    return mach_ip

def server_init(server_name, params=None):
    """Common initialization the dynamic reconfigure

    - Get the IP address of the machine within the network
    - Connects to the dynamic reconfigure server
    - Updates the parameters in the server

    Parameters
    ----------
    params: dict
        A dictionary that is used to update the parameters
    
    Returns
    -------
    client: client
        Dynamic reconfigure client
    server_status: bool
        A flag on the success of the connection 
    mach_ip: str
        The ip address of the machine
    """

    mach_ip = get_ip(prefix="/NUC_")

    try:
        client = dynamic_reconfigure.client.Client(server_name, timeout=1)
        client.update_configuration(params)
        server_status = True

    except rospy.exceptions.ROSException:
        print("Unable to connect to parameter server!")
        server_status = False
        client = None

    except:
        print(traceback.format_exc())

    return client, server_status, mach_ip

def manual_cam_info():
    """Return a fixed camera info.

    Useful for testing cameras without calibration
    """

    camera_info = CameraInfo()
    camera_info.header.frame_id = "camera"
    camera_info.width = int(6176)
    camera_info.height = int(2064)
    camera_info.distortion_model = 'plumb_bob'
    camera_info.K = [1725.430495605492, 0, 1487.857389070032, 0, 2*1725.55980092612, 2*1026.660850299249, 0, 0, 1]
    camera_info.D = [-0.1078255452812613, 0.05908800312753438, -0.0008704391991578348, -0.0002940945510263317, 0]
    camera_info.R = [1, 0, 0, 0, 1, 0, 0, 0, 1]
    camera_info.P = [1654.254760742188, 0, 1489.703641266606, 0, 0, 2*1668.324096679688, 2*1024.072899447885, 0, 0, 0, 1, 0]

    return camera_info
