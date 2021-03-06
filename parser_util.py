# coding=utf-8
import os
import argparse


def get_parser():
    # 创建解析对象
    parser = argparse.ArgumentParser()
    # 添加参数
    # os.sep根据操作系统自动选择路径分隔符\或者/
    parser.add_argument('-name', '--name',
                        type=str,
                        help='dataset',
                        default='webnlg.json')
    # 命令行解析的参数命令名为dataset_root，简写为root, 参数类型

    parser.add_argument('-exp', '--experiment_root',
                        type=str,
                        help='root where to store models, losses and accuracies',
                        default='experiment' + os.sep + 'output')

    # FixMe
    parser.add_argument('-nep', '--epochs',
                        type=int,
                        help='number of epochs to train for',
                        default=10)

    parser.add_argument('-lr', '--learning_rate',
                        type=float,
                        help='learning rate for the model, default=0.001',
                        default=0.001)

    # scheduler与optimizer不同，其在每个epoch调整学习率，每个step为一个epoch
    # 每20个epoch调整一次学习率变为lr*gamma
    parser.add_argument('-lrS', '--lr_scheduler_step',
                        type=int,
                        help='StepLR learning rate scheduler step, default=20',
                        default=20)

    parser.add_argument('-lrG', '--lr_scheduler_gamma',
                        type=float,
                        help='StepLR learning rate scheduler gamma, default=0.5',
                        default=0.5)

    # FixMe
    # 每个epoch的小批数
    parser.add_argument('-bcN', '--batch_num',
                        type=int,
                        help='number of episodes per epoch, default=100',
                        default=10)

    # FixMe
    # 每个小批中指定的随机类的数目，默认为2
    parser.add_argument('-cTr', '--classes_per_it_tr',
                        type=int,
                        help='number of random classes per episode for training, default=60',
                        default=2)

    # FixMe
    # 嵌入空间维度
    parser.add_argument('-hd', '--hidden_dim',
                        type=int,
                        help='dimension of embedding space',
                        default=100)

    # 每个类的支持集样本数
    parser.add_argument('-nsTr', '--num_support_tr',
                        type=int,
                        help='number of samples per class to use as support for training, default=5',
                        default=1)

    # 每个类的查询集样本数
    parser.add_argument('-nqTr', '--num_query_tr',
                        type=int,
                        help='number of samples per class to use as query for training, default=5',
                        default=1)


    # 使初始随机值一致，如果不设置，那么seed就是当前时间，每次生成的随机数都不一样
    parser.add_argument('-seed', '--seed',
                        type=int,
                        help='input for the manual seeds initializations',
                        default=7)

    # cuda,默认为真
    parser.add_argument('--cuda',
                        action='store_true',
                        help='enables cuda',
                        default=True)

    return parser
