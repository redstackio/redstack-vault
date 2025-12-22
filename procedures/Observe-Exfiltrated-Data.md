---
tags:
  - exfiltration
  - xxe
type: procedure
tools:
  - '[[tools/Sinatra]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Data from Cloud Storage]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: de1f6131-a88a-489f-80ee-50280f1d762c
created_at: '2025-12-13T09:00:27.298Z'
updated_at: '2025-12-13T09:00:27.298Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Observe Exfiltrated Data

## Summary

This procedure involves monitoring the attacker server's logs to capture and view data exfiltrated via XXE out-of-band requests.

## Description

Once the crawler parses the malicious sitemap, it sends file contents (e.g., /etc/hostname) as query parameters to the /exfil endpoint. The attacker observes these in server logs, confirming successful exploitation and data leakage.

## Requirements

1. Running attacker server
2. Active crawl from target
3. Console access to server logs

## Defense

Defensive measures and detection strategies:

- Implement network monitoring for anomalous outbound traffic
- Use WAF to block suspicious XML payloads

## Objectives

1. Confirm XXE exploitation
2. Collect leaked sensitive information
3. Assess impact

## Instructions

### Step 1: Monitor Server Logs

**Context**: Check for incoming exfil requests.

Observe the Sinatra server console for requests to /exfil with query parameters containing file data.

> No specific command; log observation.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Cloud Storage]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Sinatra]]

## Tags

- [[Exfiltration]]
- [[xxe]]
