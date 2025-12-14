---
id: proc-uuid-4
tags:
  - analysis
  - logging
  - extension
type: procedure
tools:
  - '[[tools/Eval-Villain]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:15.766Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Analyze-Injection-with-Eval-Villain

## Summary

This procedure uses the Eval Villain Firefox extension to capture and log strings injected into dangerous JavaScript functions, revealing the exact points of DOM XSS in ad scripts.

## Description

Eval Villain intercepts calls to functions like document.write, logging the full strings for analysis. In this scenario, it exposes how the URL's single quote breaks the ad's string context. Targeted at web developers or pentesters, outcomes include vulnerability reports and fix recommendations. Prerequisites: Extension installed and page loaded.

## Requirements

1. Firefox browser.
2. Eval Villain extension installed and enabled.
3. Access to extension logs or attachments.

## Defense

Defensive measures and detection strategies:

- Integrate similar logging tools in production for anomaly detection.
- Review third-party scripts for eval/document.write usage.
- Use automated scanners for DOM XSS in ad integrations.

## Objectives

1. Capture injected strings.
2. Identify escape vulnerabilities.
3. Document for reporting.

## Instructions

### Step 1: Install and Enable Extension

**Context**: Prepare the tool for interception.

Install Eval Villain from Firefox add-ons; enable it for the session.

> Extension ready; it auto-logs on dangerous function calls.

### Step 2: Trigger and Capture

**Context**: Reload page to log ad injections.

Navigate/refresh the crafted URL; let ads load.

> Extension captures strings like url='https://...&loc=malicious-url'.

### Step 3: Review Logs

**Context**: Analyze captured data.

Access extension logs or export to files (e.g., adstring1.txt).

> Logs show full document.write content, highlighting the breakout point.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Eval-Villain]]

## Tags

- [[analysis]]
- [[logging]]
- [[firefox]]
