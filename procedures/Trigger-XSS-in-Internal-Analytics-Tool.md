---
id: proc-tiktok-xss-trigger
tags:
  - xss
  - execution
  - exfiltration
  - data-leak
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Automated Collection]]'
updated_at: '2025-12-13T23:55:20.919Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Automated Collection]]'
---
# Trigger-XSS-in-Internal-Analytics-Tool

## Summary

This procedure relies on the stored payload from the injection step to execute when a privileged TikTok employee accesses the tainted data in an internal browser-based analytics tool, enabling arbitrary JavaScript to run and exfiltrate sensitive session and system data.

## Description

Once the payload is stored, it renders unsafely in the internal Dorado/DataLeap analytics environment. When an admin views the partner form data, the JavaScript executes in their authenticated session, capturing elements like cookies, JWT tokens, PII (emails, phone numbers), API keys, internal paths, and backend architecture details. The data is then sent to an attacker-controlled server. This phase requires no further interaction from the attacker but assumes employee interaction with the system. Outcomes include full data leakage from privileged contexts.

## Requirements

1. Previously injected and stored XSS payload
2. Attacker-controlled endpoint for receiving exfiltrated data
3. Patience for employee interaction (typically hours to days)

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered data in internal tools with output encoding
- Deploy browser isolation or sandboxing for admin interfaces
- Implement anomaly detection on network traffic for unexpected outbound requests from internal sessions

## Objectives

1. Execute JavaScript in a high-privilege browser session
2. Collect and exfiltrate sensitive credentials and PII
3. Reveal internal system architecture for further attacks

## Instructions

### Step 1: Monitor for Trigger

**Context**: After injection, monitor the exfiltration endpoint for incoming data, as the payload activates upon admin access.

No command; use server logs or a tool like ngrok to host the callback URL.

> Success is indicated by HTTP requests containing stolen data, such as `GET /exfil?token=eyJ...&email=admin@tiktok.com`.

### Step 2: Analyze Exfiltrated Data

**Context**: Once triggered, review the captured information for tokens, keys, and paths to assess impact.

Manually inspect received payloads in the attacker's server logs.

> Expected data includes session cookies, JWTs, user PII, and internal API endpoints, confirming full compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Automated Collection]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[Exfiltration]]
