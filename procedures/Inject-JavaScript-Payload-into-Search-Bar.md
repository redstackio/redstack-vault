---
tags:
  - xss
  - injection
  - javascript
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
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5956c777-7fb8-4525-b24f-545aae48d255
created_at: '2025-12-14T00:11:09.353Z'
updated_at: '2025-12-14T00:11:09.353Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject JavaScript Payload into Search Bar

## Summary

This procedure details the injection of a malicious JavaScript payload into the search input field of a vulnerable .mil website, exploiting the lack of input sanitization to reflect and execute the code in the victim's browser context.

## Description

The attack targets the search bar on https://███████████████████.html, where user input is directly echoed back into the HTML response without proper escaping or validation. By submitting a script tag payload, arbitrary JavaScript runs, potentially accessing the DOM. This is a classic reflected XSS scenario, discovered via manual testing of .mil sites. Prerequisites include access to the page from Step 1; outcomes include immediate code execution upon payload reflection.

## Requirements

1. Web browser with developer tools enabled for inspection
2. The target webpage loaded and search bar accessible
3. Basic knowledge of HTML and JavaScript payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs using libraries like DOMPurify or server-side escaping (e.g., htmlspecialchars in PHP)
- Implement Content Security Policy (CSP) headers to block inline script execution
- Monitor server logs for script tag patterns in search queries and rate-limit suspicious inputs

## Objectives

1. Deliver the payload without alteration through the search mechanism
2. Trigger reflection of the unsanitized input in the HTTP response
3. Achieve JavaScript execution in the browser's context

## Instructions

### Step 1: Locate and Target Search Input

**Context**: Position the payload entry point for maximum reflection likelihood.

**Action** (Input Injection):

Click into the search bar on the loaded page.

> Ensure the input field accepts arbitrary text; no client-side validation should strip tags.

### Step 2: Enter and Submit Payload

**Context**: Craft and deliver the JavaScript to exploit the reflection.

**Action** (Payload Submission):

Type the following payload into the search field:

```
<script>alert(document.cookie)</script>
```

Submit by pressing Enter or clicking the search button.

> The server processes the query and returns a response embedding the payload directly in the HTML (e.g., in a <div> or results section), causing the browser to parse and execute it.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- Web Browser

## Tags

- [[xss]]
- [[injection]]
- [[JavaScript]]
- [[web]]
