---
id: tool-css-keylogging-001
url: 'https://github.com/maxchehab/CSS-Keylogging/'
tags:
  - css
  - keylogging
  - exfiltration
type: tool
verified: false
platforms:
  - Web
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:33.508Z'
validated: true
submitted: true
---
# CSS-Keylogging

**Status**: Unverified

## Overview

CSS-Keylogging is a proof-of-concept tool demonstrating keystroke capture using only CSS selectors and attributes, without JavaScript. It's useful in security testing for client-side attacks like CSS injection in apps such as Slack, where it can target message inputs for exfiltration.

## Description

This GitHub repository showcases CSS-based keylogging by leveraging attribute selectors (e.g., `[value^="a"]:focus`) to style elements based on input values, enabling logging of typed characters. In offensive operations, it's applied to scenarios with CSS injection vulnerabilities to exfiltrate data like chat messages. No runtime execution; it's educational for PoC development.

## Features

- Feature 1: Pure CSS keystroke detection via focus and value selectors
- Feature 2: No JavaScript dependency, evading common script blockers
- Feature 3: Applicable to form inputs in webviews or hybrid apps like Slack

## Installation

### Requirements

- Web browser for demo (e.g., Chrome on macOS)
- Git for cloning repository

### Install Commands

```bash
# Clone the repository
git clone https://github.com/maxchehab/CSS-Keylogging/
cd CSS-Keylogging
```

## Basic Usage

```bash
# Open index.html in a browser to view demo
open index.html  # On macOS
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Demo is static; no CLI options |
| View source | Inspect CSS for custom adaptation |

## Examples

### Example 1: Basic Demo

Open the cloned `index.html` in a browser and type in the input field; observe CSS styles changing per key.

### Example 2: Advanced Usage

Adapt CSS rules for Slack injection: Extend selectors to target message inputs, e.g., `input[type="text"][value^="k"]` for 'k' key, and exfil via styled elements leaking to screenshots or logs.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Keylogging]] Input Capture: Keylogging
- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Tactics

- [[Collection]] Collection
- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual CSS selector complexity in app stylesheets
- Detection method 2: Log input events without JS, flagging CSS-driven behaviors

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: GitHub README
- Related resources: CSS Tricks on attribute selectors
