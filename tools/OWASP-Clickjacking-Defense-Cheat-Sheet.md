---
url: 'https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet'
tags:
  - reference
  - defense
  - clickjacking
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-05T00:00:00Z'
updated_at: '2025-12-14T17:28:12.571Z'
id: 2c69e9cf-ea0d-47e1-a40b-4b2b9081389d
validated: true
submitted: true
---
# OWASP-Clickjacking-Defense-Cheat-Sheet

**Status**: Unverified

## Overview

The OWASP Clickjacking Defense Cheat Sheet is a comprehensive reference guide for understanding and implementing defenses against clickjacking attacks, including browser support for X-Frame-Options and alternative protections like CSP.

## Description

This resource details how to configure headers to prevent UI redressing, explains deprecated directives like ALLOW-FROM, and provides code snippets for secure implementations. It is commonly used in offensive security to validate vulnerabilities and in defensive operations to harden applications.

## Features

- Feature 1: Browser compatibility tables for X-Frame-Options values
- Feature 2: CSP frame-ancestors directive examples
- Feature 3: Detection and testing methods for clickjacking

## Installation

### Requirements

- Web browser for access

### Install Commands

No installation; access via URL.

## Basic Usage

Browse to the URL and search for specific sections like 'X-Frame-Options'.

### Common Options

N/A (web-based reference)

## Examples

### Example 1: Basic Usage

Read the section on 'Browser Support' to confirm Chrome ignores ALLOW-FROM.

### Example 2: Advanced Usage

Use examples to implement CSP: Content-Security-Policy: frame-ancestors 'self';

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- N/A (reference material)

## Related Procedures

- [[procedures/Inspect-HTTP-Response-Headers-for-X-Frame-Options]]

## Related Tools

- [[Burp Suite]]

## References

- Official OWASP documentation
