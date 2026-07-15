## add LLM basic knowledge
### 1.LLM
LLM = Large Language Model(大语言模型),根据大量文本学习出来的“预测下个Token“的模型。
比如prompt是”中国的首都是“，模型内部经过计算得出最可能的回答是”北京“，然后输出
### 2.Token
LLM会将输入的prompt转化为Token(词元)，转化流程：prompt->Tokenizer->Token->数字ID->神经网络计算
Token越多，推理越慢，延迟越高
### 3.Transformer
一种让模型理解上下文关系的结构。核心是Attention(注意力机制)，简单理解就是模型决定一句话里哪些词更重要
### 4.Embedding(向量)
把文字转换成数字向量，让机器能比较语义
### 5.Prompt
给模型的输入指令，输入指令越详细，模型给出的回答越贴近要求
### 6.Context Window(上下文窗口)
模型一次能看到多少信息，人和模型聊天，如果聊天数量超过窗口，早期的内容可能丢失(maybe类似redis？)
### 7.Temperature
控制随机性
### 8.Hallucination(幻觉)
LLM一本正经胡说八道(豆包胡说八道的时候是出现了Hallucination)
### 9.RAG(Retrieval Augmented Generation)
检索增强生成，给模型资料看，让他根据资料回答
### 10.Fine-tuning(微调)
重新训练模型一部分能力，模型会中文经过微调让他更懂医疗等行业
