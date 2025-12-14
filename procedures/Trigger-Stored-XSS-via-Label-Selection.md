---
tags:
  - xss
  - execution
  - trigger
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.475Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b95562ad-128e-42ea-b2ea-9cde9988d51a
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Label-Selection

## Summary

This procedure describes triggering the stored XSS payload by having a user select the malicious label on the VK.com orders list page, resulting in JavaScript execution in the victim's browser.

## Description

Once the payload is stored in a label, it executes when the orders list page renders the filter interface for any user viewing or interacting with it. The scenario involves a victim (community member or admin) accessing the page, leading to arbitrary JS execution for session theft or data exfiltration. Target: VK.com web app. Outcomes: Code runs in victim's context, potentially hijacking sessions. Prerequisites: Injected payload from prior step.

## Requirements

1. Access to a victim account or inducement for victim to view the page
2. Server to receive exfiltrated data (e.g., attacker-controlled domain)
3. Monitoring tools for callback verification

## Defense

Defensive measures and detection strategies:

- Output encode all user-generated content before rendering (e.g., HTML entity encoding)
- Deploy client-side XSS auditors or CSP with strict script-src policies
- Monitor for anomalous JS execution or external requests from the page

## Objectives

1. Execute the stored payload in a victim's browser session
2. Achieve impacts like cookie theft or account takeover
3. Validate exploitation via observable effects (alerts or logs)

## Instructions

### Step 1: Induce Victim Access

**Context**: Ensure a victim loads the vulnerable orders list page.

Share the community link or notify the victim to check orders, prompting them to visit the page with the malicious label.

> Victim navigates to the community orders list independently.

### Step 2: Select Malicious Label

**Context**: Trigger rendering of the stored payload through filter interaction.

The victim clicks on the filter dropdown and selects the injected label, causing the page to re-render with the label text.

> The filter applies, and the payload executes as the label is inserted into the DOM.

### Step 3: Observe Execution

**Context**: Confirm JS runs and achieves the desired impact.

Monitor for an alert popup or incoming request to the attacker's server with stolen data like cookies.

> Network logs show data exfiltration, or console errors indicate JS execution.

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

- [[xss]]
- [[Execution]]
- [[trigger]]
