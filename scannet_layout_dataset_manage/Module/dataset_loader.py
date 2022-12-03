#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scannet_layout_dataset_manage.Data.dataset import Dataset
from scannet_layout_dataset_manage.Method.depth import \
    getDepthPoints, getLayoutDepthPoints, getUniformDepthPoints
from scannet_layout_dataset_manage.Method.render import \
    renderLayoutDepthImage, renderLayoutDepthPCD


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

    def funcView(self, func, scene_name=None, view_name=None, view=None):
        if view is not None:
            return func(view)

        assert scene_name is not None and view_name is not None
        view = self.getView(scene_name, view_name)
        return func(view)

    def getDepthPoints(self, scene_name=None, view_name=None, view=None):
        return self.funcView(getDepthPoints, scene_name, view_name, view)

    def getLayoutDepthPoints(self, scene_name=None, view_name=None, view=None):
        return self.funcView(getLayoutDepthPoints, scene_name, view_name, view)

    def getUniformDepthPoints(self,
                              scene_name=None,
                              view_name=None,
                              view=None):
        return self.funcView(getUniformDepthPoints, scene_name, view_name,
                             view)

    def renderLayoutDepthImage(self,
                               scene_name=None,
                               view_name=None,
                               view=None):
        return self.funcView(renderLayoutDepthImage, scene_name, view_name,
                             view)

    def renderLayoutDepthPCD(self, scene_name=None, view_name=None, view=None):
        return self.funcView(renderLayoutDepthPCD, scene_name, view_name, view)
