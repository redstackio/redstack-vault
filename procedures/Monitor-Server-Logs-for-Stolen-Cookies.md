---
tags:
  - data-exfiltration
  - log-monitoring
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: e73ce4d5-0e64-4d5d-81a2-e561ac5c094f
created_at: '2025-12-14T00:11:16.504Z'
updated_at: '2025-12-14T00:11:16.504Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Monitor Server Logs for Stolen Cookies

## Summary

This procedure involves checking the attacker's webserver logs to extract the stolen cookie values exfiltrated via GET requests.

## Description

After the XSS payload executes, it sends the grauth cookie to the attacker's domain in the query string. Monitoring logs captures this data for use in account takeover.

## Requirements

1. Webserver with logging enabled
2. Access to server logs
3. Successful exfiltration from previous steps

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on sensitive endpoints
- Use anomaly detection for unusual query parameters

## Objectives

1. Capture stolen cookie data
2. Verify cookie validity

## Instructions

### Step 1: Check Access Logs

**Context**: Review logs for incoming requests with cookie parameter.

Tail the server logs and look for GET /?cookie=... entries.

> Extract the encoded cookie value from the query string.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[data-exfiltration]]
- [[log-monitoring]]
