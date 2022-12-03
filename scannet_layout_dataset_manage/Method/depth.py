#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def getDepthPoints(view):
    depth_image_file_path = view.depth_image_file_path
    depth_image = cv2.imread(depth_image_file_path)

    points = []
    for i in range(depth_image.shape[0]):
        for j in range(depth_image.shape[1]):
            depth = depth_image[i][j][0]
            points.append([i, j, depth])
    points = np.array(points)
    return points


def getLayoutDepthPoints(view):
    layout_depth_npy_file_path = view.layout_depth_npy_file_path
    layout_depth_image = np.load(layout_depth_npy_file_path)

    points = []
    for i in range(layout_depth_image.shape[0]):
        for j in range(layout_depth_image.shape[1]):
            depth = layout_depth_image[i][j]
            points.append([i, j, depth])
    points = np.array(points)

    return points


def getUniformDepthPoints(view, depth_scale=1):
    depth_points = getDepthPoints(view)
    depth_max = np.max(depth_points[:, 2])
    if depth_scale != 1:
        depth_points[:, 2] *= depth_scale

    layout_depth_points = getLayoutDepthPoints(view)
    layout_depth_max = np.max(layout_depth_points[:, 2])
    layout_depth_points[:, 2] *= depth_scale * depth_max / layout_depth_max
    return depth_points, layout_depth_points
