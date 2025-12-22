---
id: ae1c0e6a-e13e-45ea-9823-36f49df49f8e
name: host-resolve-master-ip
type: command
executor: bash
data: host $_MASTER_SERVER.$_DOMAIN
output: null
created_at: '2023-04-06T03:56:21.778607+00:00'
updated_at: '2023-04-10T20:21:18.291933+00:00'
platforms:
  - Linux
tags:
  - dns
  - recon
verified: true
validated: true
---

# host-resolve-master-ip

## Command

```bash
host $_MASTER_SERVER.$_DOMAIN
```

## Description

This command resolves the IP address of the master (primary) DNS server for a domain, using a standard A record lookup. It's a follow-up to name server queries to obtain the IP needed for zone transfer attempts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MASTER_SERVER.$_DOMAIN | The fully qualified name of the master server (e.g., master.example.com) | Yes |

## Examples

### Basic Usage

```bash
host master.example.com
```

### Advanced Usage

With trace for debugging:
```bash
host -t A master.example.com
```

## Expected Output

master.example.com has address 192.168.1.1

This provides the IPv4 address of the master server.

## Related

- [[procedures/DNS-Zone-Transfer-Enumeration]]
- [[commands/host-query-name-servers]]
