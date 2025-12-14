---
url: 'https://github.com/nebulade/ldapjstestserver'
tags:
  - ldap
  - simulation
type: tool
verified: false
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.192Z'
id: e860cc07-939d-490f-b265-cff9cba8c832
validated: true
submitted: true
---
# ldapjstestserver

**Status**: Unverified

## Overview

ldapjstestserver.js is a Node.js script simulating an LDAP server for testing authentication in meemo app.

## Description

Runs on localhost:3002; provides mock responses for LDAP binds and searches to reproduce the injection vulnerability.

## Features

- Feature 1: Mock LDAP operations
- Feature 2: Configurable DNs and users
- Feature 3: Port 3002 default

## Installation

### Requirements

- Node.js
- Clone or download script

### Install Commands

```bash
# Assume in meemo dir
# Script is provided in repo
```

## Basic Usage

```bash
node ldapjstestserver.js
```

### Common Options

| Option | Description |
|--------|-------------|
| None specified | Default port 3002 |

## Examples

### Example 1: Basic Usage

```bash
node ldapjstestserver.js
```

### Example 2: Advanced Usage

```bash
node ldapjstestserver.js --port 389
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Port 3002 listening
- Node process with ldapjs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/node]]

## References

- GitHub: https://github.com/nebulade/ldapjstestserver
