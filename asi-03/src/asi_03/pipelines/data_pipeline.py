from kedro.pipeline import Pipeline, node
from .loading import loadData
from .preprocesing import process_and_split
from .training import train

load_node = node(
    loadData,
    inputs=[],
    outputs="intermediate_data",
    name="load_node"
)

preprocess_node = node(
    process_and_split,
    inputs="intermediate_data",
    outputs=["train_X", "train_Y", "test_X", "test_Y", "val_X", "val_Y"],
    name="preprocess_node"
)

train_node = node(
    train,
    inputs={
        "train_X": "train_X",
        "train_Y": "train_Y",
        "test_X": "test_X",
        "test_Y": "test_Y",
        "val_X": "val_X",
        "val_Y": "val_Y",
        "model_params": "params:model_params"
    },
    outputs="model_output",
    name="train_node"
)

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            load_node,
            preprocess_node,
            train_node
        ]
    )