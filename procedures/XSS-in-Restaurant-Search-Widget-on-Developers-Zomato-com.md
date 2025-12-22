---
tags:
  - xss
  - reflected-xss
  - widget-injection
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
id: 845ade52-8201-42c2-a6d8-5a3e46a762e8
created_at: '2025-12-14T03:16:07.886Z'
updated_at: '2025-12-14T03:16:07.886Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS-in-Restaurant-Search-Widget-on-Developers-Zomato-com

## Summary

This procedure demonstrates a reflected XSS vulnerability in the Restaurant Search widget on developers.zomato.com, where search inputs for restaurant, cuisine, or dish are not properly sanitized, allowing immediate JavaScript execution in the widget interface.

## Description

The root cause is insufficient validation of search inputs in the widget configuration, permitting HTML and JavaScript injection. When a payload is entered and the widget is added or queried, it executes in the page context, potentially affecting developers configuring widgets or users viewing embedded instances. Exploitation involves manual input testing and can lead to session theft for authenticated users.

## Requirements

1. Web browser
2. Access to developers.zomato.com (public, but may require developer signup)
3. Navigation to the widgets section

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in widget parameters using allowlists for expected formats.
- Employ escaping for HTML attributes and Content Security Policy to block unsafe scripts.
- Log and monitor unusual inputs in widget search fields.

## Objectives

1. Inject JavaScript via search bar inputs.
2. Trigger immediate execution in the developer interface.
3. Compromise widget users or embedded applications.

## Instructions

### Step 1: Access Widget Interface

**Context**: Navigate to the vulnerable widget configuration.

Go to developers.zomato.com, click the 'widgets' tab, and select 'Restaurant Search' widget.

### Step 2: Enter Payload in Search Field

**Context**: Use the search input fields which lack sanitization.

Click 'Add Widget', then in the search bar for restaurant/cuisine/dish, enter:

```html
<img src=x onerror=alert(document.domain)>
```

### Step 3: Trigger Execution

**Context**: Submit the input to reflect and execute the payload.

Submit or query the widget. The onerror handler should fire, displaying an alert.

Modify payload for exfiltration, e.g., to send session data to an attacker server.

**Expected Output**: Alert popup with the document domain.

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
- [[reflected-xss]]
