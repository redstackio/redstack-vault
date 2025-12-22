---
id: p-identify-html-input
tags:
  - html-injection
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:21.102Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable HTML Input

## Summary

This procedure involves testing web application input fields to identify points where user input is reflected without proper HTML sanitization, enabling the injection of HTML tags and setting the stage for XSS exploitation.

## Description

In web applications, reflected inputs occur when user-supplied data is immediately echoed back in the response, such as in error messages or search results. Without encoding (e.g., converting < to &lt;), attackers can inject HTML. This procedure uses manual testing with browser tools to probe for such flaws, focusing on forms or parameters that render input directly in HTML. Prerequisites include access to the application and basic knowledge of HTML. Expected outcomes: confirmation of injectable points, leading to payload crafting.

## Requirements

1. Web browser with developer tools (e.g., Chrome or Firefox)
2. Direct access to the target web application via HTTP/HTTPS
3. No special credentials; assumes public-facing input fields

## Defense

Defensive measures and detection strategies:

- Implement output encoding using libraries like OWASP ESAPI or built-in functions (e.g., htmlspecialchars in PHP)
- Deploy WAF rules to detect and block common injection patterns, including HTML tags
- Use Content Security Policy (CSP) to restrict inline script execution

## Objectives

1. Locate input fields that reflect unsanitized HTML
2. Confirm lack of escaping by observing rendered tags
3. Identify reflection points for payload injection

## Instructions

### Step 1: Probe Input Fields

**Context**: Systematically test common input areas like search bars, login forms, or URL parameters to find reflection without sanitization.

Navigate to the target page and submit test payloads such as `<b>test</b>` or `<script>alert(1)</script>`. View the response in browser developer tools (F12 > Elements tab) to check if tags are rendered (e.g., text appears bold) rather than escaped.

**Expected Output**: If vulnerable, `<b>test</b>` renders as bold "test"; page source shows raw tags.

### Step 2: Confirm Injection Point

**Context**: Isolate the exact parameter or field (e.g., ?q= or POST body) where input is reflected.

Use URL encoding if needed (e.g., %3Cscript%3Ealert(1)%3C/script%3E) and observe the HTML response via Network tab in dev tools. Look for contexts like attribute values or body text where HTML can break out.

**Expected Output**: Input appears in source without entities, e.g., value="&lt;script&gt;" becomes value="<script>".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[html-injection]]
- [[web-vuln]]
