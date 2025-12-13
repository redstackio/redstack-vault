---
tags:
  - http-request-smuggling
  - payload-crafting
  - open-redirect
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 3c3c45be-bedf-44fb-a482-39bf16908ce1
created_at: '2025-12-13T09:01:26.239Z'
updated_at: '2025-12-13T09:01:26.239Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft and Send Smuggling Payload

## Summary

This procedure details crafting a CL.TE smuggling payload to poison the backend socket and hijack victim requests, forcing an open redirect to an attacker-controlled server for cookie exfiltration.

## Description

Using Burp Suite, a payload is created that prepends malicious data to victim requests, transforming them into GET requests that trigger a 301 redirect including session cookies. The target is slackb.com, requiring SSL configuration. Expected outcomes include successful socket poisoning and request hijacking.

## Requirements

1. Burp Suite with Repeater and Collaborator
2. Attacker-controlled URL for redirection
3. Vulnerable CL.TE endpoint

## Defense

Defensive measures and detection strategies:

- Rate limit suspicious requests
- Monitor for unusual redirects in server logs

## Objectives

1. Poison backend socket
2. Hijack and redirect victim requests
3. Enable cookie leakage

## Instructions

### Step 1: Craft Payload in Burp Repeater

**Context**: Create the CL.TE payload to prepend data and force redirect.

> Configure Repeater for slackb.com:443 (SSL) and send the request with the collaborator URL.

### Step 2: Set Up Burp Collaborator

**Context**: Prepare the collaborator to receive exfiltrated data.

> Copy the collaborator URL and integrate it into the payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- http-request-smuggling
- payload-crafting
