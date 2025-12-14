---
id: uuid-placeholder-1
tags:
  - deserialization
  - dnn
  - 404-trigger
type: procedure
tools:
  - '[[tools/ysoserial.net]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-404]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:54.252Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger DNN Deserialization on 404 Page

## Summary

This procedure accesses a non-existent page in a DNN application to trigger the deserialization of the DNNPersonalization cookie during error handling, setting the stage for payload injection.

## Description

In vulnerable DNN versions (< 9.3.0-RC), accessing a 404 page processes the DNNPersonalization cookie using ObjectStateFormatter, which insecurely deserializes user-controlled data. This allows arbitrary object instantiation and method invocation from classes like FileSystemUtils. The target environment is a web-accessible DNN site on .NET/ASP.NET. Expected outcomes include no immediate errors and readiness for payload exploitation.

## Requirements

1. Network access to the DNN web application
2. No authentication required
3. Tools like curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Upgrade DNN to 9.3.0-RC or later
- Implement cookie validation and deserialization blacklisting
- Monitor 404 requests for anomalous cookies

## Objectives

1. Invoke the vulnerable deserialization handler
2. Confirm 404 processing without errors
3. Prepare for cookie payload injection

## Instructions

### Step 1: Send Request to Non-Existent Page

**Context**: This step triggers the 404 error handler, which deserializes the cookie if present.

**Command** ([[commands/curl-trigger-404]]):
```bash
curl -v "https://target.com/nonexistent-page" -H "User-Agent: Mozilla/5.0"
```

> This command sends a GET request to a bogus path, expecting a 404 response. Verbose output (-v) shows headers and confirms processing.

### Step 2: Verify Response

**Context**: Check for successful 404 without deserialization failures.

**Command** ([[commands/curl-trigger-404]]):
```bash
curl -s -o /dev/null -w "%{http_code}" "https://target.com/nonexistent-page"
```

> Outputs the HTTP status code; 404 indicates success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-404]]

## Tools Used

- [[tools/ysoserial.net]]

## Tags

- deserialization
- dnn
