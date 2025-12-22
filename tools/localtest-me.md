---
id: tool-localtest-me
url: 'http://localtest.me'
tags:
  - rebinding
  - ssrf
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.617Z'
validated: true
submitted: true
---
# localtest-me

**Status**: Unverified

## Overview

Domain that resolves to 127.0.0.1 for localhost testing and rebinding in SSRF scenarios.

## Description

localtest.me rebinds to localhost, useful for disclosing internal proxy details without direct IP usage.

## Features

- Feature 1: Automatic localhost resolution
- Feature 2: Supports port specification

## Installation

Web-based.

## Basic Usage

http://localtest.me:80

## Examples

### Example 1: Basic Usage

Use in SSRF URL for proxy leak.

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

- Requests to localtest.me from backend

## Related Procedures

- [[procedures/Disclose-Squid-Proxy-Details-via-Local-Rebinding]]

## Related Tools

- [[tools/nip-io]]

## References

- http://localtest.me
