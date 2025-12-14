---
tags:
  - vulnerable-setup
  - proxy
  - curl
type: procedure
tools:
  - '[[tools/Python]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/set-ipfs-gateway-env]]'
  - '[[commands/start-vulnerable-proxy]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.415Z'
sub_techniques: []
id: 26e736d5-f467-40c6-b3d4-2250a2eddee1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure and Start Vulnerable curl IPFS Proxy

## Summary

This procedure configures and launches a proxy service that uses curl's vulnerable ipfs_url_rewrite() to process IPFS URLs, enabling SSRF demonstration by forwarding to a configured gateway without validation.

## Description

The proxy listens on port 9000, decodes the CID from ipfs:// URLs using CURLU_URLDECODE, concatenates it into the gateway path via aprintf, and fetches with libcurl. This allows path traversal like '..%2F..' to escape /ipfs/. Requires Python and vulnerable_proxy.py script; assumes curl 8.16.1-DEV or similar.

## Requirements

1. Python 3 and curl installed
2. Port 9000 available
3. vulnerable_proxy.py script implementing the flawed rewrite
4. IPFS_GATEWAY env var set to simulated gateway

## Defense

Defensive measures and detection strategies:

- Validate and normalize all URL components before concatenation
- Use whitelisting for allowed paths in URL rewriters
- Monitor for anomalous internal requests from proxies

## Objectives

1. Establish victim service mimicking curl IPFS handling
2. Enable processing of malicious URLs
3. Log rewritten URLs for analysis

## Instructions

### Step 1: Set Gateway Environment

**Context**: Configure the proxy to point to the simulated internal gateway.

**Command** ([[commands/set-ipfs-gateway-env]]):
```bash
export IPFS_GATEWAY="http://127.0.0.1:5001/"
```

> Sets the env var for the gateway URL. Expected output: None (shell confirmation).

### Step 2: Start the Proxy Server

**Context**: Launch the proxy to listen for IPFS URL requests and rewrite them vulnerably.

**Command** ([[commands/start-vulnerable-proxy]]):
```bash
python3 vulnerable_proxy.py
```

> Starts server on 0.0.0.0:9000, using curl to fetch rewritten paths. Expected output: "Vulnerable proxy listening on 0.0.0.0:9000" and logs of processed URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/set-ipfs-gateway-env]]
- [[commands/start-vulnerable-proxy]]

## Tools Used

- [[tools/Python]]
- [[tools/curl]]

## Tags

- vulnerable-setup
- proxy
- curl
