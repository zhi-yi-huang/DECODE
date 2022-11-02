# Evaluation script for task 1 and 2

We provide the evaluation script for task 1 and 2, which is the same to what we will use
for public/private leaderboard. This script can be used to help the local development.

## Evaluation for task 1

The submission file should be a `npy` file with shape either `[5, 50, 50]` or `[5, s, 50, 50]`, where 
`s` is the batch size of the adjacency matrix. For evaluation, run the following:
```bash
python -m starting_kit.evaluation.evaluate --input_file <file path to the submission> --ground_truth <file path to the ground truth> --score_dir <output dir for score files> --evaluate_adjacency --summarise
```
where enabling`--summarise` will output a single score that is the same to the one used for ranking in the leaderborad, disabling it will output
the detailed score for each dataset.

## Evaluation for task 2

The submission file should be a `npy` file with shape `[5,10]`. For evaluation, run the following:

```bash
python -m starting_kit.evaluation.evaluate --input_file <file path to the submission> --ground_truth <file path to the ground truth> --score_dir <output dir for score files> --evaluate_cate --summarise
```
where enabling `--summarise` has the same effect as in task 1 evaluation.
