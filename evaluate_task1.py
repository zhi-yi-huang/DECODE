import numpy as np
from evaluation.adjacency_utils import edge_prediction_metrics

if __name__ == '__main__':
    dataset_parameters = ["local_dev"]
    dataset_num = 5
    for dataset_parameter in dataset_parameters:
        adj_matrix_perd = np.load(f"output/Task_1_data_{dataset_parameter}_decode_result/adj_matrix.npy").astype(int)
        adj_matrix_truth = np.load(f"data/Task_1_data_{dataset_parameter}_csv/adj_matrix.npy").astype(int)
        for dataset_id in range(dataset_num):
            result = edge_prediction_metrics(adj_matrix_truth[dataset_id, :, :], adj_matrix_perd[dataset_id, :, :])
            with open(f"output/Task_1_data_{dataset_parameter}_decode_result/metrics_dataset_{dataset_id}.txt", 'w') as f:
                for key, value in result.items():
                    f.write('%s:%s\n' % (key, value))