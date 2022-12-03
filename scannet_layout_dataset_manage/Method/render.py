#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import open3d as o3d


def renderLayoutDepthImage(view, wait_key=0):
    layout_depth_npy_file_path = view.layout_depth_npy_file_path
    layout_depth_image = np.load(layout_depth_npy_file_path)
    max_depth = np.max(layout_depth_image)
    layout_depth_image = layout_depth_image * 255.0 / max_depth
    layout_depth_image = layout_depth_image.astype(np.uint8)
    cv2.imshow("layout_depth_image", layout_depth_image)
    cv2.waitKey(wait_key)
    return True


def renderLayoutDepthPCD(view):
    depth_scale = 100

    depth_image_file_path = view.depth_image_file_path
    depth_image = cv2.imread(depth_image_file_path)

    depth_max = np.max(depth_image)

    points = []
    for i in range(depth_image.shape[0]):
        for j in range(depth_image.shape[1]):
            depth = depth_image[i][j][0] * depth_scale
            points.append([i, j, depth])
    points = np.array(points)

    depth_pcd = o3d.geometry.PointCloud()
    depth_pcd.points = o3d.utility.Vector3dVector(points)

    layout_depth_npy_file_path = view.layout_depth_npy_file_path
    layout_depth_image = np.load(layout_depth_npy_file_path)

    layout_depth = np.max(layout_depth_image)

    points = []
    for i in range(layout_depth_image.shape[0]):
        for j in range(layout_depth_image.shape[1]):
            depth = layout_depth_image[i][j] * depth_scale
            depth = depth * depth_max / layout_depth
            points.append([i, j, depth])
    points = np.array(points)

    layout_depth_pcd = o3d.geometry.PointCloud()
    layout_depth_pcd.points = o3d.utility.Vector3dVector(points)

    o3d.visualization.draw_geometries([depth_pcd, layout_depth_pcd])
    return True
