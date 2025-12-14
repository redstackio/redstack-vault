---
id: t-crossdomain-xml
url: null
tags:
  - flash
  - policy
  - cors-bypass
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.804Z'
validated: true
submitted: true
---
# crossdomain.xml

**Status**: Unverified

## Overview

An XML policy file for Adobe Flash to permit cross-origin requests, used in CSRF exploits to relax security restrictions.

## Description

Placed at server root, it allows SWF files to access resources from other domains, enabling the POST to PHP proxy in the Federalist attack.

## Features

- Defines access policies for Flash
- Supports wildcard domains
- Essential for cross-origin in legacy Flash

## Installation

### Requirements

- Web server hosting SWF

### Install Commands

Upload to /crossdomain.xml

## Basic Usage

<?xml version="1.0"?><cross-domain-policy><allow-access-from domain="*" to-ports="*"/></cross-domain-policy>

### Common Options

| Option | Description |
|--------|-------------|
| domain | Allowed origins (e.g., *) |
| to-ports | Permitted ports |

## Examples

### Example 1: Permissive Policy

<cross-domain-policy><allow-access-from domain="*"/></cross-domain-policy>

### Example 2: Restricted

<allow-access-from domain="attacker.com"/>

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of crossdomain.xml with permissive policies
- Flash requests referencing it
- Security scans for Flash policies

## Related Procedures


## Related Tools

- [[tools/Flash-SWF-File]]

## References

- Adobe crossdomain policy docs
