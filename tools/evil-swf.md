---
id: tool-vimeo-evil-swf-001
url: 'http://evilsite.com/evil.swf'
tags:
  - malicious-swf
  - csrf-tool
  - token-theft
type: tool
verified: false
platforms:
  - Web
  - Flash
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:36.198Z'
validated: true
submitted: true
---
# evil-swf

**Status**: Unverified

## Overview

evil.swf is a custom malicious Flash file created by attackers to exploit Vimeo's moogaloop.swf by loading it cross-site, stealing XSRF tokens, and executing CSRF requests to modify user settings and video privacy.

## Description

Developed using Adobe Flash authoring tools, this SWF dynamically loads legitimate Vimeo's moogaloop.swf and manipulates its config_url to access protected pages. It parses responses for tokens and sends forged POSTs, enabling full account compromise in offensive security scenarios like red teaming web apps with Flash dependencies.

## Features

- Feature 1: Cross-site loading of external SWFs
- Feature 2: HTTP request interception and parsing
- Feature 3: Automated CSRF POST submission with stolen tokens

## Installation

### Requirements

- Adobe Flash Professional or open-source alternatives like Ming
- Server to host the compiled SWF

### Install Commands

Compile via command line (using Ming):

```bash
# Example compilation (pseudocode; requires Ming setup)
mingc -swf evil.swf evil.as
```

## Basic Usage

Embed in HTML for delivery:

```html
<object data="http://evilsite.com/evil.swf" type="application/x-shockwave-flash"></object>
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Custom ActionScript defines behavior |

## Examples

### Example 1: Basic Usage

Load to initiate token theft:

```html
<embed src="http://evilsite.com/evil.swf">
```

### Example 2: Advanced Usage

Integrate with POC page for display:

```actionscript
// Inside evil.as: load moogaloop and parse
loadMovie("https://f.vimeocdn.com/p/flash/moogaloop/6.3.5/moogaloop.swf", target);
// ... token extraction and POST logic
```

## Expected Output

Token stolen and requests sent; outputs to parent page or console.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Forge Web Credentials]] Forge Web Credentials

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious SWF loads from untrusted domains
- Flash requests to internal endpoints like /settings
- Unexpected account changes post-Flash execution

## Related Procedures


## Related Tools

- [[tools/moogaloop-swf]]
- [[tools/xss-swf]]

## References

- Custom exploit from HackerOne #136481
- Flash exploitation guides
