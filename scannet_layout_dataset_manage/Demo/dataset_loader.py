#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

from scannet_layout_dataset_manage.Module.dataset_loader import DatasetLoader


def demo():
    scannet_layout_dataset_folder_path = "/home/chli/chLi/ScanNetLayout/"
    print_progress = True

    dataset_loader = DatasetLoader(scannet_layout_dataset_folder_path,
                                   print_progress)

    scene_name_list = dataset_loader.getSceneNameList()
    print("scene_name_list")
    print(scene_name_list)

    scene_name = scene_name_list[0]
    view_name_list = dataset_loader.getViewNameList(scene_name)
    print("view_name_list")
    print(view_name_list)

    if len(view_name_list) > 0:
        view_name = view_name_list[0]
        view = dataset_loader.getView(scene_name, view_name)
        view.outputInfo()

        depth_image_file_path = view.depth_image_file_path
        depth_image = cv2.imread(depth_image_file_path)

        layout_depth_image = dataset_loader.getLayoutDepthImage(view=view)

        cv2.imshow("depth_image", depth_image)
        cv2.imshow("layout_depth_image", layout_depth_image)
        cv2.waitKey(0)
    return True
