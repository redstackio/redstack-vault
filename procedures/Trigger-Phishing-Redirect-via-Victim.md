---
id: proc-slack-trigger-redirect-104087
tags:
  - phishing
  - user-execution
  - redirect
  - slack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:26.087Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Trigger-Phishing-Redirect-via-Victim

## Summary

This procedure involves delivering the crafted open redirect URL to a victim, who upon clicking, is redirected to the SVG file, triggering JavaScript execution for an external phishing site redirect.

## Description

The victim clicks the malicious link, the /checkcookie endpoint processes the redir to the Slack-hosted SVG (allowed due to domain), the browser loads and renders the SVG, executing the onload JavaScript to redirect to the attacker's external site, such as a phishing page.

## Requirements

1. Crafted redirect URL from previous step.
2. Method to deliver link (e.g., email, social engineering).
3. Victim with browser access to Slack domains.

## Defense

Defensive measures and detection strategies:

- Browser extensions to warn on open redirects.
- Train users to verify links before clicking.
- Network monitoring for redirects to file.slack.com followed by external jumps.

## Objectives

1. Achieve user interaction for execution.
2. Complete the phishing redirect chain.
3. Compromise victim via external site.

## Instructions

### Step 1: Deliver the Link

**Context**: Share the crafted URL to entice the victim.

Send via email or message: "Check this Slack update: https://slack.com/checkcookie?redir=https://files.slack.com/files-pri/T0E7QLVLL-F0G41EG2W/redirect.svg?pub_secret=7a6caed489"

### Step 2: Monitor Execution

**Context**: When victim clicks, observe the redirect flow.

The endpoint redirects to SVG; onload executes window.location='http://www.example.com'.

> Success: Victim lands on external site; track via phishing page logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[user-execution]]
- [[redirect]]
- [[slack]]
