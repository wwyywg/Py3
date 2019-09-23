from sklearn.feature_extraction.text import TfidfVectorizer

def tfidfvec():
    """
    对文本进行特征值化
    :return: 
    """
    tf = TfidfVectorizer()

    # data = cv.fit_transform(["life is short,i like python","life is too long,i dislike python"])
    data = tf.fit_transform(["生命 短暂，我 喜欢 python","生命 太长，我 不喜欢 python"])

    print(tf.get_feature_names())

    print(data)

    return None

if __name__ == '__main__':
    tfidfvec()