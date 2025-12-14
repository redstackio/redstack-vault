---
id: proc-verify-ssrf-whois
tags:
  - verification
  - reconnaissance
type: procedure
tools:
  - '[[tools/whois]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/whois-ip-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Network Information]]'
updated_at: '2025-12-14T04:39:10.086Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
---
# Verify-SSRF-via-Server-Logs-and-Whois

## Summary

Verify the SSRF exploitation by inspecting incoming request logs on the attacker's server and using WHOIS to confirm the source IP belongs to the target organization.

## Description

After triggering SSRF, the attacker's server logs show the target's IP. A WHOIS query reveals DoD ownership, confirming the vulnerability's impact on the SSI website's ProxySG.

## Requirements

1. Access to server logs from Step 1
2. WHOIS tool available
3. Target IP extracted from logs

## Defense

Defensive measures and detection strategies:

- Log all outbound requests with source details
- Block or alert on requests to unknown external domains
- Regularly audit WHOIS for anomalous IP accesses

## Objectives

1. Confirm request origin
2. Validate target affiliation
3. Build evidence for report

## Instructions

### Step 1: Check Logs

**Context**: Review your server's access logs for the incoming SSRF request.

Look for entries showing GET / from the target's IP.

### Step 2: Perform WHOIS Lookup

**Context**: Query the IP to verify ownership.

**Command** ([[commands/whois-ip-lookup]]):
```bash
whois target-ip
```

> Outputs organization details like 'Organization: U.S. Department of Defense'. Expected: Matching DoD info.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Network Information]] Gather Victim Network Information

### Sub-Techniques


## Commands Used

- [[commands/whois-ip-lookup]]

## Tools Used

- [[tools/whois]]

## Tags

- [[verification]]
- [[Reconnaissance]]
