---
tags:
  - xss
  - injection
  - web
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
updated_at: '2025-12-14T03:16:37.418Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 48dd503f-344b-4d31-bb2f-59523197533b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Zomato-Review

## Summary

This procedure involves submitting a malicious JavaScript payload via Zomato's restaurant review form to exploit insufficient input sanitization, storing the payload for later execution on viewers of the page.

## Description

In the context of Zomato's web application, the review submission feature fails to properly sanitize user input, allowing storage of XSS payloads. Targeting a specific restaurant page, the attacker crafts a payload that breaks out of HTML context and injects executable script. This stored payload affects all users who view or interact with the review, potentially leading to session hijacking by stealing cookies or performing other client-side manipulations. Prerequisites include a valid Zomato account and browser access.

## Requirements

1. Valid Zomato user account for authentication
2. Web browser to interact with the site
3. Knowledge of basic HTML/JS for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization using libraries like DOMPurify
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for unusual review content patterns via WAF rules

## Objectives

1. Store malicious JS in the review database without detection
2. Ensure payload survives storage and retrieval
3. Set up for execution on page load or user interaction

## Instructions

### Step 1: Navigate to Target Restaurant Page

**Context**: Access a vulnerable restaurant page to locate the review submission form.

Navigate to https://www.zomato.com/beirut/garcias-dbayeh-metn in your browser and ensure you're logged in.

### Step 2: Craft and Submit Payload

**Context**: Enter the XSS payload in the review text field to inject script that executes on rendering.

In the review text area, input the payload: `'><img src=x onmouseover =prompt(document.domain)>`

Submit the review.

> This payload closes any open tags, injects an img element with an onmouseover event that prompts the document domain upon hover, confirming execution.

**Expected Output**: Review posts successfully; inspect the page source to verify payload presence in the HTML.

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
- [[stored-xss]]
