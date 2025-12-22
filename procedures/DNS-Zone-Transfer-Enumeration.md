---
id: b2177d32-ab8b-4626-95f0-228601d3e970
name: DNS-Zone-Transfer-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.785986+00:00'
updated_at: '2023-04-10T20:21:18.268597+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Host Information|T1592 - Gather Victim Host
    Information]]
sub_techniques: []
tags:
  - '[[tags/active-recon]]'
  - '[[tags/dns-enumeration]]'
  - '[[tags/network-discovery]]'
commands:
  - '[[commands/host-query-name-servers]]'
  - '[[commands/host-resolve-master-ip]]'
  - '[[commands/dig-perform-zone-transfer]]'
platforms:
  - Linux
tools: []
validated: true
---

# DNS-Zone-Transfer-Enumeration

## Summary

This procedure performs DNS zone transfer enumeration to discover subdomains associated with a target domain. By querying name servers and attempting a zone transfer from the authoritative server, it reveals the full DNS zone file if the server is misconfigured, providing valuable reconnaissance data for identifying potential attack surfaces.

## Description

DNS zone transfers are a mechanism for primary DNS servers to replicate zone data to secondary servers. If not properly restricted, attackers can exploit this to download the entire zone file, enumerating all subdomains, hosts, and records. This technique is useful in active reconnaissance phases to map the target's network footprint without direct access. It targets misconfigurations in DNS servers like BIND, where AXFR (full zone transfer) requests are allowed from unauthorized IPs. Success depends on the target's DNS configuration; modern setups often block this, but legacy or poorly secured environments remain vulnerable. The procedure assumes command-line access on a Linux system with DNS tools installed.

## Requirements

1. Network access to the target's DNS servers (no authentication required, but firewalls may block queries).
2. Installed tools: host and dig (part of dnsutils package on Debian-based systems).
3. Target domain name and optionally the IP of the authoritative name server.
4. Basic knowledge of DNS protocols and command-line tools.

## Defense

- Configure DNS servers to allow zone transfers only from trusted IP addresses (e.g., via ACLs in BIND named.conf).
- Use DNSSEC to validate queries and prevent unauthorized transfers.
- Monitor DNS query logs for AXFR attempts and alert on suspicious patterns (e.g., using tools like DNSSniff or server logs).
- Implement rate limiting on DNS servers to thwart enumeration attempts.

## Objectives

1. Identify all subdomains and DNS records for the target domain to map the attack surface.
2. Detect misconfigurations in the target's DNS infrastructure.
3. Gather hostnames and IP mappings for further reconnaissance or targeted attacks.

## Instructions

### Step 1: Query Name Servers

**Context**: Begin by identifying the authoritative name servers for the target domain using the host command. This reveals the DNS servers responsible for the zone, which are potential targets for zone transfer attempts.

**Command** ([[commands/host-query-name-servers]]):
```bash
host -t ns $_DOMAIN
```

> This command queries for NS (name server) records. Replace $_DOMAIN with the target domain (e.g., example.com). It lists the name servers, such as ns1.example.com, providing the next hop for deeper enumeration.

### Step 2: Resolve Master Server IP

**Context**: Once name servers are identified, resolve the IP address of the master (primary) name server. This IP will be used as the target for the zone transfer request, as primary servers are more likely to allow AXFR if misconfigured.

**Command** ([[commands/host-resolve-master-ip]]):
```bash
host $_MASTER_SERVER.$_DOMAIN
```

> Use the master server name from Step 1 (e.g., master.example.com). This resolves the A record to obtain the IP address (e.g., 192.168.1.1), confirming reachability and preparing for the transfer attempt.

### Step 3: Perform Zone Transfer

**Context**: Attempt to pull the full DNS zone using dig's AXFR command against the resolved master server IP. If successful, this dumps all records; if denied, it indicates proper configuration.

**Command** ([[commands/dig-perform-zone-transfer]]):
```bash
挖 axfr $_DOMAIN @$_MASTER_IP
```

> Specify the domain and master IP from previous steps. Success yields a list of all subdomains and records; failure shows a refusal message like "Transfer failed." Verify by checking for subdomain listings in the output.
