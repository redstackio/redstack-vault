---
id: proc-slack-inject-xss-001
tags:
  - xss
  - injection
  - slack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.374Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Slack Company Name

## Summary

This procedure involves injecting a malicious JavaScript payload into the Slack company name field during workspace setup or modification, exploiting a lack of input sanitization to store the payload for later execution.

## Description

In the context of Slack's web application, the company name field allows arbitrary input that is later reflected in message rooms without proper escaping. By setting the company name to an XSS payload like "><IMG SRC=x onerror=javascript:alert(\"XSS-by-Imran\")>", an attacker can store cross-site scripting code that executes when victims view affected areas. This targets authenticated users and can lead to arbitrary code execution in their browsers, enabling further attacks like cookie theft or phishing.

## Requirements

1. Valid Slack account with administrative access to edit workspace settings
2. Web browser for accessing the Slack interface
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization for all user-controlled fields
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript alerts or network requests from Slack domains

## Objectives

1. Store malicious JavaScript in the company name field
2. Prepare for reflection in victim-facing UI elements
3. Enable browser-based code execution without direct interaction

## Instructions

### Step 1: Access Workspace Settings

**Context**: Log in to Slack and navigate to the administration panel to reach the company name configuration.

Go to the Slack workspace settings via the web app, typically under Workspace Settings > Organization Name or similar.

### Step 2: Inject the Payload

**Context**: Enter the XSS payload into the company name field to bypass any client-side checks.

Set the company name field to: "><IMG SRC=x onerror=javascript:alert(\"XSS-by-Imran\")>"

Save the changes. The payload uses an IMG tag with an onerror handler to execute JavaScript if the source fails to load.

**Expected Output**: Settings saved without errors; the field now contains the injected payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
