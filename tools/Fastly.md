---
url: 'https://www.fastly.com'
tags:
  - cdn
  - takeover
type: tool
verified: false
platforms:
  - CDN
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.715Z'
id: 517c78db-499f-464d-94dd-2e90c554780e
validated: true
submitted: true
---
# Fastly

**Status**: Unverified

## Overview

Fastly is a content delivery network (CDN) service that can be leveraged in attacks to claim dangling DNS records for subdomain takeovers, routing traffic to attacker-controlled backends.

## Description

In offensive security, Fastly is used to exploit misconfigurations where DNS CNAMEs persist after service cancellation. Attackers create new services to hijack subdomains like fastly.sc-cdn.net, enabling arbitrary content serving.

## Features

- Feature 1: Edge computing and VCL configuration
- Feature 2: Backend server routing
- Feature 3: Global DNS propagation

## Installation

### Requirements

- Fastly account

### Install Commands

No installation; dashboard-based.

## Basic Usage

```bash
# Dashboard: Create new service
```

### Common Options

| Option | Description |
|--------|-------------|
| Service Creation | Assign to dangling CNAME |
| Backend Config | Point to Apache host |

## Examples

### Example 1: Basic Usage

Create service and set domain to fastly.sc-cdn.net.

### Example 2: Advanced Usage

Configure VCL to route /takeover.html to custom backend.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unauthorized services in Fastly dashboard
- DNS changes to Fastly endpoints

## Related Procedures

- [[procedures/Perform-Subdomain-Takeover-with-Fastly]]

## Related Tools

- [[Cloudflare]]
- [[AWS CloudFront]]

## References

- Official documentation: https://docs.fastly.com
- Related resources: CDN Misconfiguration Guides
