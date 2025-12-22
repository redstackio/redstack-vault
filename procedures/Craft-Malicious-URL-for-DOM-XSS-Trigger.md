---
id: proc-uuid-1
tags:
  - xss
  - url-crafting
  - payload-injection
type: procedure
tools:
  - '[[tools/Eval-Villain]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:15.774Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-URL-for-DOM-XSS-Trigger

## Summary

This procedure crafts a URL for Urban Dictionary's define.php endpoint that includes a single quote in the 'term' parameter to escape the JavaScript string context in third-party ad scripts, enabling DOM-based XSS.

## Description

In the attack scenario, the site's ad integration passes the current page URL to ad scripts like pwt.js without escaping single quotes. By injecting a payload in the URL parameter, attackers break out of the string and execute code. This targets web browsers accessing the public site, with outcomes including arbitrary JS execution under the site's origin. Prerequisites include basic knowledge of JavaScript string escaping and access to a browser.

## Requirements

1. Access to a web browser (Firefox recommended for tool compatibility).
2. Understanding of URL encoding and JavaScript payloads.
3. No credentials required; public site access suffices.

## Defense

Defensive measures and detection strategies:

- Sanitize and escape URLs before injecting into JavaScript strings in ad scripts.
- Use double quotes or proper encoding for string delimiters in third-party integrations.
- Monitor browser console for unexpected eval or document.write calls via content security policies.

## Objectives

1. Create a URL that triggers string breakout in ad injections.
2. Prepare for payload execution without altering site functionality.
3. Validate payload syntax for reliable escape.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Confirm the define.php page loads ads that inject the URL parameter.

Visit https://www.urbandictionary.com/define.php?term=test in the browser to observe ad loading.

> This step verifies the environment; expect ads from lijit.com or similar to appear.

### Step 2: Construct Payload

**Context**: Build the term parameter with an escape sequence and payload.

Form the URL: https://www.urbandictionary.com/define.php?term=#asdf'-alert(document.domain)-'asdf

> The single quote after #asdf' escapes the ad's url='...' string, inserting alert(document.domain) as executable code, closed by -'asdf to balance the string.

### Step 3: Test URL Formation

**Context**: Ensure the URL is valid and loads without errors.

Paste the crafted URL into the browser address bar and press enter.

> Expected: Page loads with search results; no 404 or syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Eval-Villain]]

## Tags

- [[xss]]
- [[dom-xss]]
- [[url-injection]]
