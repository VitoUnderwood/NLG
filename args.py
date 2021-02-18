# -*- coding:utf-8 -*-
import argparse
class Args:
    def __init__(self, parser:argparse.ArgumentParser):
        self.__args = parser.parse_args()
        self.__device = 0
        self.__config_path = ''
        self.__train_file_path = ''
        self.__test_file_path = ''
        self.__pretrained_model_path = ''
        self.__num_train_epochs = 10
        self.__train_batch_size = 16
        self.__test_batch_size = 8
        self.__learning_rate = 1e-4
        self.__warmup_proportion = 0.1
        self.__adam_epsilon = 1e-8
        self.__logging_steps = 20
        self.__eval_steps = 4000
        self.__output_dir = ''
        self.__seed = 2021
        self.__max_len  =512

    @property
    def args(self):
        return self.__args
    @args.setter
    def args(self, parser:argparse.ArgumentParser):
        self.__args = parser.parse_args()