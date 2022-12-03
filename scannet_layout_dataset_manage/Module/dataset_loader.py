#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scannet_layout_dataset_manage.Data.dataset import Dataset


class DatasetLoader(object):

    def __init__(self, dataset_folder_path, print_progress=False):
        self.dataset = Dataset(dataset_folder_path, print_progress)
        return

    def getSceneNameList(self):
        return list(self.dataset.scene_dict.keys())

    def isSceneNameValid(self, scene_name):
        return scene_name in self.dataset.scene_dict.keys()

    def isViewNameValid(self, scene_name, view_name):
        if not self.isSceneNameValid(scene_name):
            return False
        return view_name in self.dataset.scene_dict[scene_name].view_dict.keys(
        )

    def getViewNameList(self, scene_name):
        assert self.isSceneNameValid(scene_name)
        return list(self.dataset.scene_dict[scene_name].view_dict.keys())

    def getScene(self, scene_name):
        assert self.isSceneNameValid(scene_name)
        return self.dataset.scene_dict[scene_name]

    def getView(self, scene_name, view_name):
        assert self.isViewNameValid(scene_name, view_name)
        return self.dataset.scene_dict[scene_name].view_dict[view_name]
