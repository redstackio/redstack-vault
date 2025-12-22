---
tags:
  - xss
  - execution
  - trigger
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8efd32b1-58b7-4166-9e58-f7dd71f1c0ed
created_at: '2025-12-14T03:16:08.152Z'
updated_at: '2025-12-14T03:16:08.152Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Image-Enlargement

## Summary

This procedure demonstrates executing the stored XSS payload by interacting with the attached image in the Shopify forum topic, leading to arbitrary JavaScript execution in the viewer's browser.

## Description

Clicking to enlarge the image causes the forum software to render the topic title in a new context without proper escaping, executing the injected <img> tag's onerror handler. This results in prompt(1) or any custom payload (e.g., cookie theft via document.cookie). The attack impacts any user viewing and interacting with the topic, highlighting the stored nature of the XSS.

## Requirements

1. Topic with attached image and XSS payload from previous steps
2. Victim or test browser to simulate interaction
3. No special permissions needed for triggering

## Defense

Defensive measures and detection strategies:

- Encode title content during all renders, especially in modals/popups
- Implement strict XSS filters on dynamic content
- Monitor for JavaScript errors or unusual prompts in client logs

## Objectives

1. Execute stored JavaScript in victim browsers
2. Validate payload effectiveness
3. Demonstrate impact like session hijacking

## Instructions

### Step 1: View the Topic

**Context**: Load the topic page containing the image.

Open the URL of the created topic in a browser.

> Page renders with title and attached image visible.

### Step 2: Interact with Image

**Context**: Trigger re-rendering by enlarging the image.

Click the attached image to open/enlarge it (e.g., in a lightbox or modal).

> JavaScript executes; expect a prompt dialog or console alert confirming success.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
- [[JavaScript]]
