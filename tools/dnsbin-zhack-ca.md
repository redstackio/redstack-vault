---
url: 'http://dnsbin.zhack.ca/'
tags:
  - dns
  - exfiltration
  - logging
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.987Z'
id: d7959d10-27e9-47f1-a7fa-c50e0c441e7a
validated: true
submitted: true
---
# dnsbin.zhack-ca

**Status**: Unverified

## Overview

dnsbin.zhack.ca is an online DNS logging service that allows users to create temporary domains for capturing incoming DNS queries, ideal for observing exfiltration in RCE exploits.

## Description

This web-based tool provides a simple interface to generate subdomains and view real-time query logs, useful in red teaming to confirm server-side execution without complex setup.

## Features

- Feature 1: Instant subdomain creation for logging
- Feature 2: Real-time query visualization with source IPs
- Feature 3: No installation required; browser-based

## Installation

### Requirements

- Web browser

### Install Commands

N/A (web service)

## Basic Usage

Access http://dnsbin.zhack.ca/ and create a bin.

### Common Options

N/A

## Examples

### Example 1: Basic Usage

1. Visit site, generate subdomain (e.g., abc.dnsbin.zhack.ca)
2. Use subdomain in payload
3. Monitor logs for queries

### Example 2: Advanced Usage

Embed in EL payload and observe after exploit.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- DNS queries to *.dnsbin.zhack.ca domains
- External logging services in exploit traffic

## Related Procedures


## Related Tools

- [[Burp Collaborator]]

## References

- Site: http://dnsbin.zhack.ca/
