---
type: command
executor: bash
data: host -l $_DOMAIN $_TARGET_NAMESERVER
output: |-
  root@kali:~# host -l testsite.com nsztm1.testsite.com
  Using domain server:
  Name: nsztm1.testsite.com
  Address: 192.178.50.100#53
  Aliases: 

  testsite.com has address 192.178.50.100
  testsite.com name server nsztm1.testsite.com.
  testsite.com name server nsztm2.testsite.com.
tags:
  - reconnaissance
  - dns
  - zone-transfer
platforms:
  - Linux
  - Unix
verified: true
validated: true
---

# host-attempt-dns-zone-transfer

## Command

```bash
host -l $_DOMAIN $_TARGET_NAMESERVER
```

## Description

This command attempts a DNS zone transfer (AXFR) from the specified nameserver for the given domain. If the DNS server is misconfigured to allow zone transfers to external clients, it will dump all records in the zone, providing valuable reconnaissance data such as hostnames, IPs, and subdomains. Use this during network enumeration to identify potential information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The domain or zone name to transfer (e.g., example.com) | Yes |
| $_TARGET_NAMESERVER | The authoritative DNS server to query (e.g., ns1.example.com or IP) | Yes |
| -l | Flag to request a zone transfer (AXFR) | Built-in |

## Examples

### Basic Usage

```bash
host -l testsite.com nsztm1.testsite.com
```

### Advanced Usage

With verbose output for more details:
```bash
host -l -v testsite.com 192.168.1.1
```

## Expected Output

If successful (zone transfer allowed):
```
root@kali:~# host -l testsite.com nsztm1.testsite.com
Using domain server:
Name: nsztm1.testsite.com
Address: 192.178.50.100#53
Aliases: 

testsite.com has address 192.178.50.100
testsite.com name server nsztm1.testsite.com.
testsite.com name server nsztm2.testsite.com.
```

If denied (common in secure setups):
```
Using domain server:
Name: nsztm1.testsite.com
Address: 192.178.50.100#53
Aliases: 

Transfer failed.
```

## Related

- [[Related Procedure]] (if applicable)
- [[tools/host]] (parent tool)
