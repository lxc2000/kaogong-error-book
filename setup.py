#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="kaogong-error-book",
    version="0.1.0",
    author="养虾哥",
    description="考公错题本 - 轻量级错题管理工具",
    py_modules=["exam_book"],
    entry_points={
        "console_scripts": [
            "exam-book=exam_book:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
