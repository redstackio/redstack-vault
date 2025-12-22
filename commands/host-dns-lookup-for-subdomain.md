---
id: cmd-uuid-001
data: host odoo-staging.exness.io
tags:
  - dns
  - reconnaissance
  - subdomain-takeover
type: command
output: >-
  odoo-staging.exness.io is an alias for exness-stg.odoo.com.
  exness-stg.odoo.com has address 141.95.172.222 exness-stg.odoo.com mail is
  handled by 10 eu123a.odoo.com.
executor: bash
platforms:
  - Linux
  - macOS
  - Unix
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.998Z'
verified: false
validated: true
submitted: true
---
# host DNS Lookup for Subdomain

## Command

```bash
host odoo-staging.exness.io
```

## Description

The 'host' command performs a DNS lookup on a specified hostname, retrieving records such as A (IP addresses), CNAME (aliases), and MX (mail exchangers). It is used in reconnaissance to detect subdomain takeover vulnerabilities by identifying dangling CNAME records pointing to unused services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | The domain or subdomain to query (e.g., odoo-staging.exness.io) | Yes |

## Examples

### Basic Usage

```bash
host odoo-staging.exness.io
```

### Advanced Usage

```bash
host -t CNAME odoo-staging.exness.io
```

This specifies querying only CNAME records.

## Expected Output

odoo-staging.exness.io is an alias for exness-stg.odoo.com. exness-stg.odoo.com has address 141.95.172.222 exness-stg.odoo.com mail is handled by 10 eu123a.odoo.com.

A CNAME alias indicates potential takeover if the target service is unused.

## Related

- [[Related Procedure: Detect Subdomain Takeover with DNS Lookup]]
