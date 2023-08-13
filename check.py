import torch

# Check if CUDA is available
if not torch.cuda.is_available():
    print('CUDA is not available.')
else:
    print('CUDA is available.')

    # Get the current default CUDA device
    current_device = torch.cuda.current_device()

    # Get the name of the current default CUDA device
    device_name = torch.cuda.get_device_name(current_device)

    print('Current CUDA device:', current_device)
    print('Device name:', device_name)

