import numpy as np
from gensim.models.word2vec import Word2Vec

x_train = np.load('data/x_train.npy')

#训练Word2vec浅层神经网络模型

w2v = Word2Vec(size=300,min_count=10)
w2v.build_vocab(x_train)
w2v.train(x_train,total_examples=w2v.corpus_count,epochs=w2v.iter)

# 对每个句子的词向量进行求和计算
def sum_vec(text):
    vec = np.zeros(300).reshape((1, 300))
    for word in text:
        try:
            vec += w2v[word].reshape((1, 300))
        except KeyError:
            continue
    return vec

# 将词向量保存为 Ndarray
train_vec = np.concatenate([sum_vec(z) for z in x_train])

# 保存 Word2Vec 模型及词向量
w2v.save('data/w2v_model.pkl')
np.save('data/x_train_vec.npy', train_vec)
