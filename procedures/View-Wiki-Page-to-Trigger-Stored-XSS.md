---
tags:
  - xss
  - trigger
  - browser
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
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: c66f94e2-864e-43fa-9336-58b60ee1c011
created_at: '2025-12-13T23:52:55.057Z'
updated_at: '2025-12-13T23:52:55.057Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# View Wiki Page to Trigger Stored XSS

## Summary

This procedure involves accessing the updated wiki page in a browser, causing GitLab to render the page with the injected XSS payload from the commit author email, executing arbitrary JavaScript.

## Description

Upon viewing, GitLab's show.html.haml template (line 10) inserts the unsanitized author_url into an <a> tag, allowing attribute injection like onanimationstart=alert(1) to fire on load or interaction, stealing sessions or performing client-side attacks.

## Requirements

1. Pushed malicious commit live on GitLab
2. Victim or tester browser access to the wiki URL
3. No additional auth if wiki is public

## Defense

Defensive measures and detection strategies:

- Apply HTML escaping to author_url in wiki templates (remove .html_safe)
- Implement Content Security Policy (CSP) to block inline JS execution
- Monitor browser console errors and XSS alerts in access logs

## Objectives

1. Execute JS in victim's browser context
2. Collect sensitive data like cookies/sessions
3. Demonstrate impact of stored payload

## Instructions

### Step 1: Access Wiki Page

**Context**: Navigate to the rendered wiki page URL to trigger rendering.

**Command** (Browser Navigation):
No CLI command; open http://gl.local/root/test/-/wikis/home in a browser.

> The page loads, rendering the author link with injected attributes. Expected output: Alert dialog or JS execution visible.

### Step 2: Validate Execution

**Context**: Inspect the page to confirm payload injection.

**Command** (Browser DevTools):
Right-click > Inspect Element, search for author <a> tag.

> Look for injected onanimationstart or similar; console shows JS errors/alerts.

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
- [[trigger]]
- [[browser]]
