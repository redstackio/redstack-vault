---
id: proc-lichess-exploit-001
tags:
  - ssrf
  - poc
  - exploit
  - aws
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-lichess-ssrf-poc]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.705Z'
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
# Craft-and-Execute-Lichess-SSRF-POC-Request

## Summary

This procedure crafts and sends a proof-of-concept request to Lichess's vulnerable game export API, using the 'players' parameter to force SSRF against internal endpoints like AWS instance metadata.

## Description

The SSRF arises from the 'players' parameter being passed unchecked to an HTTP client in the Scala backend. Attackers craft URLs pointing to sensitive internal resources (e.g., http://169.254.169.254/latest/meta-data/), send via public endpoints, and potentially exfiltrate credentials or scan networks. No authentication is needed, making it highly abusable.

## Requirements

1. Valid Lichess game ID or username (publicly available)
2. curl or similar HTTP client
3. Target internal URL (e.g., AWS metadata)

## Defense

Defensive measures and detection strategies:

- Validate and allowlist URLs in 'players' parameter (block private IPs)
- Use network segmentation to isolate backend from metadata services
- Monitor server logs for outbound requests to internal/cloud endpoints

## Objectives

1. Trigger server-side request to arbitrary URL
2. Bypass IP restrictions on internal services
3. Access sensitive data like AWS IAM credentials

## Instructions

### Step 1: Select Target and Endpoint

**Context**: Choose a vulnerable endpoint and internal target URL.

Use /game/export/[GAME_ID] and http://169.254.169.254/latest/meta-data/ for AWS.

### Step 2: Craft the Request

**Context**: Build the malicious query.

Construct: https://lichess.org/game/export/[GAME_ID]?players=[INTERNAL_URL]

### Step 3: Execute the POC

**Context**: Send the request to exploit SSRF.

**Command** ([[commands/curl-lichess-ssrf-poc]]):
```bash
curl "https://lichess.org/game/export/[GAME_ID]?players=http://169.254.169.254/latest/meta-data/" -v
```

> Replace [GAME_ID] with a real ID. Expected output: Server processes request, fetches metadata internally.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-lichess-ssrf-poc]]

## Tools Used


## Tags

- ssrf
- exploit
- aws
