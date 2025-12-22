---
id: uuid-proc-1-683298
tags:
  - open-redirect
  - url-construction
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:35.097Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Construct-and-Test-Open-Redirect-URL

## Summary

This procedure constructs a baseline login URL for the MoPub application with a benign 'next' parameter to test and confirm the presence of an open redirect vulnerability before escalating to malicious payloads.

## Description

In the context of testing the MoPub login endpoint at https://app.mopub.com/login, this step involves building a URL that includes a safe 'next' parameter value, such as a legitimate site like Google. The goal is to verify that the application accepts and processes the parameter without validation, setting the stage for redirect exploitation. This is typically done in a web browser to simulate user interaction, revealing the lack of URL allowlisting that permits arbitrary redirects post-authentication.

## Requirements

1. Access to a web browser with developer tools enabled.
2. Knowledge of the target login URL: https://app.mopub.com/login.
3. No credentials needed for initial construction, but login required for full test.

## Defense

Defensive measures and detection strategies:

- Implement URL validation or allowlisting for redirect parameters to restrict to trusted domains.
- Monitor login endpoints for unusual 'next' parameter values via WAF rules.
- Log post-login redirects and alert on external or suspicious URIs.

## Objectives

1. Confirm the 'next' parameter is accepted without filtering.
2. Verify benign redirection works to baseline normal behavior.
3. Identify the vulnerability for further exploitation.

## Instructions

### Step 1: Build the Base URL

**Context**: Manually assemble the login URL with a safe redirect target to load the page.

No command required; enter directly in browser:

```url
https://app.mopub.com/login?next=https://google.com
```

> This loads the login page. Inspect the page source or network tab to ensure the parameter is preserved in the form submission.

### Step 2: Initial Test Without Login

**Context**: Access the URL to check for immediate errors or sanitization.

Navigate to the URL in the browser and observe if the page renders normally.

> Expected: No errors; parameter visible in URL bar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Phishing: Spearphishing Link

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[open-redirect]]
- [[url-testing]]
