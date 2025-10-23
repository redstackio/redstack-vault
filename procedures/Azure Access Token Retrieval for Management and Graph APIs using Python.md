---
id: 4e9675f4-b3b8-4f76-8094-61818aad47c5
name: Azure Access Token Retrieval for Management and Graph APIs using Python
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.226533+00:00'
updated_at: '2023-05-24T16:06:01.998528+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
platforms:
- Cloud
- Web
tags:
- '[[Azure API via Python Version]]'
- '[[Cloud - Azure]]'
- '[[Python]]'
- '[[Token from Managed Identity]]'
---

# Azure Access Token Retrieval for Management and Graph APIs using Python

**Status**: ✓ Verified

## Summary

This procedure demonstrates how to retrieve access tokens for the  Management API and Graph API using cURL commands within a Python script.  It utilizes environment variables, specifically IDENTITY_ENDPOINT and IDENTITY_HEADER,  to construct the cURL commands and obtain the access tokens. By  follo

## Description

# Description

This procedure demonstrates how to retrieve access tokens for the  Management API and Graph API using cURL commands within a Python script.  It utilizes environment variables, specifically `IDENTITY_ENDPOINT` and `IDENTITY_HEADER`,  to construct the cURL commands and obtain the access tokens. By  following these steps, you can obtain the access tokens and  corresponding client ID or account ID for both the Management API and  Graph API.

 

## Requirements

To successfully execute this procedure, ensure the following prerequisites:

- Python is installed and accessible.

- cURL is installed and accessible.

- Environment variables `IDENTITY_ENDPOINT` and `IDENTITY_HEADER` are set with the appropriate values.

- Proper permissions are granted to access the Management API and Graph API.

 

## Defense

1. Ensure that Managed Identities are only assigned the necessary permissions

1. Regularly rotate the access keys for Managed Identities

1. Monitor for any unauthorized access to Azure APIs via Managed Identities

 

## Objectives

1. Retrieve an access token from a Managed Identity in Azure

1. Use the access token to authenticate with Azure APIs via Python

1. Automate access to Azure APIs via Python scripts

 

# Instructions

1.Import the required modules, retrieve the access token for the Management API, and retrieve the access token for the Graph API.

 



**Code**: [[IDENTITY_ENDPOINT = os.environ['IDENTITY_ENDPOINT']]



> This script retrieves the access token, client ID, and account ID for the Azure Management API and Graph API. The script uses the environment variables IDENTITY_ENDPOINT and IDENTITY_HEADER to authenticate the request. The first command retrieves the access token and client ID for the Management API by making a curl request to the specified endpoint with the resource and API version parameters. The second command retrieves the access token and client ID for the Graph API by making a similar curl request with the appropriate resource parameter. The retrieved access tokens can be used to authenticate requests to the respective APIs.



2. (Optional) To use managed identity inside a Python Function, you can use the 'OS module' to retrieve the identity endpoint and header, and then use these values to authenticate your function with Azure APIs.

 



**Code**: [[import logging, os
import azure.functions as func
]]



> The above code shows an example of how to use managed identity inside a Python Function. The function retrieves the identity endpoint and header using the os module, and then uses these values to authenticate with Azure APIs. The function then executes a curl command to retrieve a resource from the Azure Management API, using the managed identity to authenticate the request. The response is returned as an HTTP response with a status code of 200.

## Platforms

- Cloud
- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Tags

- [[Azure API via Python Version]]
- [[Cloud - Azure]]
- [[Python]]
- [[Token from Managed Identity]]


