---
id: proc-uuid-2
tags:
  - csrf
  - poc
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.835Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create CSRF Proof-of-Concept HTML

## Summary

This procedure crafts a malicious HTML file using details from a captured request, creating an auto-submitting form that forges a POST to the vulnerable account closure endpoint when loaded in a browser.

## Description

Building on the captured request, this step uses Burp Suite's CSRF PoC generator or manual HTML editing to create a webpage that exploits the missing token validation. The HTML includes a hidden form mimicking the original POST data and JavaScript to submit it automatically. This is hosted externally to trick victims. Prerequisites: Captured request details; outcomes: A functional PoC that closes accounts when visited by authenticated users.

## Requirements

1. Captured request from previous procedure
2. Burp Suite Professional or text editor
3. Basic HTML/JavaScript knowledge
4. Server to host the HTML (e.g., Apache, GitHub)

## Defense

Defensive measures and detection strategies:

- Enforce same-origin policy and CSRF tokens
- Scan for and block auto-submitting forms via client-side protections
- Log and alert on requests from unexpected referers

## Objectives

1. Replicate legitimate request in HTML form
2. Ensure auto-submission without user interaction
3. Test PoC in isolated environment

## Instructions

### Step 1: Generate PoC in Burp

**Context**: Use Burp's built-in tool to automate HTML creation.

In Burp Repeater, right-click the captured request and select 'Engagement tools' > 'Generate CSRF PoC'. Customize the HTML to include auto-submit script, e.g., <script>document.forms[0].submit();</script>.

### Step 2: Customize and Save

**Context**: Adjust form to match exact parameters.

Edit the generated HTML to set action to https://target.com/services/user/closeAccount, add hidden inputs for parameters like confirm=close, and ensure it uses the victim's cookies via same-site context.

### Step 3: Test PoC

**Context**: Verify the PoC without causing harm.

Host the HTML locally (e.g., python -m http.server), load in browser authenticated to target, and confirm the POST is sent (monitor in Burp).

**Expected Output**: HTML file example:

```html
<html>
<body>
<form id="csrf" method="POST" action="https://target.com/services/user/closeAccount">
<input type="hidden" name="confirm" value="close">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[poc]]
- [[web]]
