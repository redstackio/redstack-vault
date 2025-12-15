---
id: proc-verify-dns
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
  - Network
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:23:27.712Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Verify-Execution-with-DNS-Logs

## Summary

This procedure confirms RCE by checking DNS query logs on an attacker-controlled BIND server, triggered by the URLDNS gadget in the deserialized payload.

## Description

After sending the payload, the server's deserialization executes the gadget, causing a DNS lookup to the controlled domain. BIND logs capture this as evidence of successful exploitation without needing direct server access. Requires a running BIND instance configured for the domain.

## Requirements

1. Attacker-controlled DNS server (BIND) hosting testing1.jexboss.info
2. Access to BIND logs
3. Payload already sent to target

## Defense

Defensive measures and detection strategies:

- Monitor application server DNS traffic for anomalous queries
- Block or log DNS to external attacker domains
- Implement DNS sinkholing for known malicious domains

## Objectives

1. Observe DNS query from target
2. Confirm deserialization and gadget execution
3. Validate RCE without disruption

## Instructions

### Step 1: Monitor BIND Logs

**Context**: Check logs for incoming queries post-payload delivery.

No command executed; manually tail or grep BIND logs (e.g., /var/log/named/query.log) for 'testing1.jexboss.info' queries from the target's IP.

> Expected output: Log entry showing A record query for the domain, timestamped after the curl request.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/BIND]]

## Tags

- verification
- dns
- exfiltration
