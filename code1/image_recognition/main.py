import torch

print("1. CUDA 是否对 PyTorch 可见:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("2. 识别到的可用 GPU 数量:", torch.cuda.device_count())
    print("3. 当前挂载的具体显卡型号:", torch.cuda.get_device_name(0))
    print("4. 当前设备正处于的算力架构版本:", torch.cuda.get_device_capability(0))
else:
    print("环境崩塌：你的 PyTorch 安装的完全是 CPU 阉割版，或者显卡驱动/CUDA Toolkit 未正确配置！")
