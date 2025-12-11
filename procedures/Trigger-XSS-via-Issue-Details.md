---
tags:
  - xss
  - javascript-execution
type: procedure
tools:
  - '[[tools/Apache-Web-Server]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Self-hosted GitLab
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: fa0ee45d-9520-470d-8618-8fc34fb0b86d
created_at: '2025-12-11T03:47:48.731Z'
updated_at: '2025-12-11T03:47:48.731Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Trigger XSS via Issue Details

## Summary

This procedure triggers the stored XSS by navigating to the ZenTao issues page in GitLab, causing it to fetch and render the malicious API response, and then clicking the injected element to execute JavaScript.

## Description

After integration setup, visiting the specific issue URL forces GitLab to query the malicious server, which returns unvalidated data rendered in the page. The injected HTML creates a clickable element linked to a javascript: URL, executing arbitrary code when clicked, potentially allowing account takeover without strict CSP.

## Requirements

1. Configured ZenTao integration in GitLab project
2. Malicious server online and responding
3. Web browser to interact with GitLab UI

## Defense

Defensive measures and detection strategies:

- Patch GitLab to validate URLs and encode fields properly
- Monitor for JavaScript execution alerts in browser consoles
- Use network monitoring for suspicious API calls

## Objectives

1. Fetch and render malicious payload in GitLab
2. Execute XSS payload via user interaction
3. Achieve arbitrary JavaScript execution for further exploitation

## Instructions

### Step 1: Navigate to Issues Page

**Context**: Trigger the API fetch from GitLab.

Go to /-/integrations/zentao/issues/story-1 in the project.

> Page loads and fetches data from malicious server.

### Step 2: Interact with Injected Element

**Context**: Click to execute the JavaScript.

Click the big white square rendered from the HTML-injected ID.

> This triggers the javascript:alert(document.domain) payload.

### Step 3: Verify Execution

**Context**: Confirm XSS success.

Observe the alert popup showing the document domain.

> Proceed to advanced exploitation if needed, like stealing session cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #xss
- #javascript-execution
