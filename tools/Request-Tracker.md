---
id: tool-request-tracker
url: 'https://bestpractical.com/request-tracker'
tags:
  - ticketing
  - support-system
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:12.626Z'
validated: true
submitted: true
---
# Request-Tracker

**Status**: Unverified

## Overview

Request Tracker (RT) is an open-source ticketing system used for managing support requests, commonly integrated with platforms like Weblate for handling user inquiries. In security testing, it's often targeted due to vulnerabilities in input handling, such as HTML injection in form processing.

## Description

RT provides a web-based interface for creating, viewing, and managing tickets, with email integration for notifications. It stores ticket content in a database and renders it in HTML views. Vulnerable versions fail to sanitize user inputs, allowing HTML/JS injection that executes in admin contexts. Used in offensive ops to poison tickets for tracking or escalation.

## Features

- Feature 1: Ticket creation via web forms and email
- Feature 2: Admin panel for viewing and updating tickets with HTML rendering
- Feature 3: Email notifications that may embed or link to ticket content

## Installation

### Requirements

- Perl environment
- PostgreSQL or MySQL database
- Apache or Nginx web server

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt-get install request-tracker4
# Configure via web installer at http://localhost/rtinstaller
```

## Basic Usage

```bash
rt-server  # Start RT server (after config)
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help for RT commands |
| `-c, --config` | Specify config file |

## Examples

### Example 1: Basic Usage

Access the web interface at http://your-host/rt to create/view tickets.

### Example 2: Advanced Usage

```bash
rt --dump-config  # View current configuration
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTML in ticket databases
- Outbound requests from RT servers to unknown external images
- Log entries for unsanitized form submissions

## Related Procedures


## Related Tools

- [[Weblate]]

## References

- Official documentation: https://bestpractical.com/request-tracker/documentation
- Related resources: Weblate integration docs
