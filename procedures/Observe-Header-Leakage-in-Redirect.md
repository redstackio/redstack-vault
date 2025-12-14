---
tags:
  - observation
  - leakage
  - verification
  - undici
type: procedure
tools:
  - '[[tools/undici]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/undici-redirect-test]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:29:28.372Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 55585888-02ae-45ab-ab9d-2c33f9bd4d22
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Observe-Header-Leakage-in-Redirect

## Summary

This procedure monitors the response and incoming requests on the attacker-controlled server to confirm that the Proxy-Authorization header is leaked during the cross-domain redirect, while other headers like authorization and cookie are cleared.

## Description

After executing the undici request, inspect the logs on the attacker server (e.g., at http://attacker.com:8182/vvv) to verify header presence. This step validates the information disclosure vulnerability in undici v6.5.0, showing how proxy credentials can be exfiltrated to third-party sites via redirects.

## Requirements

1. Attacker server (e.g., simple Node.js or Python server) listening on port 8182
2. Logging enabled on the server to capture request headers
3. Execution of the prior request procedure
4. Tools like Wireshark or server logs for inspection

## Defense

Defensive measures and detection strategies:

- Implement server-side logging of incoming headers to detect anomalies
- Use WAF rules to block requests with unexpected Proxy-Authorization headers
- Audit client-side HTTP libraries for redirect behaviors
- Educate developers on header management in redirects

## Objectives

1. Capture the final redirected request
2. Verify selective header clearing
3. Confirm credential leakage potential

## Instructions

### Step 1: Monitor Attacker Server

**Context**: Set up logging on the attacker endpoint to capture incoming requests.

For a simple Node.js server:

```javascript
const http = require('http');
const server = http.createServer((req, res) => {
  console.log('Headers:', req.headers);
  res.end('Captured');
});
server.listen(8182);
```

> Run this on attacker.com to log all headers from incoming requests.

### Step 2: Trigger and Observe

**Context**: Run the request and check logs for header presence.

Execute [[commands/undici-redirect-test]] from the previous procedure, then review server console.

> Expected: Logs show 'Proxy-Authorization': 'xxxxxxxx', but no 'autHorization' or 'coOkie'. Status code 200 on response.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/undici-redirect-test]]

## Tools Used

- [[tools/undici]]

## Tags

- [[observation]]
- [[leakage]]
