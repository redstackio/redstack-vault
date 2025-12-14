---
tags:
  - csrf
  - payload-crafting
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/Cancel-Bugzilla-Password-Reset-Token]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:25:13.420Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6d7953a8-bee2-4244-ad7c-867aad011ced
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-CSRF-Payload-for-Reset-Cancellation

## Summary

This procedure details using Burp Suite to intercept a password reset cancellation request and generate a CSRF-proof HTML payload that forces the victim's browser to submit the request.

## Description

The Bugzilla /token.cgi endpoint lacks CSRF protection, allowing a crafted form to POST cancellation parameters. The attacker opens their own cancel link in Burp, intercepts the request, and uses the 'Generate CSRF PoC' feature to create an auto-submitting HTML form. This payload includes hidden fields for the cancel_token, t, a, and cancel parameters. Prerequisites: Valid token from prior step and Burp Suite. Expected outcome: Malicious HTML ready for delivery.

## Requirements

1. Burp Suite Professional installed
2. Valid cancel_token from password reset
3. Access to a web proxy setup

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens or SameSite=Strict cookies on sensitive POST endpoints
- Validate origin headers for state-changing requests
- Log and monitor anomalous POSTs to /token.cgi

## Objectives

1. Intercept legitimate cancellation request
2. Generate exploitable CSRF HTML
3. Ensure payload submits from victim's IP

## Instructions

### Step 1: Open Cancel Link in Burp

**Context**: Proxy the request to capture details.

Configure browser to use Burp proxy, then click the password reset cancel link from the email.

**Expected Output**: Intercepted POST to /token.cgi in Burp Repeater.

### Step 2: Generate CSRF PoC

**Context**: Use Burp to create the payload.

In Burp, right-click the request and select 'Engagement tools' > 'Generate CSRF PoC'. Customize the form to auto-submit on load.

**Command** ([[commands/Cancel-Bugzilla-Password-Reset-Token]]):
```bash
curl -X POST https://bugzilla.mozilla.org/token.cgi \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'cancel_token=1727251240-UxKc4U5ThgrHPhWNJ323-fahjy5Pn05h5ZYb7OqG-SI&t=3XOIDGIRtcwC3icniucOlm&a=cxlpw&cancel=Cancel'
```

> This curl equivalent verifies the request; the HTML form mimics this POST with hidden inputs.

**Expected Output**: HTML file like <form action="https://bugzilla.mozilla.org/token.cgi" method="post"><input type="hidden" name="cancel_token" value="..." /> ... <input type="submit" value="Click" onload="this.form.submit()" /></form>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/Cancel-Bugzilla-Password-Reset-Token]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf
- payload-crafting
- burp-suite
