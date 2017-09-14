#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
image = Image.open("E:\\validcode.png")
vcode = pytesseract.image_to_string(image)
print(vcode)