from sklearn.feature_extraction.text import CountVectorizer

def countvec():
    """
    对文本进行特征值化
    :return: 
    """
    cv = CountVectorizer()

    # data = cv.fit_transform(["life is short,i like python","life is too long,i dislike python"])
    data = cv.fit_transform(["生命 短暂，我 喜欢 python","生命 太长，我 不喜欢 python"])

    print(cv.get_feature_names())

    print(data.toarray())

    return None

if __name__ == '__main__':
    countvec()