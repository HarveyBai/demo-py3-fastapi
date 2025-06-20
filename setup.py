from setuptools import setup, find_packages

setup(
    name="demo_py3_fastapi",
    version="0.1",
    package_dir={"": "src"},  # 指定src为包根目录
    packages=find_packages(where="src"),
)
