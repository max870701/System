import pandas as pd
from CustomTree import Tree
from SaveAndLoadTree import save_tree, load_tree
from MaxHeapTree import MaxHeapTree
from sklearn.metrics import classification_report


if __name__ == '__main__':
    drive_path = '/content/drive/MyDrive/ISE-244'
    review_data_csv = 'raw_review_Electronics.csv'
    meta_data_csv = 'raw_meta_Electronics.csv'

    review_iterator = pd.read_csv(f'{drive_path}/{review_data_csv}', iterator=True, chunksize=1000)
    meta_iterator = pd.read_csv(f'{drive_path}/{meta_data_csv}', iterator=True, chunksize=1000)

    meta_df = next(meta_iterator)
    review_df = next(review_iterator)

    custom_tree = Tree()
    max_heap_tree = MaxHeapTree()


    if isinstance(meta_df['categories'].iloc[0], str):
        meta_df['categories'] = meta_df['categories'].apply(eval)

    for index, row in meta_df.iterrows():
        custom_tree.add_path(row['main_category'], row['categories'])
        max_heap_tree.insert(row['main_category'])
    
    for df in review_df.iterrows():
        all_review_df = pd.concat(df)

    save_tree(custom_tree, f'{drive_path}/category_tree.pkl')
    save_tree(max_heap_tree, f'{drive_path}/max_heap_tree.pkl')

    # Load
    loaded_custom_tree = load_tree(f'{drive_path}/category_tree.pkl')
    loaded_max_heap_tree = load_tree(f'{drive_path}/max_heap_tree.pkl')

    # Apply the trees to the review data
    custom_tree_predictions = all_review_df['reviewText'].apply(loaded_custom_tree.predict)
    max_heap_tree_predictions = all_review_df['reviewText'].apply(loaded_max_heap_tree.predict)

    # Print the classification report for the custom tree
    print("Custom Tree Performance:")
    print(classification_report(review_df['main_category'], custom_tree_predictions))

    # Print the classification report for the max heap tree
    print("Max Heap Tree Performance:")
    print(classification_report(review_df['main_category'], max_heap_tree_predictions))

