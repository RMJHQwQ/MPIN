import argparse
import logging
import os
import random
import sys
import time
from datetime import datetime

import torch


def get_config():
    parser = argparse.ArgumentParser()
    '''Base'''

    parser.add_argument('--num_classes', type=int, default=3)
    parser.add_argument('--model_name', type=str, default='bert',
                        choices=['bert', 'roberta','chi_bert'])
    parser.add_argument('--method_name', type=str, default='sknetandlstm',
                        choices=['gru', 'rnn', 'bilstm', 'lstm', 'fnn', 'textcnn', 'attention', 'lstm+textcnn',
                                 'lstm_textcnn_attention', 'sknet', 'sknet_lstm', 'sknet_lstm_attention','sknetandlstm'])

    '''LLaBa'''
    parser.add_argument('--llaba_dim', type=int, default=512)


    '''Optimization'''
    parser.add_argument('--train_batch_size', type=int, default=8)
    parser.add_argument('--test_batch_size', type=int, default=16)
    parser.add_argument('--num_epoch', type=int, default=50)
    parser.add_argument('--lr', type=float, default=1e-5)
    parser.add_argument('--weight_decay', type=float, default=0.01)

    '''Environment'''
    parser.add_argument('--device', type=str, default='cuda')
    parser.add_argument('--backend', default=False, action='store_true')
    parser.add_argument('--workers', type=int, default=0)
    parser.add_argument('--timestamp', type=int, default='{:.0f}{:03}'.format(time.time(), random.randint(0, 999)))

    args = parser.parse_args()
    args.device = torch.device(args.device)

    '''logger'''
    args.log_name = '{}_{}_{}.log'.format(args.model_name, args.method_name,
                                          datetime.now().strftime('%Y-%m-%d_%H-%M-%S')[2:])
    if not os.path.exists('logs'):
        os.mkdir('logs')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.addHandler(logging.FileHandler(os.path.join('logs', args.log_name)))
    return args, logger
