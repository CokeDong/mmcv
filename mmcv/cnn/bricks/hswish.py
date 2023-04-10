# Copyright (c) OpenMMLab. All rights reserved.
import torch
import torch.nn as nn
from mmengine.registry import MODELS
from mmengine.utils import digit_version
from mmengine.utils.dl_utils import TORCH_VERSION


class HSwish(nn.Module):
    """Hard Swish Module.

    This module applies the hard swish function:

    .. math::
        Hswish(x) = x * ReLU6(x + 3) / 6

    Args:
        inplace (bool): can optionally do the operation in-place.
            Default: False.

    Returns:
        Tensor: The output tensor.
    """

    def __init__(self, inplace: bool = False):
        super().__init__()
        self.act = nn.ReLU6(inplace)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x * self.act(x + 3) / 6


if digit_version(TORCH_VERSION) < digit_version('1.7'):
    # Hardswish is not supported when PyTorch version < 1.6.
    # And Hardswish in PyTorch 1.6 does not support inplace.
    MODELS.register_module(module=HSwish)
else:
    MODELS.register_module(module=nn.Hardswish, name='HSwish')
