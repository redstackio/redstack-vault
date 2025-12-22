---
tags:
  - xss
  - styling
  - phishing
  - web
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
updated_at: '2025-12-14T17:28:28.176Z'
sub_techniques: []
id: 64289ac9-a623-4060-abf9-f56cf0efe239
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Style XSS Payload to Mimic UI Elements

## Summary

This procedure enhances XSS payloads by applying target-specific CSS classes to injected HTML, making malicious elements indistinguishable from legitimate UI components on sites like Reverb.com, thereby increasing the effectiveness of phishing attacks.

## Description

Once basic XSS is confirmed, attackers can leverage the site's own stylesheets by assigning class attributes to injected tags. For Reverb.com, classes like `btn button button--orange button--wide` replicate native buttons. This involves iterative testing in the browser to match styles, requiring dev tools for inspection. The outcome is a deceptive payload that blends seamlessly, tricking users into interacting with phishing elements without suspicion.

## Requirements

1. Confirmed XSS vulnerability from prior discovery
2. Browser dev tools for CSS inspection
3. Knowledge of target site's CSS classes (via inspect element)

## Defense

Defensive measures and detection strategies:

- Strip or whitelist only safe attributes in inputs; block class/style attributes
- Use CSS class namespaces or hashing to prevent external mimicry
- Implement client-side validation and server-side logging of suspicious class usage

## Objectives

1. Replicate legitimate UI styling in injected HTML
2. Improve payload deception for higher interaction rates
3. Prepare for full phishing interface construction

## Instructions

### Step 1: Identify Target CSS Classes

**Context**: Analyze the site's legitimate elements to extract usable classes.

On Reverb.com, inspect a real button (e.g., search button) via dev tools to note classes like `btn button button--orange`.

> Copy exact class strings for reuse in payloads.

### Step 2: Inject Styled Test Payload

**Context**: Apply classes to a basic tag and test rendering.

Modify the search URL: `https://reverb.com/marketplace?query=<a class="btn button button--orange button--wide" href="#">Fake Unlock</a>`.

> The link should render as an orange button matching site design.

### Step 3: Refine and Validate Styling

**Context**: Ensure no visual discrepancies that could alert users.

Iterate by adding more classes (e.g., for overlays) and check cross-browser consistency.

> Success shows the element indistinguishable from native UI in both appearance and behavior.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Phishing]]
- [[web]]
