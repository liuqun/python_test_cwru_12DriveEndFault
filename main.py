import cwru

def main_program():
    print('采样频率12kHz的驱动端故障数据')
    print('实验数据集 exp="12DriveEndFault", 转速 rpm="1797", 每列信号长度 length=384\n')

    data = cwru.CWRU("12DriveEndFault", "1797", 384)
    labels = data.labels
    print(labels)

    i = 0
    j = 0
    k = 0
    for num in data.y_train:
        j = j+1   #总的训练样本数据个数
        if num == 13:  #训练样本每种类型的样本长度，1-14差不多长，15（正常类型）大概是其它的2倍
            i = i+1
    for num in data.y_test:
        k = k+1   #测试样本数据个数
    #print("训练数据的标签（0-15, 共16个数字）data.y_train = ", data.y_train)
    print("i=", i)
    print("总的训练样本数据个数j=", j)
    print("测试样本数据个数k=", k)
    print("================\nmain_program() finish!\n")


if __name__ == "__main__":
    main_program()