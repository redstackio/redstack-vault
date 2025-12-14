---
tags:
  - css-injection
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: fb732560-b87f-4a60-8644-ac51bfb1c8d0
created_at: '2025-12-14T03:16:37.059Z'
updated_at: '2025-12-14T03:16:37.059Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-CSS-Payload-into-Search-Parameter

## Summary

This procedure crafts and appends a malicious CSS payload to the 's' search parameter on Avito.ru, closing open style attributes to inject arbitrary CSS rules, enabling defacement or further exploitation.

## Description

User input from the 's' parameter is directly embedded into CSS blocks, such as style attributes, without escaping quotes or validating content. The payload '><b/style=position:fixed;top:0;left:0;font-size:200px>XSS<!-- closes the attribute, injects a new bold element positioned fixed at the top-left with large font size to display 'XSS', and comments out the rest to avoid syntax errors. This targets the vulnerability in IE11 and sets up for advanced attacks like JS execution via expression() or data theft via selectors.

## Requirements

1. Access to the target URL from Step 1
2. Ability to modify URL parameters manually or via browser tools
3. Understanding of CSS syntax for payload crafting

## Defense

Defensive measures and detection strategies:

- Escape user input in CSS contexts (e.g., replace quotes with &quot;)
- Use parameterized queries or whitelist allowed characters in search inputs
- Log and alert on payloads containing CSS keywords like 'position:fixed' or 'expression'

## Objectives

1. Close existing style attributes with injected quotes
2. Insert custom CSS rules for visual or functional impact
3. Ensure payload evades basic encoding in legacy browsers

## Instructions

### Step 1: Craft the Payload

**Context**: Build a payload that breaks out of the CSS string and adds new rules without breaking page rendering.

No command required; construct the string manually.

> Payload: ?s='><b/style=position:fixed;top:0;left:0;font-size:200px>XSS<!--. The leading quote closes the attribute, > closes the tag, and <!-- comments out trailing content.

### Step 2: Append to URL and Load

**Context**: Integrate the payload into the target URL and refresh the page.

No command required; edit the address bar.

> Full URL: https://www.avito.ru/rossiya/nedvizhimost?s='><b/style=position:fixed;top:0;left:0;font-size:200px>XSS<!--. Load the page to apply the injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[css-injection]]
- [[payload-injection]]
