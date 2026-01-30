import os

def list_models(folder="models"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    return [f for f in os.listdir(folder) if f.lower().endswith(".pt")]
