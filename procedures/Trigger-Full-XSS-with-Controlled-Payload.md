---
id: proc-uuid-005
name: Trigger-Full-XSS-with-Controlled-Payload
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.066Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss-trigger
  - execution
  - cookie-theft
platforms:
  - Web
  - Browser Extension
tools:
  - '[[tools/Awesome-Autocomplete-Extension]]'
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-Full-XSS-with-Controlled-Payload

## Summary

This procedure triggers the full XSS by searching for a query that loads the malicious issue, causing the extension to render and execute the embedded JavaScript, alerting sensitive data like cookies.

## Description

A simple search like a single apostrophe `'` in the repository context forces the extension to fetch and insert the issue details unsanitized, executing the script in the GitHub.com origin. This enables arbitrary JS, such as session hijacking for logged-in users.

## Requirements

1. Malicious repository and issue created and indexed
2. Extension active on GitHub search
3. Authenticated session for impact demonstration

## Defense

Defensive measures and detection strategies:

- Extensions should use textContent or innerText instead of innerHTML for dynamic content
- GitHub: Escape HTML in indexed metadata
- User: Log out or use incognito for testing; monitor cookie access

## Objectives

1. Load the payload via autocomplete search
2. Execute JS to access document.domain and document.cookie
3. Demonstrate potential for data exfiltration or takeover

## Instructions

### Step 1: Craft Trigger Query

**Context**: Use a minimal query to target the malicious issue without alerting filters.

In GitHub search bar, enter: `' ` (single apostrophe) while focusing on the repository namespace.

```text
'
```

> This loads issue details into autocomplete.

### Step 2: Execute and Observe

**Context**: Render the results to trigger script execution.

Allow autocomplete to populate; the extension inserts the payload, firing the alert.

> Alert shows "XSS on github.com. Cookies: [values]", confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Awesome-Autocomplete-Extension]]

## Tags

- [[xss-trigger]]
- [[Execution]]
