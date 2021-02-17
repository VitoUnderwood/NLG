# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod

class BaseModel(metaclass=ABCMeta):
    """
    some base config for deep model
    """
    __lr = 0.0

    @abstractmethod
    def sigmoid(self, x):
        pass
