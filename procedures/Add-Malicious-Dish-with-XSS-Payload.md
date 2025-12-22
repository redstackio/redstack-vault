---
id: proc-uuid-003
tags:
  - xss-injection
  - payload-craft
  - dish-name
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:30.782Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Add-Malicious-Dish-with-XSS-Payload

## Summary

This procedure injects a malicious JavaScript payload into a dish name on a Zomato restaurant profile, exploiting lack of input sanitization for later XSS execution in search results.

## Description

The procedure targets Zomato's dish addition feature within an editable restaurant. User-controlled names are rendered unescaped in the 'explore-keywords-dropdown'. Outcomes: Payload stored and ready for triggering. Prerequisites: Edit access to restaurant.

## Requirements

1. Edit access to approved restaurant
2. Knowledge of XSS payloads (e.g., <svg/onload=alert(1);>)
3. Unique dish name to avoid conflicts

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in UI rendering
- Validate dish names for script tags or special characters
- Monitor for unusual dish additions post-restaurant approval

## Objectives

1. Store XSS payload in dish name
2. Bypass any client-side validation
3. Enable reflected execution in searches

## Instructions

### Step 1: Navigate to Dish Addition

**Context**: Access the menu/dish edit section.

In the restaurant edit page, find 'Add Dish' or 'Menu' section.

### Step 2: Craft and Enter Payload

**Context**: Input the malicious name.

Set Dish Name to: "Cool Dish >%0D%0A%0D%0A<svg/onload=alert(1);>"

Fill other fields neutrally (e.g., price: $10) and submit.

> Expected output: Dish added to menu without error.

### Step 3: Verify Storage

**Context**: Check if payload is stored intact.

View the restaurant menu to see the dish name; ensure special characters are present.

> Expected output: Payload visible in dish list.

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
- [[injection]]
