---
url: >-
  https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html#character-escape-sequences
tags:
  - xss
  - evasion
  - reference
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.109Z'
id: 15d75f54-8267-46ca-9db4-cd85d0813af0
validated: true
submitted: true
---
# OWASP-XSS-Filter-Evasion-Cheat-Sheet

**Status**: Unverified

## Overview

The OWASP XSS Filter Evasion Cheat Sheet is a reference guide for crafting payloads that bypass web application filters, particularly useful for exploiting reflected XSS vulnerabilities through encoding techniques.

## Description

This resource details methods like HTML entity encoding, Unicode escapes, and polyglot payloads to evade sanitization. In security testing, it's used to develop effective XSS exploits against filtered inputs, such as URL parameters in applications like Glassdoor.

## Features

- Feature 1: Comprehensive list of evasion techniques including decimal and hex entities
- Feature 2: Examples for SVG, script tags, and event handlers
- Feature 3: categorized by filter type for targeted bypass

## Installation

### Requirements

- Web browser for access

### Install Commands

No installation required; access via URL.

## Basic Usage

Visit the URL in a browser and search for relevant sections like "Character Escape Sequences".

### Common Options

N/A (web-based reference)

## Examples

### Example 1: Basic Usage

Browse to https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html and review encoded alert payloads.

### Example 2: Advanced Usage

Use the sheet to encode: alert(1) as &#x00000000061;lert(1) for SVG onload.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Web traffic to OWASP cheat sheet domains from testing environments
- Payloads in logs matching known evasion patterns from the sheet

## Related Procedures


## Related Tools

- [[tools/Chrome]]

## References

- Official documentation: https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html
- Related resources: OWASP XSS Prevention Cheat Sheet
