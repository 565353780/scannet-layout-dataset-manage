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

        dataset_loader.renderLayoutDepthImage(view=view)

        dataset_loader.renderLayoutDepthPCD(view=view)
    return True
