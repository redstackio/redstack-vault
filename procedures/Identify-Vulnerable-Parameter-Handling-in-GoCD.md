---
id: proc-gocd-identify-002
tags:
  - xss
  - parameter-handling
  - gocd
  - javascript
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
updated_at: '2025-12-13T23:52:24.679Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-Vulnerable-Parameter-Handling-in-GoCD

## Summary

This procedure analyzes the JavaScript code in the GoCD Analytics Plugin to identify the insecure handling of the 'msg' URL parameter, which enables DOM-based XSS by directly inserting decoded input into HTML without escaping.

## Description

The attack scenario involves dissecting the plugin's client-side code to find where user-controlled data from the URL is processed. In the target web environment running GoCD, the code uses regex to extract the parameter, decodes it, and injects it via jQuery's .html() method, wrapped in a <p> tag by Utils.infoMessage. Prerequisites include access to the source code; expected outcomes are confirmation of the XSS vector.

## Requirements

1. Source code from the GitHub repository
2. Understanding of DOM manipulation and URL parsing in JavaScript
3. Tools for code annotation or a text editor

## Defense

Defensive measures and detection strategies:

- Use input sanitization libraries like DOMPurify before inserting data into the DOM
- Employ Content Security Policy (CSP) to restrict inline scripts
- Perform dynamic analysis with tools like OWASP ZAP to detect runtime XSS

## Objectives

1. Trace the flow of the msg parameter from URL to DOM
2. Confirm lack of escaping in insertion points
3. Assess potential for arbitrary code execution

## Instructions

### Step 1: Extract Parameter Logic

**Context**: Locate the code responsible for parsing the URL search string.

Identify: window.location.search.match(/\?&?msg=([^&]+)/)

> This regex captures the msg value; expected output: Matched parameter value.

### Step 2: Decode and Process Input

**Context**: Check for decoding and any sanitization steps.

Note: decodeURIComponent on the captured value to get msgText.

> No escaping occurs here, setting up the injection point.

### Step 3: Insertion into DOM

**Context**: Verify how the processed input is added to the page.

Observe: $(document.body).html(Utils.infoMessage(msgText))

> Utils.infoMessage wraps in <p>msgText</p>, and .html() interprets it as HTML, allowing script tags.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- vulnerability-identification
- dom-injection
