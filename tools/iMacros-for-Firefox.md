---
url: 'https://addons.mozilla.org/en-US/firefox/addon/imacros-for-firefox/'
tags:
  - automation
  - browser
type: tool
verified: false
platforms:
  - Web
  - Firefox
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.770Z'
id: 92032d48-46da-4685-a4dc-ffc47251451a
validated: true
submitted: true
---
# iMacros-for-Firefox

**Status**: Unverified

## Overview

iMacros for Firefox is a browser extension for automating repetitive web tasks, commonly used in security testing to script UI interactions like form submissions, clicks, and data extraction without full programming.

## Description

This tool records and replays browser actions using a simple scripting language with TAG commands for elements, WAIT for delays, and EVAL for JavaScript integration (e.g., AJAX calls). In offensive security, it's ideal for automating web app exploits involving manual UI steps, such as refreshing tokens or cycling authentications in SaaS platforms like Shopify.

## Features

- Feature 1: Record/playback of mouse/keyboard actions
- Feature 2: Scripting with loops, variables, and conditional logic
- Feature 3: JavaScript execution for API calls and data manipulation

## Installation

### Requirements

- Firefox browser version 78+
- No additional dependencies

### Install Commands

No CLI install; manual:

Visit https://addons.mozilla.org/en-US/firefox/addon/imacros-for-firefox/ > Click 'Add to Firefox' > Confirm.

## Basic Usage

```imacros
VERSION BUILD=10021450
TAG POS=1 TYPE=A ATTR=TXT:Click<SP>Me
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | N/A (UI-based) |
| !LOOP | Set loop count |

## Examples

### Example 1: Basic Usage

Record clicking a button: iMacros > Record > Perform action > Stop > Play.

### Example 2: Advanced Usage

Script with loop and API: As in [[commands/imacros-refresh-flow-url]] for Shopify exploit.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Valid Accounts]]

### Tactics

- [[Execution]]
- [[Persistence]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual browser extensions in session logs
- Pattern of automated clicks/delays in web app access logs
- JavaScript EVAL calls to external APIs from admin pages

## Related Procedures

- [[procedures/Automate-Persistent-Access-with-iMacros]]

## Related Tools

- [[Selenium]]
- [[Puppeteer]]

## References

- Official documentation: https://imacros.net/
- Firefox Add-ons page
