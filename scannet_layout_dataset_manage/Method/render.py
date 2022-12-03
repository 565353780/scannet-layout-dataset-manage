#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import open3d as o3d

from scannet_layout_dataset_manage.Method.depth import getUniformDepthPoints


def renderLayoutDepthImage(view, wait_key=0):
    layout_depth_npy_file_path = view.layout_depth_npy_file_path
    layout_depth_image = np.load(layout_depth_npy_file_path)
    max_depth = np.max(layout_depth_image)
    layout_depth_image = layout_depth_image * 255.0 / max_depth
    layout_depth_image = layout_depth_image.astype(np.uint8)
    cv2.imshow("layout_depth_image", layout_depth_image)
    cv2.waitKey(wait_key)
    return True


def renderLayoutDepthPCD(view, depth_scale=100):
    depth_points, layout_depth_points = getUniformDepthPoints(
        view, depth_scale)

    depth_pcd = o3d.geometry.PointCloud()
    depth_pcd.points = o3d.utility.Vector3dVector(depth_points)

    layout_depth_pcd = o3d.geometry.PointCloud()
    layout_depth_pcd.points = o3d.utility.Vector3dVector(layout_depth_points)

    o3d.visualization.draw_geometries([depth_pcd, layout_depth_pcd])
    return True
