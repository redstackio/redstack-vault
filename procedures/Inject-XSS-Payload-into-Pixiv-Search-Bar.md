---
id: proc-pixiv-search-xss-001
tags:
  - xss
  - reflected-xss
  - search-injection
type: procedure
tools:
  - '[[tools/Chrome-iOS-13-1]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.884Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Pixiv-Search-Bar

## Summary

This procedure exploits reflected XSS in pixiv.net's mobile search bar, where input is reflected into the tags endpoint URL without validation, enabling JavaScript execution on search results page load.

## Description

On the mobile version via Chrome iOS 13.1, entering a payload in the search bar redirects to /en/tags/[payload]#discover, executing the script due to lack of input sanitization. This allows arbitrary code like confirm dialogs, extending the attack surface beyond direct URLs to user-driven searches.

## Requirements

1. Access to pixiv.net mobile site on iOS 13.1 Chrome.
2. No login required.
3. Payload knowledge for confirmation testing.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize search inputs server-side, rejecting special characters.
- Use URL encoding and escape user input in redirects.
- Log and alert on search queries containing script tags or event handlers.

## Objectives

1. Confirm XSS in search reflection.
2. Execute code via tags endpoint.
3. Prepare for broader payload delivery in phishing.

## Instructions

### Step 1: Enter Payload in Search Bar

**Context**: Input triggers redirect to vulnerable tags URL.

Using [[tools/Chrome-iOS-13-1]], enter in search bar:

```text
['-confirm(3)-']
```

> This generates https://www.pixiv.net/en/tags/['-confirm(3)-']#discover and executes on load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-iOS-13-1]]

## Tags

- [[xss]]
- [[search-injection]]
