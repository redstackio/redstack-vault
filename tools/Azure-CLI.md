---
url: 'https://docs.microsoft.com/en-us/cli/azure/'
tags:
  - azure
  - cloud
  - cli
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.806Z'
id: 88969dfb-877a-4564-9d4f-f0a5c09098da
validated: true
submitted: true
---
# Azure-CLI

**Status**: Unverified

## Overview

Azure CLI is a command-line tool for managing Azure resources, commonly used in security testing for creating, querying, and configuring cloud infrastructure like Traffic Manager profiles during subdomain takeover exploits.

## Description

It provides access to Azure APIs for automation, allowing attackers to claim unclaimed resources or audit configurations. In offensive operations, it's used to interact with services like Traffic Manager for hijacking DNS-routed subdomains.

## Features

- Feature 1: Resource creation and management (e.g., az network traffic-manager)
- Feature 2: Querying with JMESPath for reconnaissance
- Feature 3: Cross-platform support with scripting integration

## Installation

### Requirements

- Python 3.6+ or Node.js
- Internet access for installation

### Install Commands

```bash
# On Linux/macOS
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# On Windows
winget install Microsoft.AzureCLI
```

## Basic Usage

```bash
az --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| --output json | JSON output format |
| --query | JMESPath query for filtering |

## Examples

### Example 1: Basic Usage

```bash
az login
az network traffic-manager profile list
```

### Example 2: Advanced Usage

```bash
az network traffic-manager profile create --resource-group rg --name profile --unique-dns-name example.trafficmanager.net
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Acquire Infrastructure]] Acquire Infrastructure
- [[Hardware]] Gather Victim Host Information

### Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Azure sign-ins from CLI user agents in logs
- Alert on az commands in command-line auditing
- Track unusual Traffic Manager creations

## Related Procedures

- [[procedures/Identify-Dangling-Subdomain-DNS-Records]]
- [[procedures/Verify-Unclaimed-Azure-Traffic-Manager-Profile]]
- [[procedures/Claim-Azure-Traffic-Manager-Profile-for-Subdomain-Takeover]]

## Related Tools

- [[AWS-CLI]]
- [[GCP-gcloud]]

## References

- Official documentation: https://docs.microsoft.com/en-us/cli/azure/
- Related resources: Azure Security Center guides
