# path_config.py
from pathlib import Path

# Automatically locate the project root: RL-BERT-Opinion
def find_project_root(target_name="RL-BERT-Opinion"):
    current = Path().resolve()
    while current.name != target_name:
        if current.parent == current:
            raise RuntimeError(f"Cannot locate project root: {target_name}")
        current = current.parent
    return current

# Set project root
PROJECT_ROOT = find_project_root()

# Subfolders
DATASET_DIR = PROJECT_ROOT / "Dataset"
MODEL_DIR   = PROJECT_ROOT / "Model"
LOGS_DIR    = PROJECT_ROOT / "Logs"
CODE_DIR    = PROJECT_ROOT / "Code"

# BERT Model Path
BERT_MODEL_PATH = MODEL_DIR / "sentiment_bert"

# Debug print
if __name__ == "__main__":
    print("Project root:", PROJECT_ROOT)
    print("Dataset path:", DATASET_DIR)
    print("Model path:", MODEL_DIR)
    print("Logs path:", LOGS_DIR)
    print("BERT model:", BERT_MODEL_PATH)
