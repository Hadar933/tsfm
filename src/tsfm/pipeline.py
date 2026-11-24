import pandas as pd
import numpy as np
import torch

class TSFMPipeline:
    def __init__(self):
        pass

    def fit(
        self,
        X: pd.DataFrame | np.ndarray | torch.Tensor,
        y: pd.DataFrame | np.ndarray | torch.Tensor,
    )-> "TSFMPipeline":
        pass

    def predict(
        self,
        X: pd.DataFrame | np.ndarray | torch.Tensor,
    )-> pd.DataFrame | np.ndarray | torch.Tensor:
        pass
    