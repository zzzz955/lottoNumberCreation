import pandas as pd
import openpyxl


def prize_solution(file_path, nums, order, is_bonus):
    num_list = []
    df = pd.read_excel(file_path, na_values=False, engine='openpyxl')
    if is_bonus:
        selected_columns = df.iloc[:, 1:8]
    else:
        selected_columns = df.iloc[:, 1:7]
    counts = {}
    for col in selected_columns.columns:
        counts[col] = selected_columns[col].value_counts()
    result_df = pd.DataFrame(counts, index=range(1, 46)).fillna(0).astype(int)
    result_df = result_df.apply(lambda row: row.sum(), axis=1).sort_values(ascending=order)
    for i in range(nums):
        num_list.append(result_df.index[i])
    return num_list

