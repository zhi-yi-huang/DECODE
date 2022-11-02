import os
import warnings

import numpy as np
import pandas as pd
from scipy.stats import rankdata


def coef(r1, r2, k):
    assert r1.ndim == 1 and r2.ndim == 1

    n1, n2 = r1.shape[0], r2.shape[0]
    assert n1 == n2

    return sum(r2[r1 > n1 - k])/k

def decode(data, ratio=0.18):
    rank = rankdata(data, method='ordinal', axis=0)

    sample_size, ndim = data.shape

    adj_matrix = np.zeros(shape=(ndim, ndim))

    k = int(sample_size * ratio)

    causal_order = []

    remain = set(range(ndim))

    for _ in range(ndim):
        cnt = np.zeros(shape=(ndim,))
        for i in remain:
            for j in remain:
                if i == j:
                    continue
                cnt[i] += coef(rank[:, i], rank[:, j], k=k)

        head = np.argmax(cnt)
        causal_order.append(head)
        remain -= {head}
        for i in remain:
            adj_matrix[i, head] = 1


    return adj_matrix, causal_order

if __name__ == '__main__':
    warnings.filterwarnings("ignore")

    dataset_num = 5
    dataset_parameters = ["local_dev", "private", "public"]

    for dataset_parameter in dataset_parameters:
        mats = []
        if not os.path.exists(f"output/Task_1_data_{dataset_parameter}_decode_result"):
            os.makedirs(f"output/Task_1_data_{dataset_parameter}_decode_result")
        for dataset_id in range(dataset_num):
            df = pd.read_csv(f"data/Task_1_data_{dataset_parameter}_csv/dataset_{dataset_id}/train.csv", header=None)
            data = df.iloc[:, 2:].to_numpy()

            adj_matrix, causal_order = decode(data)
            result = adj_matrix
            result.astype(int)
            mats.append(result)
            np.savetxt(f"output/Task_1_data_{dataset_parameter}_decode_result/dataset_{dataset_id}.txt", result, fmt="%i")
        np.save(f"output/Task_1_data_{dataset_parameter}_decode_result/adj_matrix.npy", np.stack(mats))

