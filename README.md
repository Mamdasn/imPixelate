[![PyPI Latest Release](https://img.shields.io/pypi/v/imPixelate.svg)](https://pypi.org/project/imPixelate/)
[![Package Status](https://img.shields.io/pypi/status/imPixelate.svg)](https://pypi.org/project/imPixelate/)
[![Downloads](https://pepy.tech/badge/imPixelate)](https://pepy.tech/project/imPixelate)
[![License](https://img.shields.io/pypi/l/imPixelate.svg)](https://github.com/Mamdasn/imPixelate/blob/main/LICENSE)
![Repository Size](https://img.shields.io/github/languages/code-size/mamdasn/imPixelate)


# ImPixelate
This snippet of code attempts to pixelate images.

## Installation

Run the following to install:

```python
pip install imPixelate
```

## Usage
```python
import cv2, os
import numpy as np
from imPixelate import pix

img_fullname = "assets/lotus.jpg"
img_name, img_ext = os.path.splitext(img_fullname)
 
img = cv2.imread(img_fullname)
img_out = img.copy()

[h, w, d] = img.shape
for i in range(d):
    img_out[:, :, i] = pix(img[:, :, i].copy())
cv2.imwrite(f'{img_name}-pixelate{img_ext}', img_out)
```

## Output
This is a sample image:  
![lotus.jpg](https://raw.githubusercontent.com/Mamdasn/imPixelate/main/assets/lotus.jpg "lotus.jpg")  
This is the sample image pixelated:  
![lotus-pixelate.jpg](https://raw.githubusercontent.com/Mamdasn/imPixelate/main/assets/lotus-pixelate.jpg "lotus-pixelate.jpg")  
