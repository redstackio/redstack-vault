---
id: 01996e7d-2f73-4004-b3b0-13790da90e67
name: dig-perform-zone-transfer
type: command
executor: bash
data: dig axfr $_DOMAIN @$_MASTER_IP
output: null
created_at: '2023-04-06T03:56:21.778678+00:00'
updated_at: '2023-04-10T20:21:18.291933+00:00'
platforms:
  - Linux
tags:
  - dns
  - recon
verified: true
validated: true
---

# dig-perform-zone-transfer

## Command

```bash
dig axfr $_DOMAIN @$_MASTER_IP
```

## Description

This command attempts a full DNS zone transfer (AXFR) from the specified authoritative server, downloading all records if permitted. It's a key reconnaissance tool to enumerate subdomains and hosts when DNS is misconfigured.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| axfr | Requests a zone transfer | Built-in |
| $_DOMAIN | The target domain (e.g., example.com) | Yes |
| @$_MASTER_IP | The IP address of the target DNS server (e.g., @192.168.1.1) | Yes |

## Examples

### Basic Usage

```bash
dig axfr example.com @192.168.1.1
```

### Advanced Usage

With short output:
```bash
dig +short axfr example.com @192.168.1.1
```

## Expected Output

example.com.          3600  IN  SOA  ns1.example.com. admin.example.com. (
                        2023010101 ; serial
                        3600       ; refresh (1 hour)
                        1800       ; retry (30 minutes)
                        604800     ; expire (1 week)
                        86400      ; minimum (1 day)
                        )
sub1.example.com.     3600  IN  A    192.168.1.10
sub2.example.com.     3600  IN  A    192.168.1.11

On failure: ;; Transfer failed.

## Related

- [[procedures/DNS-Zone-Transfer-Enumeration]]
- [[commands/host-resolve-master-ip]]
