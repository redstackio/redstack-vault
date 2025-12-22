---
id: e4d02609-e3d7-4809-b00b-439611b07930
name: host-query-name-servers
type: command
executor: bash
data: host -t ns $_DOMAIN
output: null
created_at: '2023-04-06T03:56:21.778539+00:00'
updated_at: '2023-04-10T20:21:18.291933+00:00'
platforms:
  - Linux
tags:
  - dns
  - recon
verified: true
validated: true
---

# host-query-name-servers

## Command

```bash
host -t ns $_DOMAIN
```

## Description

This command queries the DNS for name server (NS) records of a target domain, identifying the authoritative DNS servers that manage the zone. Use this during reconnaissance to find entry points for further DNS enumeration like zone transfers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The target domain name (e.g., example.com) | Yes |
| -t ns | Specifies the query type for name server records | Built-in |

## Examples

### Basic Usage

```bash
host -t ns example.com
```

### Advanced Usage

For verbose output:
```bash
host -t ns -v example.com
```

## Expected Output

example.com name server ns1.example.com.
example.com name server ns2.example.com.

This lists the authoritative name servers for the domain.

## Related

- [[procedures/DNS-Zone-Transfer-Enumeration]]
- [[commands/host-resolve-master-ip]]
