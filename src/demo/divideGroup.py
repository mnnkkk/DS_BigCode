'''
使用pca自动分组
'''
import json

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 229  # 维度 229


def distance_fun(p1, p2, N):
    result = 0
    for i in range(0, N):
        result = result + ((p1[i] - p2[i]) ** 2)
    return np.sqrt(result)


def mean_fun(a):
    return np.mean(a, axis=0)


def farthest(center_arr, arr):
    f = [0, 0]
    max_d = 0
    for e in arr:
        d = 0
        for i in range(center_arr.__len__()):
            d = d + np.sqrt(distance_fun(center_arr[i], e, N))
        if d > max_d:
            max_d = d
            f = e
    return f


def closest(a, arr):
    c = arr[1]
    min_d = distance_fun(a, arr[1])
    arr = arr[1:]
    for e in arr:
        d = distance_fun(a, e)
        if d < min_d:
            min_d = d
            c = e
    return c


def pca(XMat):
    average = mean_fun(XMat)
    m, n = np.shape(XMat)
    data_adjust = []
    avgs = np.tile(average, (m, 1))
    data_adjust = XMat - avgs
    cov_x = np.cov(data_adjust.T)  # 计算协方差矩阵
    feat_value, feat_vec = np.linalg.eig(cov_x)  # 求解协方差矩阵的特征值和特征向量
    index = np.argsort(-feat_value)  # 依照featValue进行从大到小排序

    sum_feat_value = sum(index)
    sumt = 0
    k = 0
    while (sumt < 0.9 * sum_feat_value):
        sumt += index[k]
        k += 1

    final_data = []
    select_vec = np.matrix(feat_vec.T[index])  # 所以这里须要进行转置
    final_data = data_adjust * select_vec.T
    recon_data = (final_data * select_vec) + average

    return final_data, recon_data, k


def plot_best_fit(data1, data2):
    data_arr1 = np.array(data1)
    data_arr2 = np.array(data2)

    m = np.shape(data_arr1)[0]
    axis_x1 = []
    axis_y1 = []
    axis_x2 = []
    axis_y2 = []
    for i in range(m):
        axis_x1.append(data_arr1[i, 0])
        axis_y1.append(data_arr1[i, 1])
        axis_x2.append(data_arr2[i, 0])
        axis_y2.append(data_arr2[i, 1])
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    # ax.scatter(axis_x1, axis_y1, s=50, c='red', marker='s')
    ax.scatter(axis_x2, axis_y2, s=1, c='blue')
    plt.show()


if __name__ == "__main__":
    '''
    arr = np.random.randint(0,10000, size=(1000, 1, N))[:, 0, :]
    XMat=arr
    '''


    XMat = []

    json_data = open('../../resource/test_data1.json', encoding='utf-8').read()
    data = json.loads(json_data)

    json_data = open('../../resource/test_data1_problem_list.json', encoding='utf-8').read()
    all_problem_list = json.loads(json_data)

    for k, v in data.items():
        sub_XMat = [0] * N
        for problem_name in v["problems"]:
            for i in range(1, N):
                if problem_name == all_problem_list[str(i)]:
                    sub_XMat[i] = 1000
                    break
        #print(sub_XMat)
        XMat.append(sub_XMat)
    #print(XMat)


    '''
    block1 = np.random.randint(0, 2000, size=(100000, 1, N))[:, 0, :]  # 分区间生成随机数
    block2 = np.random.randint(2000, 4000, size=(100000, 1, N))[:, 0, :]
    block3 = np.random.randint(4000, 6000, size=(100000, 1, N))[:, 0, :]
    block4 = np.random.randint(6000, 8000, size=(100000, 1, N))[:, 0, :]
    block5 = np.random.randint(8000, 10000, size=(100000, 1, N))[:, 0, :]
    XMat = np.vstack((block1, block2, block3, block4, block5))
    print(block1[0])
    print(len(block1))
    '''

    final_data, recon_mat, pca_n = pca(XMat)
    plot_best_fit(final_data, recon_mat)  # 输出前两维切片检查效果
    print('降维到：', pca_n)
