---
id: a012a198-145c-4011-8776-70a3f11e7448
name: Resolve-Domain-Using-Host-Command
type: procedure
verified: true
submitted: false
created_at: '2020-07-24T17:11:26.822994+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Network Boundary Bridging]]'
sub_techniques: []
tags:
  - reconnaissance
  - dns
  - domain-resolution
commands:
  - '[[commands/host-resolve-domain]]'
platforms:
  - Linux
  - Unix
tools:
  - '[[tools/host]]'
validated: true
---

# Resolve-Domain-Using-Host-Command

## Summary

This procedure uses the 'host' command-line tool to perform a DNS lookup on a specified domain name, resolving it to IP addresses and other associated records. It is a fundamental reconnaissance technique to verify domain existence, gather network information, and map potential targets during security assessments.

## Description

Domain resolution is a basic step in network reconnaissance, allowing testers to confirm if a domain is active and to identify its associated IP addresses, mail servers, or other DNS records. The 'host' command queries DNS servers directly from the command line, providing quick feedback without needing a graphical interface. This is useful in initial phases of penetration testing to build an attack surface map, validate target reachability, and identify misconfigurations in DNS setups. It works on Unix-like systems where DNS resolution is available and does not require elevated privileges.

## Requirements

1. Access to a Unix-like system (Linux, macOS) with network connectivity to public DNS resolvers.
2. The 'host' tool installed (part of dnsutils package).
3. No special credentials needed; runs as a standard user.
4. Internet access or connectivity to the target DNS infrastructure.

## Defense

Defensive measures and detection strategies:

- Monitor DNS query logs on authoritative servers for unusual volume or patterns from reconnaissance tools.
- Implement DNS rate limiting and anomaly detection to block automated queries.
- Use DNSSEC to prevent spoofing and ensure query integrity.

## Objectives

1. Verify if the target domain resolves to valid IP addresses.
2. Gather basic DNS records (A, MX, etc.) for further enumeration.
3. Confirm network reachability without alerting advanced defenses.

## Instructions

### Step 1: Execute Domain Resolution Query

**Context**: This step performs the DNS lookup using the host command to resolve the domain name to its IP address and other records. It helps determine if the domain is live and provides initial intelligence on the target's infrastructure.

**Command** ([[commands/host-resolve-domain]]):
```bash
host $_DOMAIN
```

> The command sends a DNS query to the default resolver for the specified domain. Replace $_DOMAIN with the target domain name, such as 'owasp.com'. This step is quick and low-risk, providing output that includes A records (IP addresses), MX records (mail servers), and more if available. If the domain does not resolve, it indicates potential issues like non-existence or DNS blocking.
