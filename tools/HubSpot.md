---
url: 'https://hubspot.com'
tags:
  - hosting
  - subdomain-takeover
type: tool
platforms:
  - Web
description: >-
  Web hosting platform for creating and managing sites, exploitable for
  subdomain takeovers via unclaimed instances
id: 35e9d1d5-ae3c-49e9-a68a-4621c23fece7
created_at: '2025-12-11T06:10:30.440Z'
updated_at: '2025-12-11T06:10:30.440Z'
verified: false
validated: true
submitted: true
---
# HubSpot

**Status**: Unverified

## Overview

HubSpot is a CRM and marketing platform that allows users to create and host websites. In security contexts, it's used for claiming unclaimed instances linked to dangling CNAMEs for subdomain takeovers.

## Description

Provides tools for site building, content management, and hosting. Attackers can register unclaimed sites to control subdomains, hosting malicious PHP/JS for exploits like cookie theft.

## Features

- Site claiming and registration
- Content uploading (HTML, PHP, JS)
- Easy web hosting integration

## Installation

### Requirements

- Web browser
- HubSpot account

### Install Commands

No installation needed; web-based.

## Basic Usage

Access via browser: hubspot.com

### Common Options

| Option | Description |
|--------|-------------|
| Claim Site | Register unclaimed instance |
| Upload Content | Host files on site |

## Examples

### Example 1: Basic Usage

Log in and claim site via dashboard.

### Example 2: Advanced Usage

Upload PHP script for cookie capture.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Compromise Infrastructure]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor DNS changes and HubSpot claims
- Anomalous traffic to new subdomains

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[AWS S3]]
- [[GitHub Pages]]

## References

- Official HubSpot documentation
- Subdomain takeover guides
