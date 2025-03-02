from typing import Dict, List, Optional, Union, Tuple, Callable
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from base_bert import BertPreTrainedModel
from utils import *
from bert import BertSelfAttention
from tqdm import tqdm

print('testing testing')

# % operator
print(3 % 3)
print(4 % 3)
print(5 % 3)

# iter
'''
x = iter([1,2,3])
print(next(x))
'''

# test tqdm
'''
data_loader = range(100)
for int in tqdm(data_loader):
    print(int)
'''

# test torch.mul
'''
a = torch.randn(1,4)
b = torch.randn(1,4)
print(a)
print(b)
print(b.transpose(-1, -2))
print(a.matmul(b.transpose(-1, -2)))
'''

# test torch.view
'''
a = torch.randn(2,2,3)
print(a)
print(a.shape)
b = a.view(-1)
print(b)
print(b.shape)
'''

# test torch.mul
'''
a = torch.randn(2,2,3)
b = torch.randn(2,2,3)
print(a)
print(b)
output = a.mul(b)
print(output)
'''

# how does softmax behave? (with respect to dim parameter)
'''
m = nn.Softmax(dim=0)
input = torch.randn(2, 3)
output = m(input)
print(output)
'''

# F.softmax
'''
input = torch.randn(2, 3)
output = F.softmax(input, 0)
print(output)
'''

# functions with tensor
'''
t1 = torch.randn(2, 3)
t2 = torch.randn(3, 2)
print(t1)
print(t2)
output = t1.matmul(t2)
print(output)
'''

# debug bert.BertSelfAttention.attention
'''
class Config:
  def __init__(self, num_attention_heads, hidden_size, attention_probs_dropout_prob):
    self.num_attention_heads = num_attention_heads
    self.hidden_size = hidden_size
    self.attention_probs_dropout_prob = attention_probs_dropout_prob
config = Config(2, 4, 0.1)

layer = BertSelfAttention(config)

key = torch.randn(1, 2, 10, 2)
query = torch.randn(1, 2, 10, 2)
value = torch.randn(1, 2, 10, 2)
attention_mask = torch.zeros(1, 1, 1, 10)
attn_output = layer.attention(key, query, value, attention_mask)
'''
