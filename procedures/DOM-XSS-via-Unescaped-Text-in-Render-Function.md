---
tags:
  - dom-xss
  - html-insertion
  - render-function
type: procedure
tools:
  - '[[tools/Internet-Explorer]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.262Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: fc5f8162-f527-46fc-a128-9e9a0c86ebf7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-XSS-via-Unescaped-Text-in-Render-Function

## Summary

This procedure exploits DOM XSS in the render function by injecting unescaped HTML/JavaScript into e.text, which is inserted via .html() without sanitization, affecting tweet text display.

## Description

In the render function, .html(this.getStatusTextHtml(e.text, e.entities)) directly inserts user-controlled e.text into the DOM, allowing <script> tags or other HTML to execute. This can be triggered via hosted PoC HTML mimicking the tweet render, leading to no-interaction XSS in Twitter timelines.

## Requirements

1. Internet Explorer for testing
2. Local or remote hosting for PoC HTML with malicious e.text
3. Access to simulate tweet rendering

## Defense

Defensive measures and detection strategies:

- Escape HTML entities in all user inputs before .html() insertion
- Use textContent or sanitized libraries like DOMPurify
- Audit jQuery DOM manipulations for raw HTML sinks

## Objectives

1. Execute JS without user interaction in tweet views
2. Target embedded content in social media
3. Demonstrate persistent XSS risks

## Instructions

### Step 1: Prepare PoC HTML

**Context**: Create HTML simulating the render sink with injected script.

Example PoC at http://innerht.ml/pocs/twitter-amp-xss/text.html:

```html
<div id="tweet">e.text with <script>alert(1)</script></div>
<script> $("#tweet").html(e.text); </script>
```

### Step 2: Load PoC

**Context**: Access the file to trigger insertion.

Open in Internet Explorer.

> The .html() call executes the script inline.

### Step 3: Validate

**Context**: Ensure automatic execution.

**Expected Output**: Alert fires on load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer]]

## Tags

- [[dom-xss]]
- [[render]]
- [[twitter]]
