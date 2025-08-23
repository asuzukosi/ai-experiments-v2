from setuptools import setup, find_packages

setup(
    name="vae",
    version="0.1.0",
    description="VAE implementation for deep learning study",
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
