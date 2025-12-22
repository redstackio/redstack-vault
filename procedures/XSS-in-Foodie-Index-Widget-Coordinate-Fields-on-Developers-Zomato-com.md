---
tags:
  - xss
  - persistent-xss
  - event-handler-injection
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
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7b7f8ffa-ea99-4ea7-80d0-078d7b7532ce
created_at: '2025-12-14T03:16:07.882Z'
updated_at: '2025-12-14T03:16:07.882Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS-in-Foodie-Index-Widget-Coordinate-Fields-on-Developers-Zomato-com

## Summary

This procedure exploits an XSS vulnerability in the Foodie Index Widget on developers.zomato.com by injecting HTML tags with event handlers into longitude and latitude fields, leading to JavaScript execution upon widget loading or interaction.

## Description

Due to no sanitization of coordinate inputs, attackers can insert HTML elements like SVG with onload handlers. This executes arbitrary code when the widget is added or rendered, compromising the developer interface or embedded widget users. The vulnerability was found through testing input fields, enabling potential data theft or malicious redirects.

## Requirements

1. Web browser
2. Access to developers.zomato.com widgets
3. Basic knowledge of HTML event handlers

## Defense

Defensive measures and detection strategies:

- Validate coordinate inputs as numeric values only, rejecting HTML tags.
- Use strict parsing and encoding for all form fields.
- Implement CSP to prevent onload/onerror execution and scan for suspicious inputs.

## Objectives

1. Inject HTML with JavaScript event handlers into coordinate fields.
2. Execute code on widget load.
3. Impact widget interactions and steal user data.

## Instructions

### Step 1: Access Foodie Index Widget

**Context**: Locate the vulnerable coordinate input fields.

Visit developers.zomato.com, go to 'widgets' tab, and select 'Foodie Index Widget'.

### Step 2: Inject Payload in Coordinates

**Context**: Exploit the unsanitized longitude/latitude fields.

Click 'Add widget', then enter in both fields:

```html
<img class="emoji" alt="😯" src="x" /><svg onload=prompt(document.domain)>
```

### Step 3: Load Widget to Execute

**Context**: Trigger the onload event by saving or rendering the widget.

Save the widget configuration or interact with it. The SVG onload should prompt the domain.

For attacks, adapt to exfiltrate data via fetch or form submission.

**Expected Output**: Prompt displaying the document domain.

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

- [[xss]]
- [[event-handler]]
