# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod

class BaseModel(metaclass=ABCMeta):
    """
    some base config for deep model
    """

    @abstractmethod
    def sigmoid(self, x):
        pass

class GPT(BaseModel):
    pass
