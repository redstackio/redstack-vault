---
id: proc-uuid-004
tags:
  - verification
  - dns
  - exfiltration
type: procedure
tools:
  - '[[tools/BIND]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Standard Application Layer Protocol]]'
updated_at: '2025-12-14T17:23:20.512Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Standard Application Layer Protocol]]'
---
# Verify-RCE-via-DNS-Logs

## Summary

This procedure verifies successful RCE by inspecting DNS server logs for queries initiated by the deserialized payload from the target server.

## Description

After sending the URLDNS payload, the gadget forces the server to resolve the attacker's domain, logging the query with the target's IP. Uses BIND as the authoritative nameserver for the domain.

## Requirements

1. BIND DNS server configured for dod_test.jexboss.info
2. Access to BIND logs
3. Payload already sent to target

## Defense

Defensive measures and detection strategies:

- Monitor application server DNS traffic for external resolutions
- Block or log unexpected DNS queries from web servers
- Use DNS sinkholing for known malicious domains

## Objectives

1. Confirm gadget chain execution
2. Identify source IP for attribution
3. Validate RCE without direct server access

## Instructions

### Step 1: Check BIND Logs

**Context**: Review logs for incoming queries post-payload submission.

**Command** (No specific command; manual log inspection):

> Tail or grep BIND logs (e.g., /var/log/named/query.log) for 'dod_test.jexboss.info' queries. Expected output: Entry like 'query from target.IP for A record'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/BIND]]

## Tags

- [[verification]]
- [[DNS]]
- [[Exfiltration]]
