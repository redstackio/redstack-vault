---
id: tool-xss-swf
url: 'https://github.com/evilcos/xss.swf/blob/master/xss_source.txt'
name: xss.swf
tags:
  - flash
  - xss
  - cross-domain
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.612Z'
validated: true
submitted: true
---
# xss.swf

**Status**: Unverified

## Overview

xss.swf is a proof-of-concept Flash SWF file for testing cross-domain access and policy enforcement, often referenced in vulnerability reports like Vimeo's to validate Flash-based bypasses for XSS or CSRF scenarios.

## Description

This open-source SWF, available on GitHub, demonstrates how Flash can request crossdomain.xml and perform unauthorized cross-origin actions. In the Vimeo report, it's cited as a validation tool to confirm that Vimeo's policy prevents response reading post-exploit, but allows request issuance. Useful for red teaming legacy web apps still supporting Flash, focusing on domain policy manipulation.

## Features

- Feature 1: Automatic crossdomain.xml fetching for policy checks.
- Feature 2: Basic cross-site scripting simulation via Flash.
- Feature 3: Source code transparency for custom modifications.

## Installation

### Requirements

- Git for cloning repository.
- Flash compiler if modifying source.

### Install Commands

```bash
# Clone the repo
git clone https://github.com/evilcos/xss.swf.git
# Use as-is or compile from xss_source.txt
```

## Basic Usage

Host the SWF and load in browser to test cross-domain access.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Configured via source ActionScript |

## Examples

### Example 1: Basic Policy Test

Load https://attacker.com/xss.swf; it requests target/crossdomain.xml.

### Example 2: XSS Simulation

Modify source to inject script post-policy check:

```actionscript
// From xss_source.txt example
var policyLoader:URLLoader = new URLLoader(new URLRequest("https://target.com/crossdomain.xml"));
// Proceed to XSS payload if permitted
ExternalInterface.call("alert", "XSS via Flash");
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript (via Flash bridge)
- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: SWF requests to crossdomain.xml from unknown sources.
- Detection method 2: Flash plugin activity in modern browsers (rare, flagged by EDR).

## Related Procedures


## Related Tools

- [[tools/Flash-SWF]]

## References

- GitHub: https://github.com/evilcos/xss.swf
- Vimeo HackerOne Report #44146
