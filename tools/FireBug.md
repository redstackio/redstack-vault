---
id: tool-firebug-37822
url: 'https://getfirebug.com/'
tags:
  - browser-extension
  - inspection
  - debugging
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.587Z'
validated: true
submitted: true
---
# FireBug

**Status**: Unverified

## Overview

FireBug is a legacy browser extension for Firefox that provides advanced debugging, inspection, and editing capabilities for web pages, commonly used in security testing to analyze HTTP requests, DOM elements, and cookies during vulnerability assessments like authentication flaws.

## Description

FireBug, developed for Firefox, allows real-time inspection of network traffic, JavaScript execution, HTML/CSS, and browser storage including cookies. In offensive security, it's used to examine session artifacts post-authentication, such as long-lived cookies in login vulnerabilities. Though deprecated in favor of built-in DevTools (post-Firefox 50), it was pivotal in early web pentesting for its comprehensive panels. It supports breaking on network events and editing responses, aiding in the discovery of misconfigurations like extended cookie expirations.

## Features

- Feature 1: Network panel for monitoring HTTP requests/responses and cookie setting
- Feature 2: Console for JavaScript debugging and DOM manipulation
- Feature 3: Storage inspector for viewing cookies, localStorage, and session data

## Installation

### Requirements

- Firefox browser (versions prior to 57; legacy use via add-ons)
- Note: Modern alternative is Firefox Developer Tools

### Install Commands

```bash
# No CLI install; download from add-ons.mozilla.org
# Or use: firefox --install-global-extension firebug.xpi
```

## Basic Usage

```bash
tool-name --help
```

Open FireBug via browser toolbar or right-click 'Inspect Element with FireBug'.

### Common Options

| Option | Description |
|--------|-------------|
| Enable/Disable | Toggle via Firefox Add-ons manager |
| Net Panel | Filter by type (e.g., cookies) |
| Console | Clear logs or persist across reloads |

## Examples

### Example 1: Basic Usage

After login, open FireBug > Net tab > Inspect POST to /sessions for cookie headers.

### Example 2: Advanced Usage

In Cookies panel, search for 'auth_token' and view expiration: right-click > Copy value for analysis.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[JavaScript]] JavaScript (for DOM inspection)

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of FireBug extension in browser profiles
- Anomalous network inspection logs or console errors in web apps
- User-agent strings or extension artifacts in traffic

## Related Procedures


## Related Tools

- [[Firefox Developer Tools]]
- [[Chrome DevTools]]

## References

- Official documentation: https://getfirebug.com/wiki/
- Related resources: Mozilla Add-ons archive
