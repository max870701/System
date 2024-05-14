import pickle


def save_tree(tree, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(tree, file)

def load_tree(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)