#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from scannet_layout_dataset_manage.Data.view import View


class Scene(object):

    def __init__(self, scene_folder_path):
        self.scene_folder_path = scene_folder_path

        self.view_dict = {}

        self.loadViews()
        return

    def loadViews(self):
        color_folder_path = self.scene_folder_path + "color/"
        view_file_name_list = os.listdir(color_folder_path)

        for view_file_name in view_file_name_list:
            view_name = view_file_name.split(".jpg")[0]
            self.view_dict[view_name] = View(self.scene_folder_path, view_name)
        return True
