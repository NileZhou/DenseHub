from datasets import load_dataset, Dataset, DatasetDict
import os


def slice_and_save_dataset(dataset_path, save_dir, n=1000):
    full_ds = load_dataset(dataset_path)
    os.makedirs(save_dir, exist_ok=True)

    # 统一保存为 split.parquet 格式（即使单split）
    if isinstance(full_ds, DatasetDict):
        sliced_ds = DatasetDict()
        for split in full_ds:
            subset = full_ds[split].select(range(min(n, len(full_ds[split]))))
            subset.to_parquet(f"{save_dir}/{split}.parquet")  # 关键命名规范
            sliced_ds[split] = subset
    else:
        # 单split数据集统一保存为 train.parquet
        sliced_ds = full_ds.select(range(min(n, len(full_ds))))
        sliced_ds.to_parquet(f"{save_dir}/train.parquet")  # 强制命名为train

    return sliced_ds

def load_sliced_dataset(save_dir):
    return load_dataset("parquet", data_dir=save_dir) 


if __name__ == "__main__":
    ori_ds_path = '/njfs/train-nlp/x/datasets/cache/open-r1___open_r1-math-220k/default/0.0.0/e4e141ec9dea9f8326f4d347be56105859b2bd68'
    save_ds_path = '/njfs/train-nlp/x/datasets/cache/open_r1-math-224'
    sliced_ds = slice_and_save_dataset(ori_ds_path, save_ds_path, n=56*4)
    sliced_ds = load_sliced_dataset(save_ds_path)
    print(sliced_ds)
    
