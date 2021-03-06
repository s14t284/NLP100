# -*- coding: utf-8 -*-
import re
from logistic import Logistic_Regression
from nltk import PorterStemmer


def get_sentence_vector(sentence: str, features: list) -> list:
    """
    文章のベクトルを返す
    """

    vector = []
    stemmer = PorterStemmer()

    # 単語分割
    words = re.split(r"[,.:;\s]", sentence[2:])
    while words.count("") > 0:
        words.remove("")
    stem_words = [stemmer.stem(word) for word in words]

    # ベクトル作成
    for i in range(len(features)):
        # BoWに素性を変更
        vector.append(float(stem_words.count(features[i])))

    return vector


def get_sentence_learn_vector(sentence: str, features: list):
    """
    学習のための文章のベクトルを返す
    """
    sign = float(sentence[:2])
    value = len(features)
    vector = get_sentence_vector(sentence, features)

    # 文章の極性によってベクトルの位置を変更
    return vector, sign


if __name__ == "__main__":
    vectors = []
    sign = []
    print("setting...")
    # 素性のリストを用意
    with open("features.txt", "r") as f:
        features = [word[:-1] for word in f.readlines()]

    # 素性のリストを使って学習データを用意
    with open("sentiment.txt", "r") as f:
        for sentence in f.readlines():
            vec, sig = get_sentence_learn_vector(sentence, features)
            vectors.append(vec)
            sign.append(sig)

    # 学習
    learn_circuit = Logistic_Regression(vectors, sign)
    learn_circuit.learn()
    with open("learndata.txt", "w") as f:
        print("input text...")
        data = map(str, learn_circuit.get_learn_data())
        f.write("\n".join(data))

    # 試しに推定
    with open("sentiment.txt", "r") as f:
        vec = get_sentence_vector(f.readlines()[0], features)
        print(learn_circuit.get_prob(vec))
