---
tags:
  - xss
  - trigger
  - execution
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
updated_at: '2025-12-14T03:16:14.563Z'
sub_techniques: []
id: b96a7561-3801-4d69-afc3-be7eff2ec6de
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS in Portfolio View

## Summary

This procedure demonstrates triggering the injected XSS payload by interacting with the vulnerable portfolio image view on experts.shopify.com, resulting in arbitrary JavaScript execution in the victim's browser context.

## Description

After saving the profile with the malicious caption, the gallery renders user inputs unsafely. Clicking on the image causes the caption to load, executing the injected script. This can affect any user viewing the portfolio, leading to session theft or phishing. The attack relies on the onerror handler in a broken img tag.

## Requirements

1. Saved profile with injected payload
2. Access to the profile or gallery page
3. Victim (or self for testing) viewing the page in a browser

## Defense

Defensive measures and detection strategies:

- Encode output in HTML contexts to prevent tag injection
- Validate and strip dangerous attributes (e.g., onerror) from user content
- Monitor browser consoles and error logs for unexpected script executions or alerts

## Objectives

1. Render the vulnerable caption to initiate execution
2. Confirm JavaScript runs in the page's domain context
3. Demonstrate potential for broader client-side attacks

## Instructions

### Step 1: Navigate to Gallery

**Context**: Load the page where portfolio images are displayed.

After saving, ensure you are redirected to or manually navigate to the profile/gallery view showing the uploaded images.

> Images and captions render; inspect source to verify payload presence if needed.

### Step 2: Interact with Image

**Context**: Trigger rendering of the caption via user action.

Locate the uploaded image and click on it to open or expand the view, which loads the full caption HTML.

> Caption injects into DOM; onerror fires due to invalid src='x'.

### Step 3: Observe Execution

**Context**: Validate the payload's effect.

Watch for the alert dialog popping up with the document domain (e.g., 'experts.shopify.com').

> Alert confirms execution; in a real attack, replace alert with data exfiltration code.

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
- [[trigger]]
- [[Execution]]
- [[shopify]]
