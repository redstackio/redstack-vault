---
id: proc-modify-logout-malicious
tags:
  - open-redirect
  - phishing
  - expedia
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-malicious-logout]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:34.957Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Modify-Logout-URL-for-Malicious-Redirect

## Summary

This procedure exploits the open redirect by appending a malicious URL to the rurl parameter in Expedia's logout endpoint, causing users to be redirected to an attacker-controlled site for phishing.

## Description

The vulnerability stems from inadequate validation of the rurl parameter after the '?' in the logout URL. By crafting /?logout=1&rurl=https://malicious-site.com, the application performs an uncontrolled redirect. This works across browsers but is more reliable in Firefox due to encoding differences. The attack scenario involves sending the crafted link to victims, who upon clicking and logging out, are sent to a phishing page mimicking Expedia to steal credentials.

## Requirements

1. Knowledge of a malicious domain under attacker control
2. Curl or browser for testing
3. Target: www.expedia.com logout endpoint

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against a whitelist of trusted domains
- Apply consistent URL encoding and decoding
- Log and alert on redirects to external/unexpected domains

## Objectives

1. Force redirect to arbitrary external URL
2. Enable phishing post-logout
3. Confirm lack of validation

## Instructions

### Step 1: Craft Malicious URL

**Context**: Append the rurl parameter with a malicious site to the logout path.

**Command** ([[commands/curl-malicious-logout]]):
```bash
curl -X GET "https://www.expedia.com/?logout=1&rurl=https://qx4lw1nsec.blogspot.com/" -v
```

> The command triggers the redirect; verbose output shows Location header pointing to the malicious URL. Success indicates the vulnerability is exploitable.

### Step 2: Test in Browser

**Context**: Open the crafted URL in a browser to simulate victim interaction.

No command; paste URL into Firefox for immediate redirect.

> Expected: Browser navigates to the external site without warnings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### Sub-Techniques


## Commands Used

- [[commands/curl-malicious-logout]]

## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
