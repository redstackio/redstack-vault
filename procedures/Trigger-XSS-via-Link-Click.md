---
id: proc-uuid-instacart-xss-trigger-001
tags:
  - xss
  - execution-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.873Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Link-Click

## Summary

This procedure triggers the reflected XSS payload by accessing the crafted URL and clicking the malicious link, executing arbitrary JavaScript in the browser context for potential session hijacking or data theft.

## Description

Following payload injection, the partner recipe page renders a clickable element (e.g., recipe image) with the injected href. Clicking it invokes the javascript: protocol, running the script as if it were native to the page. This requires victim interaction but can be socially engineered (e.g., via phishing). The attack targets the web platform and exploits client-side rendering flaws.

## Requirements

1. Crafted URL from prior injection step
2. Web browser with JavaScript enabled
3. User interaction capability (self or simulated victim)

## Defense

Defensive measures and detection strategies:

- Escape or validate all href attributes to prevent protocol injection
- Implement clickjacking protection and user education on suspicious links
- Log and alert on JavaScript errors or unexpected script executions in browser consoles

## Objectives

1. Execute the injected JavaScript payload
2. Confirm control over the victim's browser session
3. Escalate to data exfiltration if successful

## Instructions

### Step 1: Access the Crafted URL

**Context**: Load the page to render the reflected content.

Paste the full URL into the browser address bar and navigate.

Example:
```url
https://www.instacart.com/store/partner_recipe?recipe_url=javascript:alert(1)&partner_name=&ingredients%5B%5D=apples&ingredients%5B%5D=butter&ingredients%5B%5D=Splenda+Brown+Sugar+Blend&ingredients%5B%5D=cinnamon&ingredients%5B%5D=nutmeg&title=Barb%27s+Fried+Apples+-Diabetic-Low+Fat&description=&image_url=%2Fassets%2Fimg%2Fno-recipe-image.jpg
```

> The page should display a recipe card with an image link containing the payload.

### Step 2: Interact with the Link

**Context**: Click the reflected element to trigger execution.

Click on the recipe image or title link (e.g., 'Barb's Fried Apples -Diabetic-Low Fat').

> An alert(1) dialog should appear, confirming execution. In a real attack, replace with document.cookie theft or keylogging.

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
- [[execution-trigger]]
