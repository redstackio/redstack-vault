---
tags:
  - xss
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
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
id: 34c42b75-a212-4fdd-acee-85d066b93fca
created_at: '2025-12-14T03:16:37.378Z'
updated_at: '2025-12-14T03:16:37.378Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable XSS Endpoint in Scores.ubnt.com

## Summary

This procedure involves examining the scores.ubnt.com/form.html endpoint to identify the 'p' parameter as a vector for reflected XSS, where input is directly reflected into a style attribute without sanitization, allowing potential script injection.

## Description

In the context of testing Ubiquiti's scores.ubnt.com, this step focuses on analyzing the URL structure and page source to detect reflection points. The vulnerability stems from a prior fix that overlooked style attribute contexts, making it exploitable in browsers supporting CSS expressions or url() handlers. Expected outcomes include confirmation of unsanitized input, setting the stage for payload testing.

## Requirements

1. Web browser with developer tools
2. Access to public internet for the target URL
3. Basic knowledge of HTML/CSS inspection

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input sanitization for all attributes, including styles
- Use Content Security Policy (CSP) to restrict inline scripts and styles
- Monitor for anomalous JavaScript execution in web logs

## Objectives

1. Confirm reflection of 'p' parameter in style attribute
2. Identify lack of sanitization
3. Prepare for payload injection

## Instructions

### Step 1: Access and Inspect Endpoint

**Context**: Load the target page and review the query parameters to locate potential injection points.

Visit: https://scores.ubnt.com/form.html?uid=259&p=test

Inspect the page source (right-click > View Page Source or use DevTools) to find where 'p=test' is echoed, e.g., in <div style="...test...">

> This reveals direct reflection without escaping, indicating vulnerability.

### Step 2: Validate Reflection Context

**Context**: Confirm the reflection occurs in a CSS style attribute, which can interpret certain payloads as code.

Modify the URL to include benign input and re-inspect: https://scores.ubnt.com/form.html?uid=259&p=color:red;

Check if it applies as inline style without filtering.

> Success shows no blocking of CSS properties, allowing advanced payload construction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[recon]]
