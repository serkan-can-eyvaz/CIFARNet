import torch

if torch.cuda.is_available():
    print("GPU aktif ve kullanılabilir!")
    print(f"GPU ismi: {torch.cuda.get_device_name(0)}")
else:
    print("GPU kullanılabilir değil.")
