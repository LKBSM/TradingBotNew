#!/bin/bash
pip install --no-cache-dir torch==2.5.0+cpu torchvision==0.20.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
pip install --no-cache-dir stable-baselines3==2.0.0
pip install --no-cache-dir gymnasium==0.28.1
pip install --no-cache-dir numpy pandas scipy ta scikit-learn matplotlib rich pydantic python-dotenv gdown requests boto3
