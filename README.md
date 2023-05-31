# 基于凯斯西储大学数据集的故障诊断

Case Western Reserve University(凯斯西储大学)

__参考中文博客:__

- CSDN博客链接：https://blog.csdn.net/weixin_50642818/category_11953250.html

__使用方法：__

```python
import cwru
data = cwru.CWRU("12DriveEndFault", "1797", 384)
```

再用 `data.X_train, data.y_train, data.X_test, data.y_test, data.labels, data.nclasses`

## 详解

- data.X_train：训练数据的纯特征数据
- data.y_train：训练数据的标签（0-15，共16个数字）
- data.labels：标签0-15对应的具体的故障诊断类型名称
- data.nclasses：一共多少类，输出16
- "12DriveEndFault"：采样频率12kHz的驱动端故障数据
- 1797：每分钟转速，负载不同对应转速就不同：
  - 0hp（马力）——1797
  - 1hp（马力）——1772
  - 2hp（马力）——1750
  - 3hp（马力）——1730
- 384：每列信号长度，训练样本和测试样本的大小会随之改变，可用如下函数计算具体样本长度

## 例子代码

```python
import cwru
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
print(i, j, k)
```

输出结果如下：

```text
('0.007-Ball', '0.007-InnerRace', '0.007-OuterRace12', '0.007-OuterRace3',
 '0.007-OuterRace6', '0.014-Ball', '0.014-InnerRace', '0.014-OuterRace6',
 '0.021-Ball', '0.021-InnerRace', '0.021-OuterRace12', '0.021-OuterRace3', 
'0.021-OuterRace6', '0.028-Ball', '0.028-InnerRace', 'Normal'）
```

- i= 235
- 总的训练样本数据个数 j = 4032
- 测试样本数据个数 k = 1355

试了一下300-700比较合适
