#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scannet_layout_dataset_manage.Data.dataset import Dataset


class DatasetLoader(object):

    def __init__(self, dataset_folder_path, print_progress=False):
        self.dataset = Dataset(dataset_folder_path, print_progress)
        return
