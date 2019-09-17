import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow.contrib.legacy_seq2seq.python.ops import seq2seq
import jieba
import random
from pre_data import WordToken
# 输入序列长度
input_seq_len = 5
# 输出序列长度
output_seq_len = 5
# 空值填充0
PAD_ID= 0
# 输出序列起始标记
GO_ID = 1
# 结尾标记
EOS_ID = 2
# LSTM神经元size
size = 8
# 初始化学习率
init_learning_rate = 0.001
# 在样本中出现频率超过这个词才会进入词表
min_freq = 10

wordToken = WordToken()

def get_train_set():
    global num_encoder_symbols, num_decoder_symbols
    train_set = []
    with open('./chatbot/question.txt', 'r') as question_file:
        with open('./chatbot/answer.txt', 'r') as answer_file:
            while True:
                question = question_file.readline()
                answer = answer_file.readline()
                if question and answer:
                    question = question.strip()
                    answer = answer.strip()

                    question_id_list = get_id_list_from(question)
                    answer_id_list = get_id_list_from(answer)
                    answer_id_list.append(EOS_ID)
                    train_set.append([question_id_list, answer_id_list])
                else:
                    break
    return train_set

def get_id_list_from(sentence):
    sentence_id_list = []
    seg_list = jieba.cut(sentence)
    for str in seg_list:
        id = wordToken.word2id(str)
        if id:
            sentence_id_list.append(wordToken.word2id(str))
    return sentence_id_list
