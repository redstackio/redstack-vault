---
id: 24a0d39e-802d-4be6-bc2b-f3e26d2e5686
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:08.938941+00:00'
updated_at: '2023-04-10T20:20:58.743576+00:00'
---

# Code Snippet 24a0d39e

**Language**: Powershell

```powershell
$ git clone https://github.com/nccgroup/s3_objects_check
$ python3 -m venv env && source env/bin/activate
$ pip install -r requirements.txt
$ python s3-objects-check.py -h
$ python s3-objects-check.py -p whitebox-profile -e blackbox-profile
```
