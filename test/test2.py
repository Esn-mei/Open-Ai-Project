from __future__ import annotations
import platform, sys
import torch

BYTES_PER_GIB = 1024**3
def format_gib(byte_count: int) -> str:
    return f"{byte_count / BYTES_PER_GIB:.2f} GiB"
def print_environment() -> None:
    print("=" * 60)
    print("PyTorch CUDA Environment Report")
    print("=" * 60)
    print(f"Python version:      {sys.version.split()[0]}")
    print(f"Operating system:    {platform.platform()}")
    print(f"PyTorch version:     {torch.__version__}")
    print(f"PyTorch CUDA build:  {torch.version.cuda or 'CPU-only build'}")
    print(f"cuDNN version:       {torch.backends.cudnn.version() or 'Not available'}")
    print(f"CUDA available:      {torch.cuda.is_available()}")
def print_gpu_details(device_index: int) -> None:
    properties = torch.cuda.get_device_properties(device_index)
    total_memory = properties.total_memory
    allocated_memory = torch.cuda.memory_allocated(device_index)
    reserved_memory = torch.cuda.memory_reserved(device_index)
    free_memory = max(total_memory - allocated_memory, 0)
    usage_percent = allocated_memory / total_memory * 100 if total_memory else 0
    print(f"\n--- GPU {device_index}: {properties.name} ---")
    print(f"Compute capability:  {properties.major}.{properties.minor}")
    print(f"Total memory:        {format_gib(total_memory)}")
    print(f"Allocated memory:    {format_gib(allocated_memory)} ({usage_percent:.1f}%)")
    print(f"Reserved memory:     {format_gib(reserved_memory)}")
    print(f"Estimated free:      {format_gib(free_memory)}")
    print(f"Multiprocessors:     {properties.multi_processor_count}")
def main() -> None:
    print_environment()
    if not torch.cuda.is_available():
        print("\nNo CUDA-capable GPU is available to this PyTorch installation.")
        print("Check the NVIDIA driver, CUDA-compatible PyTorch package, and device access.")
        return
    device_count = torch.cuda.device_count()
    current_device = torch.cuda.current_device()
    print(f"CUDA device count:   {device_count}")
    print(f"Current device:      GPU {current_device}")
    for device_index in range(device_count):
        try:
            print_gpu_details(device_index)
        except RuntimeError as error:
            print(f"\n--- GPU {device_index} ---")
            print(f"Unable to read device details: {error}")
    print("\nGPU check completed.")
if __name__ == "__main__":
    main()
print("nihao")