---
id: proc-identify-domxss-js
tags:
  - xss
  - dom-xss
  - code-analysis
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:31.654Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-DOM-XSS-in-JavaScript-Code

## Summary

This procedure uses passive code analysis to detect a DOM-based XSS vulnerability in client-side JavaScript, specifically where unsanitized window.location.pathname is used to construct a <base> tag href, enabling protocol-relative URL attacks.

## Description

In the context of web applications like the Informatica assessment page, JavaScript dynamically appends a <base> element to the document head using the current pathname. This can be exploited if the pathname includes protocol-relative constructs (e.g., //attacker.com), causing subsequent resource loads to originate from an attacker-controlled domain. The procedure involves scanning the page's JS code to identify such patterns, assuming access to the target URL via a proxy tool.

## Requirements

1. Burp Suite installed and configured as a browser proxy
2. Access to the target web page (https://alpha.informatica.com/assessmentBase/assessment.html)
3. Basic knowledge of JavaScript DOM manipulation

## Defense

Defensive measures and detection strategies:

- Sanitize or validate window.location.pathname before use in DOM elements
- Use absolute URLs for <base> tags instead of pathname-derived values
- Implement Content Security Policy (CSP) to restrict script sources

## Objectives

1. Locate vulnerable JavaScript code insertions
2. Confirm lack of input sanitization on pathname
3. Assess potential for XSS exploitation

## Instructions

### Step 1: Configure Proxy and Load Page

**Context**: Set up Burp Suite to intercept and analyze the page load, enabling passive scanning of JavaScript resources.

No specific command; configure Burp Suite proxy in browser settings and navigate to the target URL.

> Burp Suite's passive scanner will automatically analyze loaded JS files for vulnerabilities like unsanitized DOM writes.

### Step 2: Run Code Analysis

**Context**: Use Burp's code analysis engine to inspect the JS for DOM-based issues.

Focus on scripts in the <head> that manipulate the DOM with location data.

> Look for patterns like document.createElement('base') or jQuery appends using pathname; expected output is a vulnerability alert on the <base> tag construction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[dom-xss]]
- [[code-analysis]]
