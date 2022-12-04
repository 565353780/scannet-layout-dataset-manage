#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def getDepthImage(view):
    depth_image_file_path = view.depth_image_file_path
    depth_image = cv2.imread(depth_image_file_path)
    depth_image = depth_image[:, :, 0]
    return depth_image


def getLayoutDepthImage(view):
    layout_depth_npy_file_path = view.layout_depth_npy_file_path
    layout_depth_image = np.load(layout_depth_npy_file_path)
    return layout_depth_image


def getUniformDepthImages(view, depth_scale=1):
    depth_image = getDepthImage(view).astype(np.float64)
    depth_max = np.max(depth_image)
    if depth_scale != 1:
        depth_image *= depth_scale

    layout_depth_image = getLayoutDepthImage(view)
    layout_depth_max = np.max(layout_depth_image)
    layout_depth_image *= depth_scale * depth_max / layout_depth_max
    return depth_image, layout_depth_image


def getPointsFromImage(image):
    points = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            points.append([i, j, image[i][j]])
    points = np.array(points)
    return points


def getDepthPoints(view):
    depth_image = getDepthImage(view)
    return getPointsFromImage(depth_image)


def getLayoutDepthPoints(view):
    layout_depth_image = getLayoutDepthImage(view)
    return getPointsFromImage(layout_depth_image)


def getUniformDepthPoints(view, depth_scale=1):
    depth_image, layout_depth_image = getUniformDepthImages(view, depth_scale)
    depth_points = getPointsFromImage(depth_image)
    layout_depth_points = getPointsFromImage(layout_depth_image)
    return depth_points, layout_depth_points
