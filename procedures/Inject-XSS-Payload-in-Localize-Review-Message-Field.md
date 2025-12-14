---
id: proc-localize-xss-injection-001
tags:
  - xss
  - html-injection
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.844Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Localize-Review-Message-Field

## Summary

This procedure exploits a cross-site scripting (XSS) and HTML injection vulnerability in the Localize platform's phrase review message field by injecting a malicious payload that evades sanitization, leading to arbitrary JavaScript execution in the browsers of users who view the reviewed content.

## Description

The Localize platform, used for localization and translation management, fails to properly sanitize user input in the message field during phrase approval and review. Attackers with access to the review interface can inject HTML elements, such as an SVG with a base64-encoded onload JavaScript handler, which executes when the message is rendered. This can result in client-side attacks like session hijacking, phishing, or data exfiltration for any user interacting with the affected review content. The vulnerability was reported on HackerOne (Report #7876) and targets endpoints like http://www.localize.io/review/{project}/languages/{lang}.

## Requirements

1. Authenticated access to the Localize platform as a reviewer or approver
2. Web browser capable of executing JavaScript (e.g., Chrome, Firefox)
3. Network connectivity to the target Localize instance

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all user-supplied content using libraries like DOMPurify
- Deploy Content Security Policy (CSP) headers to restrict script execution and inline HTML
- Monitor for anomalous JavaScript execution or unexpected alerts in application logs
- Conduct regular security audits of review and approval workflows

## Objectives

1. Inject and execute arbitrary JavaScript in victim browsers
2. Demonstrate potential for session theft or data collection
3. Highlight risks of unsanitized user-generated content in collaborative platforms

## Instructions

### Step 1: Navigate to Phrase Review Endpoint

**Context**: Gain access to the vulnerable review interface to prepare for payload injection.

Log in to the Localize platform and navigate to a phrase review page, such as http://www.localize.io/review/3C/languages/3. Select a phrase to approve or review.

**Expected Output**: The review interface loads, displaying the message input field.

### Step 2: Inject Malicious Payload

**Context**: Enter the XSS payload into the message field to exploit the lack of sanitization.

In the message input field, paste the following payload:

```html
<object data="data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoNCk+"></object>
```

This decodes to an SVG element that triggers alert(4) on load. Submit the approval or review to store the payload.

**Expected Output**: Payload is accepted without error and stored in the review.

### Step 3: Trigger Execution

**Context**: Render the injected content to execute the JavaScript.

Have another user (or yourself in a different session) view the reviewed phrase, or wait for the platform to render the message. The onload attribute will execute the JavaScript.

**Expected Output**: JavaScript alert displays "4", confirming execution. In a real attack, replace with payloads for cookie theft (e.g., document.cookie) or redirects.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[html-injection]]
- [[web-vulnerability]]
