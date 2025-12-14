---
id: tool-mandygreencps
url: 'https://mandygreencps.com'
tags:
  - redirect
  - dos
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.615Z'
validated: true
submitted: true
---
# mandygreencps-com

**Status**: Unverified

## Overview

Custom domain hosting redirect chains for testing SSRF redirect handling and DoS amplification.

## Description

Hosts HTML files like redir1.html with infinite or long redirect loops to exploit max_redirects in backends.

## Features

- Feature 1: Configurable redirect chains
- Feature 2: Protocol/port switching in chains

## Installation

Host your own similar site.

## Basic Usage

Access /redir1.html in SSRF URL.

## Examples

### Example 1: Basic Usage

https://mandygreencps.com/redir1.html for 30 redirects.

## MITRE ATT&CK Mapping

### Techniques

- [[Network Denial of Service]]

### Tactics

- [[Impact]]

## Detection

- High outbound requests to the domain

## Related Procedures

- [[procedures/Test-Redirect-Handling-for-DoS-Amplification]]

## Related Tools


## References

- https://mandygreencps.com
