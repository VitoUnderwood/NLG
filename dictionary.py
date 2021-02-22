# -*- coding:utf-8 -*-
import json

from tqdm import tqdm
from transformers import BertTokenizer


class Dictionary:
    def __init__(self, args):
        self.__args = args
        self.data_set = []
        self.__tokenizer = BertTokenizer.from_pretrained(args.vocab_path)
        self.__max_len = args.max_len
        self.__title_max_len = args.title_max_len
        self.__content_id = self.__tokenizer.convert_tokens_to_ids("[Content]")
        self.__title_id = self.__tokenizer.convert_tokens_to_ids("[Title]")

    def readFromJson(self, filePath):
        """
        从json文件中加载数据，由于原始数据格式各种各样，提前处理成统一的json文件格式
        Args:
            filePath:

        Returns:

        """
        with open(filePath, "r", encoding="utf-8") as f:
            data = json.load(f)
            for idx, sample in enumerate(tqdm(data, desc="iter")):
                # 使用convert_feature函数，对新闻正文和标题进行索引化，生成模型所需数据格式
                input_ids, token_type_ids = self.convertWrod2Id(sample)
                self.data_set.append({"input_ids": input_ids, "token_type_ids": token_type_ids})
        return self.data_set

    def convertWrod2Id(self, sample):
        """
        数据处理函数
        Args:
            sample: 一个字典，包含新闻的正文和新闻的标题，格式为{"content": content, "title": title}

        Returns:

        """
        input_ids = []
        token_type_ids = []
        # 对新闻正文进行tokenizer.tokenize分词
        content_tokens = self.__tokenizer.tokenize(sample["content"])
        title_tokens = self.__tokenizer.tokenize(sample["title"].replace(" ", "[Space]"))
        # 判断如果标题过长，进行截断
        if len(title_tokens) > self.__title_max_len:
            title_tokens = title_tokens[:self.__title_max_len]
        # 判断如果正文过长，进行截断
        if len(content_tokens) > self.__max_len - len(title_tokens) - 3:
            content_tokens = content_tokens[:self.__max_len - len(title_tokens) - 3]
        # 生成模型所需的input_ids和token_type_ids
        input_ids.append(self.__tokenizer.cls_token_id)
        token_type_ids.append(self.__content_id)
        input_ids.extend(self.__tokenizer.convert_tokens_to_ids(content_tokens))
        token_type_ids.extend([self.__content_id] * len(content_tokens))
        input_ids.append(self.__tokenizer.sep_token_id)
        token_type_ids.append(self.__content_id)
        input_ids.extend(self.__tokenizer.convert_tokens_to_ids(title_tokens))
        token_type_ids.extend([self.__title_id] * len(title_tokens))
        input_ids.append(self.__tokenizer.sep_token_id)
        token_type_ids.append(self.__title_id)
        # 判断input_ids与token_type_ids长度是否一致
        assert len(input_ids) == len(token_type_ids)
        # 判断input_ids长度是否小于等于最大长度
        assert len(input_ids) <= self.__max_len
        return input_ids, token_type_ids
