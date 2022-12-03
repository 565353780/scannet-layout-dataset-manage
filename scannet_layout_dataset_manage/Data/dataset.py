#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tqdm import tqdm

from scannet_layout_dataset_manage.Data.scene import Scene


class Dataset(object):

    def __init__(self, dataset_folder_path, print_progress=False):
        self.dataset_folder_path = dataset_folder_path

        self.scene_dict = {}

        self.loadScenes(print_progress)
        return

    def loadScenes(self, print_progress=False):
        scene_root_folder_path = self.dataset_folder_path + "data/"
        scene_name_list = os.listdir(scene_root_folder_path)
        for_data = scene_name_list
        if print_progress:
            print("[INFO][Dataset::loadScenes]")
            print("\t start load all scene...")
            for_data = tqdm(for_data)
        for scene_name in for_data:
            scene_folder_path = scene_root_folder_path + scene_name + "/"
            self.scene_dict[scene_name] = Scene(scene_folder_path)
        return True
