from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os,sys
from typing import Optional
import numpy as np
load_dotenv(find_dotenv())
def get_key(name: str, default: Optional[str]= None) -> Optional[str]:
    return os.getenv(name, default)
API_KEY = os.getenv("API_KEY")
if API_KEY != None:
    print(np.array([1,7,8,9]))