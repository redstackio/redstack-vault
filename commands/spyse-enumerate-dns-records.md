---
id: 8301cb6e-e854-461e-9a31-45736f5127cc
name: spyse-enumerate-dns-records
type: command
executor: bash
data: spyse -target $_TARGET_DOMAIN --dns-all
output: null
created_at: '2023-04-06T03:56:22.173430+00:00'
updated_at: '2023-04-10T20:25:09.108205+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
verified: true
validated: true
---

# spyse-enumerate-dns-records

## Command

```bash
spyse -target $_TARGET_DOMAIN --dns-all
```

## Description

This command uses the Spyse CLI to query the Spyse API for all DNS record types associated with a target domain. It performs passive reconnaissance to gather A, AAAA, CNAME, MX, NS, PTR, SOA, SRV, and TXT records without direct interaction with the target's DNS servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DOMAIN | The domain name to enumerate (e.g., example.com) | Yes |
| -target | Specifies the target domain for the query | Yes |
| --dns-all | Retrieves all available DNS record types | Yes |

## Examples

### Basic Usage

```bash
spyse -target example.com --dns-all
```

### Advanced Usage

```bash
spyse -target example.com --dns-all | jq '.records'
```

## Expected Output

The command returns JSON output listing DNS records:

```
{
  "records": [
    {
      "name": "example.com",
      "type": "NS",
      "value": "ns1.example.com"
    },
    {
      "name": "www.example.com",
      "type": "A",
      "value": "192.0.2.1"
    },
    {
      "name": "mail.example.com",
      "type": "MX",
      "value": "10 mailserver.example.com"
    }
  ]
}
```

Success is indicated by a non-empty records array without API errors.

## Related

- [[procedures/Enumerate-DNS-Records-with-Spyse]]
- [[tools/Spyse]]
