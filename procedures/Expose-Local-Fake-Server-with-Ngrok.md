---
tags:
  - ngrok
  - port-exposure
  - tunneling
type: procedure
tools:
  - '[[tools/fake_server.py]]'
  - '[[tools/Flask]]'
  - '[[tools/Browser-Console]]'
  - '[[tools/Digest::SHA2]]'
  - '[[tools/Git]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ca7fd66f-8a6c-4f43-9328-d4b967e0b138
created_at: '2025-12-11T03:47:59.551Z'
updated_at: '2025-12-11T03:47:59.551Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Expose Local Fake Server with Ngrok

## Summary

This procedure uses ngrok to expose a local fake server to the internet, allowing it to be used in GitLab's remote import feature.

## Description

Ngrok creates a public tunnel to the local port, providing a URL that can be entered into GitLab's import interface. This is essential for remote exploitation where the fake server isn't directly accessible.

## Requirements

1. Ngrok installed and authenticated
2. Local server running on port 5000
3. Internet access

## Defense

Defensive measures and detection strategies:

- Block known tunneling services like ngrok in network policies
- Validate import URLs against allowlists

## Objectives

1. Obtain a public URL for the fake server
2. Enable remote interaction with GitLab
3. Facilitate the import exploit

## Instructions

### Step 1: Start Ngrok Tunnel

**Context**: Expose the local port 5000.

**Command** ([[commands/ngrok-expose-local-port]]):
```bash
ngrok http 5000
```

> This generates a public URL like https://abc123.ngrok.io.

### Step 2: Verify Accessibility

**Context**: Test the tunnel.

Access the ngrok URL in a browser to confirm it proxies to the fake server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/ngrok-expose-local-port]]

## Tools Used

- #ngrok

## Tags

- #ngrok
- #port-exposure
- #tunneling
