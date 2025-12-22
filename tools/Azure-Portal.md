---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567896
url: 'https://portal.azure.com'
tags:
  - cloud-management
  - azure
type: tool
verified: false
platforms:
  - Web
  - Azure
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:38:49.786Z'
validated: true
submitted: true
---
# Azure Portal

**Status**: Unverified

## Overview

The Azure Portal is a web-based interface for managing Microsoft Azure cloud resources, commonly used in offensive security for provisioning services, deploying applications, and exploiting misconfigurations like subdomain takeovers.

## Description

It provides a dashboard for creating Cloud Services, Storage Accounts, and deploying packages. In attacks, it's used to claim unclaimed domains and host malicious content, as seen in hijacking .cloudapp.net subdomains.

## Features

- Feature 1: Resource creation and management (e.g., Cloud Services, Storage)
- Feature 2: Deployment uploads for web apps
- Feature 3: Monitoring and configuration of DNS-integrated services

## Installation

### Requirements

- Web browser (Chrome, Edge)
- Azure subscription

### Install Commands

No installation; access via browser.

## Basic Usage

```bash
# No CLI; use web UI
```

### Common Options

| Option | Description |
|--------|-------------|
| Create Resource | Search and provision new services |
| Upload Package | Deploy apps to Cloud Services |

## Examples

### Example 1: Basic Usage

Navigate to portal.azure.com > Sign in > Search 'Cloud Services' > Create with domain name.

### Example 2: Advanced Usage

Create Storage: Portal > Storage Accounts > Create > Configure replication.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Azure resource creations from unknown IPs
- API logs showing domain registrations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Visual-Studio]]

## References

- Official documentation: https://docs.microsoft.com/azure/
- Azure security best practices
