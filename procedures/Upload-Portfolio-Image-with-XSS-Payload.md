---
tags:
  - xss
  - payload-injection
  - upload
  - shopify
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
updated_at: '2025-12-14T03:16:14.566Z'
sub_techniques: []
id: 5c19f8d8-5bbb-4bf7-81b1-ccbdb1664fd0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload Portfolio Image with XSS Payload

## Summary

This procedure details uploading an image to the Shopify Experts portfolio and injecting a reflected XSS payload into the caption field, exploiting insufficient sanitization to persist malicious HTML/JavaScript.

## Description

During the expert application, the Portfolio Images section accepts user-supplied captions that are rendered without proper escaping in the gallery view. By injecting a payload that breaks out of HTML context, an attacker can execute JavaScript when the portfolio is viewed. This targets the caption field specifically and requires form submission to save.

## Requirements

1. Active session from account creation
2. A benign image file for upload (e.g., JPG under size limits)
3. Access to the profile form's Portfolio Images section

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in HTML contexts using libraries like DOMPurify
- Implement Content Security Policy (CSP) to block inline scripts and unsafe eval
- Log and monitor form submissions for suspicious payloads containing script tags or event handlers

## Objectives

1. Upload image to establish legitimate portfolio entry
2. Inject and persist XSS payload in caption
3. Enable execution upon rendering in viewer context

## Instructions

### Step 1: Upload Image

**Context**: Add an image to the portfolio to access the caption field.

In the Portfolio Images section, click the upload button and select a test image file. Ensure it uploads successfully before proceeding to the caption.

> Upload completes with a preview; caption input appears below or adjacent.

### Step 2: Inject Payload

**Context**: Enter the malicious payload to exploit the lack of escaping.

In the caption field, input: `"><img src=x onerror=alert(document.domain)>". This closes any parent tags (e.g., <p> or <div>) and injects an erroneous img tag that fires onerror to execute the alert.

> Field accepts the input without immediate validation errors.

### Step 3: Save Profile

**Context**: Persist the changes to make the payload renderable in the gallery.

Complete any required fields and click 'Save' or 'Submit' to process the form.

> Redirects to profile/gallery page; changes are saved server-side.

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
- [[payload-injection]]
- [[upload]]
- [[shopify]]
