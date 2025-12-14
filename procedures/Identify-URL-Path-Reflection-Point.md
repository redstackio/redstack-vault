---
id: p-identify-url-reflection
tags:
  - xss
  - reflection
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:12.978Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify URL Path Reflection Point

## Summary

This procedure identifies the unsanitized reflection of URL path input in the HTML response on the Glassdoor job search page, confirming the XSS vulnerability.

## Description

The /Job/[INPUT] path segment directly mirrors user-provided strings into the HTML without escaping special characters like <, >, or ". This allows for XSS payload injection. The procedure uses browser developer tools to inspect the page source in a web environment. Prerequisites include access to the base URL; outcomes confirm the lack of sanitization.

## Requirements

1. Loaded job search page
2. Browser with developer tools (F12)
3. Basic HTML knowledge

## Defense

Defensive measures and detection strategies:

- Apply HTML entity encoding to all reflected inputs
- Use Content Security Policy (CSP) to restrict script execution

## Objectives

1. Confirm input reflection without sanitization
2. Identify exact locations of reflection in HTML
3. Assess payload potential

## Instructions

### Step 1: Inspect Page Source

**Context**: Use developer tools to view how the URL path input is rendered in the HTML.

No command; right-click and select 'Inspect' or press F12, then search for the input string.

> Look for the path segment like /Job/pratt-whitney-jobs appearing raw in <div> or other elements. Expected output: Input echoed without &lt; or &gt; encoding.

### Step 2: Test with Special Characters

**Context**: Modify URL slightly to include a quote or angle bracket and reload.

Append a test like /Job/test" to the path and observe.

> Expected output: HTML breaks if unescaped, e.g., closing a tag prematurely.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- [[xss]]
- [[reflection]]
