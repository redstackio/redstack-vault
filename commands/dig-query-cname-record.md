---
data: dig email.smule.com CNAME
tags:
  - dns
  - recon
type: command
output: |-
  ;; ANSWER SECTION:
  email.smule.com. 3600 IN CNAME something.sendgrid.net.
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.370Z'
id: 64200264-db6a-44c2-98af-3be993e95cac
verified: false
validated: true
submitted: true
---
# dig-query-cname-record

## Command

```bash
dig email.smule.com CNAME
```

## Description

This command queries the DNS for the CNAME record of a specific subdomain, useful for identifying dangling records in subdomain takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | The subdomain to query (e.g., email.smule.com) | Yes |
| CNAME | Record type to fetch (CNAME for aliases) | Yes |

## Examples

### Basic Usage

```bash
dig email.smule.com CNAME
```

### Advanced Usage

```bash
dig +short email.smule.com CNAME
```

## Expected Output

DNS response with ANSWER SECTION showing the CNAME target, such as pointing to sendgrid.net, indicating a potential takeover vector.

## Related

- [[Related Procedure: Query-DNS-for-CNAME-Record]]
