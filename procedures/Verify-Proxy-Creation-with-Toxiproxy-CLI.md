---
tags:
  - verification
  - cli
  - inspect
type: procedure
tools:
  - '[[tools/toxiproxy-cli]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/toxiproxy-cli-inspect-csrf]]'
platforms:
  - macOS
techniques:
  - '[[System Information Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 38a33eef-2f45-462a-a344-84baab2113ab
created_at: '2025-12-14T17:27:29.725Z'
updated_at: '2025-12-14T17:27:29.725Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Verify-Proxy-Creation-with-Toxiproxy-CLI

## Summary

This procedure uses the Toxiproxy CLI to inspect a newly created proxy, confirming its configuration after CSRF exploitation, including listen port, upstream target, and enabled status.

## Description

Post-CSRF creation, the attacker or victim can verify the proxy's state via the CLI or direct access. This step validates the attack's success in a controlled environment. It targets the local Toxiproxy instance and assumes the CLI is installed alongside the server.

## Requirements

1. Toxiproxy CLI installed
2. Proxy named 'csrf' created
3. Local access to the machine

## Defense

Defensive measures and detection strategies:

- Log CLI usage and API inspections
- Alert on unexpected proxy inspections
- Disable CLI if not needed in production

## Objectives

1. Confirm proxy existence and config
2. Identify any misconfigurations
3. Validate upstream routing

## Instructions

### Step 1: Inspect Proxy

**Context**: Query the Toxiproxy API via CLI to retrieve details of the 'csrf' proxy.

**Command** ([[commands/toxiproxy-cli-inspect-csrf]]):
```bash
toxiproxy-cli inspect csrf
```

> Displays JSON-like output with proxy attributes. Expected output includes name, listen (0.0.0.0:2773), upstream (attacker-server:9999), and toxics array.

### Step 2: Test Connectivity

**Context**: Optionally, curl the proxy endpoint to verify traffic flow.

No specific command; use curl:

```bash
curl http://127.0.0.1:2773/
```

> Should route to upstream or return error if not connected.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/toxiproxy-cli-inspect-csrf]]

## Tools Used

- [[tools/toxiproxy-cli]]

## Tags

- verification
- cli
- inspect
