---
id: proc-002
tags:
  - deserialization
  - file-read
  - http-request
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:49.754Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-DNN-Cookie-Deserialization-for-File-Read

## Summary

This procedure sends an HTTP request with a malicious DNNPersonalization cookie to trigger unsafe deserialization on a vulnerable DotNetNuke instance, resulting in remote file read.

## Description

By requesting a non-existent path like /__, DNN processes the 404 and deserializes the cookie, allowing arbitrary object creation via XML gadgets. This leads to FileSystemUtils.WriteFile execution, echoing file contents in the response. Requires the payload from the generation procedure and tools like curl.

## Requirements

1. Generated XML payload from YSoSerial.net
2. Network access to target (e.g., lonidoor.mtn.ci)
3. HTTP client like curl or Burp Suite

## Defense

Defensive measures and detection strategies:

- Implement cookie size limits and content validation
- Log and alert on 404 requests with large cookies
- Patch DNN to version 9.3.1+ or apply deserialization fixes

## Objectives

1. Trigger RCE via cookie deserialization
2. Retrieve sensitive file contents
3. Confirm vulnerability exploitation

## Instructions

### Step 1: Craft and Send the Malicious Request

**Context**: Insert the XML payload into the cookie and send to trigger 404 handling.

**Command** (curl-send-malicious-cookie):
```bash
curl -H "Cookie: DNNPersonalization=<XML_PAYLOAD>" http://lonidoor.mtn.ci/__
```

> Replace <XML_PAYLOAD> with generated XML. Expected: File contents in response body if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- deserialization
- rce
- web-exploit
