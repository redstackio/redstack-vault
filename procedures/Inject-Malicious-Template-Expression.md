---
tags:
  - template-injection
  - client-side
  - injection
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
updated_at: '2025-12-13T23:52:33.852Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 25e6e819-3998-48f0-b0b6-538e17415b50
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Template-Expression

## Summary

This procedure exploits a client-side template injection vulnerability by submitting user input containing malicious template expressions to the Image Collection feature, allowing arbitrary code execution when the template is rendered in a victim's browser.

## Description

In applications using client-side template frameworks (e.g., Handlebars or Angular), user input is dynamically embedded into HTML templates without proper escaping or validation. Attackers can supply payloads that the framework interprets as executable code, such as JavaScript constructors, leading to code injection. In this scenario, the Image Collection feature stores unsanitized input, which is later rendered client-side, enabling stored XSS. Prerequisites include access to the feature and knowledge of the template syntax (test via trial-and-error or framework documentation).

## Requirements

1. Valid user session on the target web application.
2. Access to the Image Collection input form (e.g., for adding image descriptions).
3. Web browser to submit and test payloads.
4. Optional: Proxy tool like Burp Suite to intercept and modify requests.

## Defense

Defensive measures and detection strategies:

- Sanitize all user input before embedding in templates using framework-specific escaping functions (e.g., Handlebars' `{{{tripleStash}}}` for HTML-safe output).
- Implement content security policy (CSP) to restrict script execution and data exfiltration.
- Monitor for anomalous JavaScript execution in client-side logs or via browser security tools.
- Validate template expressions server-side to prevent malicious syntax.

## Objectives

1. Store malicious payload in the application's database via user input.
2. Confirm injection without triggering errors.
3. Set up for subsequent XSS execution on page load.

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate the user input mechanism in the Image Collection feature, such as a text field for image tags or descriptions, where input is directly interpolated into client-side templates.

No specific command required; use the browser to navigate to the feature and inspect the form (e.g., right-click > Inspect Element to view template usage).

> Expected output: Identification of the input field and confirmation that submitted text appears in rendered templates (e.g., via `{{input}}` syntax).

### Step 2: Test for Template Injection

**Context**: Submit a benign payload to verify the framework executes expressions, such as math operations to detect evaluation.

Use the browser form to submit: `{{7*'7'}}` in the input field.

> Expected output: The page renders `49` instead of the literal string, confirming injection. If not, try framework-specific syntax like `${7*7}` for Angular.

### Step 3: Submit Malicious Payload

**Context**: Craft and inject a payload that executes JavaScript, such as creating an alert or exfiltration function, to achieve XSS.

Submit payload like: `{{constructor.constructor('alert(1)')()}}` (for prototype pollution-style injection common in many frameworks).

> Expected output: Payload stored successfully; test by refreshing the page to see if it executes (use own account for safety). Adapt payload based on framework (e.g., `<% alert(1) %>` for ERB-like templates).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- template-injection
- client-side
- injection
