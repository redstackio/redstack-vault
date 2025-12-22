---
type: code
language: text
verified: true
tags:
  - dns
  - c2
  - beacon
platforms:
  - Linux
validated: true
---

# DNS Zone File Entries for Cobalt Strike Beacon

## Code

```text
NS  example.com directs to 10.10.10.10. 86400
NS  polling.campaigns.example.com directs to campaigns.example.com. 3600
A campaigns.example.com directs to 10.10.10.10 3600
```

## Description

This code snippet provides DNS zone file entries to configure a domain hierarchy for Cobalt Strike's DNS Beacon C2. The NS records delegate name service authority, and the A record maps the subdomain to the attacker's DNS server IP, enabling the beacon to resolve and query subdomains for commands and exfiltration.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `example.com` | Primary C2 domain | `attackerdomain.com` |
| `campaigns.example.com` | Subdomain for campaigns/beaconing | `beacon.attackerdomain.com` |
| `polling.campaigns.example.com` | Polling subdomain for task retrieval | `poll.beacon.attackerdomain.com` |
| `10.10.10.10` | Attacker's DNS server IP | `192.168.1.100` |
| `86400` / `3600` | TTL values in seconds | Adjust for caching needs |

## Usage

Append these lines to your DNS zone file (e.g., in BIND: /var/lib/bind/db.example.com). After editing, validate and reload the zone: `named-checkzone example.com zonefile && rndc reload example.com`. Deploy the beacon payload on the target, which will begin querying subdomains like xxxx.polling.campaigns.example.com for C2 tasks.

## Detection

- Anomalous NS/A record additions in DNS server logs.
- High volume of unique subdomain queries from a single client.
- Use tools like DNSTAP or Suricata rules for DNS C2 signatures (e.g., alert on rapid subdomain generation).

## Related

- [[Related Procedure: configure-dns-for-cobalt-strike-dns-beacon]]
- [[Related Tool: Cobalt-Strike]]
