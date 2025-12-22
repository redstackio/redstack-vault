---
url: 'https://www.canarytokens.org'
tags:
  - canary
  - detection
  - callback
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.517Z'
id: 055c2a16-8ded-4527-878f-7ab0fd4761d3
validated: true
submitted: true
---
# Canarytokens

**Status**: Unverified

## Overview

Canarytokens is a free service for generating unique 'canary' tokens that alert on unauthorized access or callbacks, commonly used in red teaming to detect exploitation like JNDI lookups in Log4Shell attacks.

## Description

It creates disposable domains or URLs that, when accessed, notify the owner via email or dashboard. In security testing, it's perfect for confirming remote interactions, such as LDAP queries from vulnerable servers, without maintaining infrastructure.

## Features

- Feature 1: Multiple token types (DNS, HTTP, LDAP, etc.)
- Feature 2: Instant alerts on hits with source details
- Feature 3: No setup required, web-based generation

## Installation

### Requirements

- Web browser and internet access
- Optional: Email for alerts

### Install Commands

```bash
# No installation; use web interface
# Self-host option via GitHub repo
curl -sSL https://github.com/thinkst/canarytokens | bash
```

## Basic Usage

```bash
# Web-based; no CLI
```

### Common Options

| Option | Description |
|--------|-------------|
| Token Type | Select LDAP for JNDI |
| Custom Domain | Optional branding |

## Examples

### Example 1: Basic Usage

Generate an LDAP token on the site and use the domain in payloads.

### Example 2: Advanced Usage

Monitor dashboard for hits post-exploitation.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]
- [[Remote Access Tools]]

### Tactics

- [[Reconnaissance]]
- [[Command and Control]]

## Detection

Indicators and methods for detecting this tool's usage:

- DNS queries to unusual canary domains
- Outbound connections to thinkst.com subdomains
- Alert emails from Canarytokens

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://docs.canarytokens.org
- Related resources: Thinkst Applied Research
