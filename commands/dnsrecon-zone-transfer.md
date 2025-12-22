---
id: 86aa5503-6bb7-4536-84c2-edb089b20150
type: command
executor: bash
data: dnsrecon -d $_TARGET_DOMAIN -t axfr
output: |-
  root@kali:~# dnsrecon -d testsite.com -t axfr
  [*] Testing NS Servers for Zone Transfer
  [*] Checking for Zone Transfer for testsite.com name servers
  [*] Resolving SOA Record
  [+]      SOA nsztm1.testsite.com 192.178.50.100
  [*] Resolving NS Records
  [*] NS Servers found:
  [*]     NS nsztm1.testsite.com 192.178.50.101
  [*]     NS nsztm2.testsite.com 192.178.50.102
  [*] Removing any duplicate NS server IP Addresses...
  [*]
  [*] Trying NS server 192.178.50.101
  [+] 192.178.50.101 Has port 53 TCP Open
  [+] Zone Transfer was successful!!
  [*]      SOA nsztm1.testsite.com 192.178.50.101
  [*]      NS nsztm1.testsite.com 192.178.50.101
  [*]      SRV _sip._tcp.testsite.com www 5060 0 no_ip
  [*]      HINFO Casio fx-700G Windows XP
  [*]      RP robin robinwood
  [*]      AFSDB 1 asfdbbox
  [*]      AFSDB 1 asfdbbox
  [*]      LOC 53 20 56.558 N 1 38 33.526 W 0.00m
  [*]      NAPTR P 2 3 !^.*$!sip:customer-service@testsite.com! . E2U+sip
  [*]      NAPTR P 1 1  email.testsite.com E2U+email
created_at: '2019-09-20T18:53:20.010961+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - DNS
  - Zone Transfer
  - Enumeration
verified: true
validated: true
---

# dnsrecon-zone-transfer

## Command

```bash
dnsrecon -d $_TARGET_DOMAIN -t axfr
```

## Description

This command uses DNSRecon to test for DNS zone transfers (AXFR) on a target domain. It attempts to query the domain's name servers for a full zone transfer, which can reveal all DNS records if the server is misconfigured to allow it. This is a common reconnaissance technique to map out internal network details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_TARGET_DOMAIN` | The target domain name to test (e.g., example.com) | Yes |
| `-d` | Specifies the domain flag | Built-in |
| `-t axfr` | Specifies the zone transfer (AXFR) test type | Built-in |

## Examples

### Basic Usage

Test zone transfer for a single domain.

```bash
dnsrecon -d example.com -t axfr
```

### Advanced Usage

Specify a custom name server for the query.

```bash
dnsrecon -d example.com -t axfr -n 8.8.8.8
```

## Expected Output

Description of what output to expect when the command runs successfully.

If the zone transfer succeeds, it will list all DNS records from the zone. If it fails, it will report no transfer available.

```
root@kali:~# dnsrecon -d testsite.com -t axfr
[*] Testing NS Servers for Zone Transfer
[*] Checking for Zone Transfer for testsite.com name servers
[*] Resolving SOA Record
[+]      SOA nsztm1.testsite.com 192.178.50.100
[*] Resolving NS Records
[*] NS Servers found:
[*]     NS nsztm1.testsite.com 192.178.50.101
[*]     NS nsztm2.testsite.com 192.178.50.102
[*] Removing any duplicate NS server IP Addresses...
[*]
[*] Trying NS server 192.178.50.101
[+] 192.178.50.101 Has port 53 TCP Open
[+] Zone Transfer was successful!!
[*]      SOA nsztm1.testsite.com 192.178.50.101
[*]      NS nsztm1.testsite.com 192.178.50.101
[*]      SRV _sip._tcp.testsite.com www 5060 0 no_ip
[*]      HINFO Casio fx-700G Windows XP
[*]      RP robin robinwood
[*]      AFSDB 1 asfdbbox
[*]      AFSDB 1 asfdbbox
[*]      LOC 53 20 56.558 N 1 38 33.526 W 0.00m
[*]      NAPTR P 2 3 !^.*$!sip:customer-service@testsite.com! . E2U+sip
[*]      NAPTR P 1 1  email.testsite.com E2U+email
```

## Related

- [[Related Command: dnsrecon-standard-enumeration]]
- [[Related Procedure: DNS-Reconnaissance]]
- [[tools/DNSRecon]]
