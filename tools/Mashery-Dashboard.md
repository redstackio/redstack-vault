---
url: 'https://www.mashery.com/'
tags:
  - api-management
  - portal-config
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.511Z'
id: 9083b16f-8df1-4567-9bf4-c9e281b779cc
validated: true
submitted: true
---
# Mashery-Dashboard

**Status**: Unverified

## Overview

Mashery is an API management platform with a web dashboard for configuring portals, adding custom domains, and editing content, exploited here for subdomain takeovers.

## Description

The dashboard allows trial users to claim unvalidated domains via Portal Settings, enabling content hosting. It's used to add the target subdomain and inject JS without checks.

## Features

- Feature 1: Custom domain addition without verification
- Feature 2: Portal page editing for HTML/JS
- Feature 3: Trial account for quick access

## Installation

### Requirements

- Web browser
- Email for signup

### Install Commands

No installation; access via web at https://www.mashery.com/.

## Basic Usage

Login and navigate to Portal Settings.

### Common Options

| Option | Description |
|--------|-------------|
| Add Domain | Input custom subdomain |
| Edit Page | Modify welcome content |

## Examples

### Example 1: Basic Usage

Add developer.openapi.starbucks.com in Portal Settings.

### Example 2: Advanced Usage

Edit welcome page: Add <script>alert(document.domain)</script>.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Logs of domain additions on Mashery
- Unexpected content on subdomains

## Related Procedures


## Related Tools

- [[tools/Browser]]

## References

- Mashery documentation (archived, as service discontinued)
