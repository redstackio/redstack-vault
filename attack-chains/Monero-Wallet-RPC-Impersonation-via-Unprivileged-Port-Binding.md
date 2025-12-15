---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - monero
  - rpc
  - impersonation
  - wallet
  - cryptocurrency
  - mitm
  - port-binding
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Gain-Non-Privileged-Access-and-Run-Malicious-Process]]'
  - '[[procedures/Start-Fake-RPC-Server-on-Monero-Port]]'
  - '[[procedures/Prevent-Legitimate-RPC-Server-Startup]]'
  - '[[procedures/Intercept-Client-Commands-via-Fake-Server]]'
step_count: 4
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-14T17:29:10.129Z'
description: >-
  An unprivileged attacker on the victim's machine binds to the Monero wallet
  RPC port to impersonate the server, intercepting client commands and enabling
  unauthorized wallet creation without credentials.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Registry Run Keys - Startup Folder]]'
---
# Monero Wallet RPC Impersonation via Unprivileged Port Binding

Multi-stage attack chain demonstrating how an unprivileged attacker can hijack the Monero wallet RPC interface to impersonate the legitimate server, capture sensitive commands, and create unauthorized wallets.

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
    A[Initial Access: Run Malicious Process] --> B[Execution: Start Fake Server]
    B --> C[Defense Evasion: Block Legitimate Server]
    C --> D[Collection: Intercept Commands]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in OS features for process management)

### Target Environment

- Monero wallet application with RPC interface enabled on user-specified port (default often 18081)
- Platforms: Linux, macOS, Windows
- Services: Monero RPC server (monero-wallet-rpc)
- Tech stack: HTTP digest authentication without TLS

### Initial Access Requirements

- Unprivileged user access to the victim's machine (e.g., shared account, remote login)
- Knowledge of the RPC port configured in the victim's monero-wallet-rpc setup
- No elevated privileges required

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Gain-Non-Privileged-Access-and-Run-Malicious-Process]]

**Objective**: Establish a persistent malicious process on the victim's machine as an unprivileged user to prepare for port hijacking.

**Instructions**: Log in as a non-privileged user, start a background process (e.g., a simple script or netcat listener), and ensure it persists after logout.

On Linux/macOS:
```bash
nohup ./malicious_process &
```
On Windows:
Use Task Scheduler or fast user switching to keep the session active.

**Expected Output**: Process running in background, verifiable via `ps aux` (Linux/macOS) or Task Manager (Windows).

**Success Indicators**:
- Process ID visible in process list
- Process survives logout or session switch

### Step 2: Execution
procedure: [[procedures/Start-Fake-RPC-Server-on-Monero-Port]]

**Objective**: Bind a fake server to the Monero RPC port to impersonate the legitimate service.

**Instructions**: Implement and launch a fake HTTP server that listens on the victim-specified RPC port (e.g., 18081) and handles digest auth challenges without verifying its own identity.

Example using Python (simple HTTP server script):
```bash
python3 -m http.server 18081 --bind 127.0.0.1
```
(Adapt to respond to digest auth and log requests.)

**Expected Output**: Server binds successfully to the port, logs show binding confirmation.

**Success Indicators**:
- `netstat -tuln | grep 18081` shows the fake process listening
- No binding errors

### Step 3: Defense Evasion
procedure: [[procedures/Prevent-Legitimate-RPC-Server-Startup]]

**Objective**: Ensure the victim's attempt to start the real monero-wallet-rpc fails silently due to port occupation.

**Instructions**: With the fake server running, the victim launches monero-wallet-rpc, which will fail to bind. If auto-started (e.g., via service), no GUI notification may appear.

Monitor for failure:
```bash
# Victim runs: monero-wallet-rpc --rpc-bind-port 18081 --wallet-file wallet
# Expected error: "Error starting RPC server: Failed to bind to 0.0.0.0:18081"
```

**Expected Output**: Legitimate executable exits with bind error; victim may not notice if backgrounded.

**Success Indicators**:
- Port remains occupied by fake server
- No new process for monero-wallet-rpc

### Step 4: Collection
procedure: [[procedures/Intercept-Client-Commands-via-Fake-Server]]

**Objective**: Capture RPC commands from the victim's client, such as wallet creation, to gain unauthorized control.

**Instructions**: Victim's client connects to localhost:18081, authenticates via HTTP digest (MD5 hash of username:password:nonce:method:URI), and sends commands. Fake server challenges auth but logs requests.

Intercept example command [[commands/create-wallet-rpc]]:
```json
{"method":"create_wallet","params":{"filename":"/path/to/new_wallet","password":"pass"}}
```

**Expected Output**: Fake server logs the full request, including params; attacker uses them to create and access the wallet.

**Success Indicators**:
- Captured commands in fake server logs
- New wallet created under attacker control

## Attack Chain Summary

### Key Achievements

1. Persistent unprivileged access without detection
2. Successful RPC server impersonation via port hijacking
3. Interception of sensitive wallet operations like account creation
4. Unauthorized control over new Monero wallets without credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (impersonating RPC server via lack of server auth)
- [[Registry Run Keys - Startup Folder]] Registry Run Keys / Startup Folder (persisting malicious process)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access (unprivileged user login)
- [[Execution]] Execution (running fake server process)
- [[Defense Evasion]] Defense Evasion (port binding to block legitimate service)

---
*Last updated: 2023-10-01T00:00:00Z*
