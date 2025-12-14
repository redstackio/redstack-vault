---
id: proc-trigger-drive2-xss
tags:
  - xss-execution
  - payload-trigger
  - client-side
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
updated_at: '2025-12-13T23:52:33.530Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Company-Profile-Page

## Summary

This procedure loads the public company profile page on drive2.ru to execute the stored XSS payload, resulting in arbitrary JavaScript running in the context of visiting users' browsers.

## Description

The company page renders the unsanitized 'Company Name' in an HTML context, triggering the onload event of the injected SVG tag. This affects the web platform without further interaction, allowing theft of non-httpOnly cookies, phishing, or redirects, with high impact due to persistence.

## Requirements

1. Saved company profile URL from prior step
2. Victim browser (can be attacker's for testing)
3. No CSP blocking the payload execution

## Defense

Defensive measures and detection strategies:

- Output encoding on all user-controlled data in HTML contexts
- HttpOnly flags on sensitive cookies
- Monitor for anomalous JavaScript alerts or network requests from pages

## Objectives

1. Render the page to execute the payload
2. Observe JavaScript effects (e.g., confirm dialog)
3. Demonstrate impact like domain confirmation

## Instructions

### Step 1: Obtain Profile URL

**Context**: Get the link to the vulnerable company page.

From the management panel or confirmation page, copy the public company profile URL.

> Ensure it's accessible without login.

### Step 2: Load the Page

**Context**: Visit the URL to trigger rendering.

Paste the URL into a browser and navigate to it.

> The page should load normally, with the company name section containing the payload.

### Step 3: Observe Execution

**Context**: Confirm the XSS fires automatically.

Watch for the confirm dialog displaying the domain (drive2.ru).

> Use dev tools console to inspect any additional effects or errors.

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

- xss-execution
- payload-trigger
- client-side
