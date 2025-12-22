---
id: e72945df-2a9e-4075-8735-ccaa8a3f1798
name: 2FA-Success-JSON-Response
type: code
language: json
verified: true
created_at: '2023-04-06T03:55:53.922577+00:00'
updated_at: '2023-04-06T03:55:53.932176+00:00'
platforms:
  - Web
tags:
  - 2fa
  - response
  - json
validated: true
---

# 2FA-Success-JSON-Response

## Code

```json
{"success": true}
```

## Description

This JSON snippet is the modified version of the 2FA response, changed from failure to success to trick the client application into granting access. It is crafted during the interception phase of the bypass procedure.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| success | Boolean flag for authentication status | true |

## Usage

In a MITM setup, replace the original failed response with this snippet before forwarding to the client. This enables account takeover without valid 2FA credentials. Ensure other response fields (e.g., tokens) are preserved.

## Detection

- Server-side logging of 2FA validations to detect unauthorized success responses.
- Anomaly detection on login patterns where success follows multiple failures.
- Use signed responses to prevent tampering.

## Related

- [[procedures/2FA-Bypass-via-Response-Manipulation]]
- [[tools/Burp-Suite]]
