---
id: proc-inject-xss-payload-informatica-search
tags:
  - xss
  - payload-injection
  - session-storage
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T03:16:25.173Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Informatica-Search-Session

## Summary

This procedure injects a malicious JavaScript payload into the 'k' search parameter of the Informatica KB search results page, causing it to be stored in the user's session as part of the `varSearchResultURL` variable for later exploitation.

## Description

The Informatica Knowledge Base (kb.informatica.com) stores user search queries in the session without proper sanitization. By appending a JavaScript-breaking payload to the 'k' parameter, an attacker can taint the session-stored URL. This sets up a stored XSS attack where the payload will be reflected unescaped in JavaScript on subsequent pages. The target environment is a .NET-based web application running on port 7001. Prerequisites include a web browser and direct access to the site; no authentication is needed.

## Requirements

1. Web browser like Firefox for navigation and payload delivery
2. Direct network access to https://kb.informatica.com on port 7001
3. No credentials or prior session required

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding for all user inputs reflected in JavaScript (e.g., use HTML entity encoding for strings in JS contexts)
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous search queries containing script tags or breaking characters like ';'

## Objectives

1. Store malicious payload in session for persistence across pages
2. Prepare for JavaScript injection without immediate detection
3. Enable arbitrary code execution on victim browsers

## Instructions

### Step 1: Craft and Visit Search URL

**Context**: Construct the search URL with the URL-encoded payload to inject into the 'k' parameter, simulating a legitimate search while appending the XSS terminator and script.

No command-line tool is used; perform this in the browser.

> Visit the following URL in Firefox: https://kb.informatica.com/kbexternal/Pages/KBSearchResults.aspx?k=Support%20Console&fromsource=11171%22%3balert(1)%2f%2f535

> The payload '%22%3balert(1)%2f%2f535' decodes to ";alert(1)//535", which breaks out of the string in `varSearchResultURL` and injects the alert. The page loads normally, but the session now holds the tainted data.

### Step 2: Verify Session Storage

**Context**: Confirm the injection by inspecting the page source or proceeding to the trigger page; no visible alert occurs here.

> Check the browser's developer tools (F12) for any immediate JS errors, but expect none. The payload is silently stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- injection
