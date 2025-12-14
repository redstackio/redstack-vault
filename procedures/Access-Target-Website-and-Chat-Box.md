---
tags:
  - ssrf
  - web-access
  - initial-recon
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.268Z'
sub_techniques: []
id: 581b0882-fa1a-47f7-a4f7-dfb2f7ed3656
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Target-Website-and-Chat-Box

## Summary

This procedure outlines the initial navigation to a target website and identification of the vulnerable chat or messenger box, setting the stage for SSRF exploitation by providing access to the input interface.

## Description

In the context of exploiting a Blind SSRF vulnerability on the MTN Group website, this procedure involves loading the public-facing page and locating the chat widget typically positioned at the bottom right. This step requires no authentication and assumes standard web access, allowing attackers to probe interactive features for request forgery opportunities. Expected outcomes include visibility of the chat input, confirming the environment is ready for payload injection.

## Requirements

1. Web browser (e.g., Chrome, Firefox) with developer tools enabled
2. Internet connectivity to access the target site
3. No special permissions or tools beyond basic browsing

## Defense

Defensive measures and detection strategies:

- Implement Web Application Firewall (WAF) rules to monitor chat inputs for suspicious URLs
- Rate-limit chat interactions to prevent abuse
- Log all server-side requests from chat processing for anomaly detection

## Objectives

1. Establish connection to the vulnerable endpoint
2. Identify the chat interface for payload delivery
3. Validate site accessibility without disruptions

## Instructions

### Step 1: Navigate to Target Site

**Context**: Load the main page to observe the overall structure and locate interactive elements.

No specific command; use browser URL bar:

```bash
# In browser: https://www.mtn.co.za (or regional equivalent)
```

> Directly enter the URL in the browser. Expected output: Page renders with chat widget visible.

### Step 2: Locate Chat Widget

**Context**: Scan for the messenger box to prepare for interaction.

No command; manual inspection:

```bash
# Visually inspect bottom-right corner for chat icon
```

> Click to expand if needed. Expected output: Input field appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[ssrf]]
- [[web-access]]
