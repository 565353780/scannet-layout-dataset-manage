#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class View(object):

    def __init__(self, scene_folder_path, view_name):
        self.scene_folder_path = scene_folder_path
        self.view_name = view_name

        self.color_image_file_path = None
        self.depth_image_file_path = None
        self.labels_json_file_path = None
        self.layout_depth_npy_file_path = None
        self.layout_depth_vis_image_file_path = None
        self.polygon_vis_image_file_path = None
        self.valid_masks_json_file_path = None

        self.loadViewDataPath()
        assert self.isValid()
        return

    def isValid(self):
        if not os.path.exists(self.color_image_file_path):
            return False
        if not os.path.exists(self.depth_image_file_path):
            return False
        if not os.path.exists(self.labels_json_file_path):
            return False
        if not os.path.exists(self.layout_depth_npy_file_path):
            return False
        if not os.path.exists(self.layout_depth_vis_image_file_path):
            return False
        if not os.path.exists(self.polygon_vis_image_file_path):
            return False
        if not os.path.exists(self.valid_masks_json_file_path):
            return False
        return True

    def loadViewDataPath(self):
        self.color_image_file_path = self.scene_folder_path + \
            "color/" + self.view_name + ".jpg"
        self.depth_image_file_path = self.scene_folder_path + \
            "depth/" + self.view_name + ".png"
        self.labels_json_file_path = self.scene_folder_path + \
            "labels_json/" + self.view_name + ".json"
        self.layout_depth_npy_file_path = self.scene_folder_path + \
            "layout_depth/" + self.view_name + ".npy"
        self.layout_depth_vis_image_file_path = self.scene_folder_path + \
            "layout_depth_vis/" + self.view_name + ".jpg"
        self.polygon_vis_image_file_path = self.scene_folder_path + \
            "polygon_vis/" + self.view_name + ".jpg"
        self.valid_masks_json_file_path = self.scene_folder_path + \
            "valid_masks/" + self.view_name + ".json"
        return True

    def outputInfo(self, info_level=0):
        line_start = "\t" * info_level
        print(line_start + "[View]")
        print(line_start + "\t view_name: " + self.view_name)
        print(line_start + "\t scene_folder_path: " + self.scene_folder_path)
        print(line_start + "\t color_image_file_path: " +
              self.color_image_file_path)
        print(line_start + "\t depth_image_file_path: " +
              self.depth_image_file_path)
        print(line_start + "\t labels_json_file_path: " +
              self.labels_json_file_path)
        print(line_start + "\t layout_depth_npy_file_path: " +
              self.layout_depth_npy_file_path)
        print(line_start + "\t layout_depth_vis_image_file_path: " +
              self.layout_depth_vis_image_file_path)
        print(line_start + "\t polygon_vis_image_file_path: " +
              self.polygon_vis_image_file_path)
        print(line_start + "\t valid_masks_json_file_path: " +
              self.valid_masks_json_file_path)
        return True
