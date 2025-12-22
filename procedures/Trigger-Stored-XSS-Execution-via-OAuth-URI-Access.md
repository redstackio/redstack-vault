---
id: proc-nextcloud-xss-trigger-oauth
tags:
  - xss
  - stored-xss
  - nextcloud
  - oauth
  - execution
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
updated_at: '2025-12-14T17:24:35.541Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS Execution via OAuth URI Access

## Summary

This procedure triggers the execution of a previously injected stored XSS payload in Nextcloud's OAuth redirect URI by accessing or displaying the vulnerable configuration, causing JavaScript to run in the browser context of the accessing user.

## Description

After injection, the malicious JavaScript in the OAuth redirect URI remains dormant until the URI is rendered or navigated to during an OAuth flow. Any user (including the admin) viewing the settings or completing an OAuth redirect will execute the script, which can log keystrokes, exfiltrate data, or manipulate the DOM. The attack relies on the field's output not being escaped, leading to client-side execution. Impact is confined to the Nextcloud domain due to same-origin policy, but enables phishing or session theft.

## Requirements

1. Injected payload already stored in OAuth redirect URI
2. Access to Nextcloud as any authenticated user
3. Web browser to observe execution

## Defense

Defensive measures and detection strategies:

- Escape all output in configuration UIs (e.g., use HTML entities for script tags)
- Implement browser-based protections like XSS auditors or strict CSP headers
- Log and alert on OAuth URI accesses; scan configs for script patterns

## Objectives

1. Execute the stored JavaScript payload
2. Verify impact such as alert or data exfiltration
3. Demonstrate vulnerability to non-admin users

## Instructions

### Step 1: Access OAuth Configuration

**Context**: Load the page containing the vulnerable URI to trigger rendering.

Log in as a user and navigate to the OAuth settings page where the redirect URI is displayed.

**Expected Output**: Page loads with the URI field visible.

### Step 2: Initiate OAuth Flow

**Context**: Force a redirect or URI evaluation to execute the JS.

If applicable, start an OAuth authorization process that uses the configured redirect URI, or manually navigate to the URI path in the browser.

**Expected Output**: JavaScript executes (e.g., alert dialog or network request to attacker server).

### Step 3: Observe Execution

**Context**: Confirm the payload's effects.

Check browser console for logs or network tab for exfiltration requests.

**Expected Output**: Evidence of JS running, such as popped alert or stolen data sent.

### Step 4: Validate Impact

**Context**: Test for real-world consequences.

Use a payload that steals cookies and sends to a controlled server; verify receipt.

**Expected Output**: Attacker server logs the exfiltrated data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- nextcloud
- oauth
