# EasyPost Python Demo

This is a demo using the EasyPost API in order to receive different rates on parcel shipping.

Before running, make sure you install easypost via pip with:

```bash
pip install easypost
```

Also, make sure to input your own API key at the top.

```bash
# findrates.py
import easypost
easypost.api_key = "API_KEY"
```