#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JimmyChen v3.0 - MackaJunest COPYRIGHT 2022

front
leg  leg1|    |leg2
4 groups: 1,2  -|1      |    |
           3,4  -|2_____Jimmychen
           5,6  -|3      |    |
           7,8  -|4  leg3|    |leg4
back
"""

import math

SHANK_LENGTH = 150  # shank
HAM_LENGTH = 198  # ham

def calculate_angles(x, y):
    """
    Calculate the shank and ham angles for a given x, y coordinate.

    Args:
    x (float): x coordinate
    y (float): y coordinate

    Returns:
    Tuple[float, float]: shank and ham angles in degrees
    """
    L3 = math.sqrt(x**2 + y**2)
    theta1 = math.acos((SHANK_LENGTH**2 + HAM_LENGTH**2 - L3**2) / (2 * SHANK_LENGTH * HAM_LENGTH))
    shank_angle =  (180 - math.degrees(theta1))
    L4 = math.sqrt(L3**2 - x**2)
    theta3 = math.asin((math.sin(theta1) / L3) * SHANK_LENGTH)
    ham_angle = math.degrees(math.atan(L4 / x)) - math.degrees(theta3)
    return shank_angle, ham_angle

def calculate_coordinates(shank_angle, ham_angle):
    """
    Calculate the x and y coordinate for a given shank and ham angle.

    Args:
    shank_angle (float): shank angle in degrees
    ham_angle (float): ham angle in degrees

    Returns:
    Tuple[float, float]: x and y coordinate
    """
    xh = math.cos(math.radians(shank_angle)) * HAM_LENGTH
    yh = math.sqrt(HAM_LENGTH**2 + HAM_LENGTH**2)
    theta4 = 180 - shank_angle
    L3 = math.sqrt(SHANK_LENGTH**2 + HAM_LENGTH**2 - 2 * SHANK_LENGTH * HAM_LENGTH * (
