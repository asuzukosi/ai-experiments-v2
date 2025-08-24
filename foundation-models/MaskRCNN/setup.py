from setuptools import setup, find_packages

setup(
    name="maskrcnn",
    version="0.1.0",
    description="MaskRCNN implementation for deep learning study",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=1.9.0",
        "torchvision>=0.10.0",
        "numpy",
        "matplotlib",
        "tqdm",
    ],
)
