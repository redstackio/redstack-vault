---
id: d374a1c1-b7f4-4191-a98e-0e2649237e14
name: Trigger and Verify XSS Payload
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:28.506Z'
updated_at: '2025-12-11T06:10:28.506Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - execution
  - verification
commands:
  - '[[commands/gitlab-env-info]]'
platforms:
  - Web
tools:
  - '[[tools/Docker]]'
  - '[[tools/Firefox]]'
  - '[[tools/GitLab]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---

# Trigger and Verify XSS Payload

## Summary

This procedure triggers the stored XSS payload by clicking the malicious link and verifies execution in the browser.

## Description

Clicking the rendered 'XSS' link executes the JavaScript alert(1); in the user's browser context, demonstrating the vulnerability.

## Requirements

1. Malicious wiki page created and saved
2. Browser like [[tools/Firefox]] to view the page

## Defense

Defensive measures and detection strategies:

- Monitor for JavaScript execution anomalies in browsers
- Implement output encoding for wiki content

## Objectives

1. Execute the XSS payload
2. Confirm vulnerability impact

## Instructions

### Step 1: Click Link

**Context**: Interact with the malicious link.

Click the 'XSS' link in the wiki page.

### Step 2: Verify Environment (Optional)

**Context**: Check GitLab environment details.

Execute [[commands/gitlab-env-info]]:

```bash
sudo gitlab-rake gitlab:env:info
```

> Displays system information for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/gitlab-env-info]]

## Tools Used

- [[tools/Firefox]]
- [[tools/GitLab]]

## Tags

- [[xss]]
- [[Execution]]
- [[verification]]
