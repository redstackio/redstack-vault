---
tags:
  - xss
  - stored-xss
  - javascript
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
updated_at: '2025-12-14T03:16:02.537Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a9030cc7-d4a1-4b89-a1c6-f1e67417aa7c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Clicking-Bookmark

## Summary

This procedure simulates a victim interacting with the malicious bookmark to execute the stored JavaScript payload, demonstrating the full impact of the stored XSS vulnerability.

## Description

Clicking the bookmark title causes the browser to interpret the href as a javascript: URI, executing the payload in the current page's context. This can lead to alerts, cookie access via document.cookie, or more advanced attacks like keylogging. The vulnerability affects any viewer of the page, amplifying reach in a collaborative wiki environment.

## Requirements

1. Loaded wiki page with the bookmark (from previous procedure)
2. Victim's browser session (potentially authenticated)
3. No browser extensions blocking javascript: URIs

## Defense

Defensive measures and detection strategies:

- Browser-level protections like disabling javascript: links
- Wiki plugin updates to escape hrefs
- Monitor for unexpected JavaScript execution via CSP violation reports

## Objectives

1. Execute the payload to confirm XSS
2. Observe impact like alert or data exfiltration
3. Escalate if possible (e.g., to session hijack)

## Instructions

### Step 1: Identify the Link

**Context**: Locate the clickable bookmark title on the page.

Scan the wiki page for the title (e.g., "powerpuff_hackerone_test") rendered as a hyperlink.

> Link is visible with href inspecting to javascript:alert(document.domain).

### Step 2: Click to Trigger

**Context**: Simulate victim interaction to run the code.

Click the bookmark title.

> Alert dialog appears showing the domain, confirming execution.

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
- [[stored-xss]]
- [[JavaScript]]
- [[Execution]]
