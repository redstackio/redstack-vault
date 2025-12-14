---
id: proc-003
tags:
  - ssh-enumeration
  - timing-attack
type: procedure
tools:
  - '[[tools/POC-py-for-CVE-2016-6210]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/python-poc-py-username-enumeration-newsletter-nextcloud-com]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:58.936Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Execute-Username-Enumeration-on-Newsletter-Subdomain

## Summary

This procedure runs the POC script to enumerate usernames on newsletter.nextcloud.com by measuring SSH authentication response times with a large password, identifying valid accounts via timing discrepancies.

## Description

Targeting the SSH service on newsletter.nextcloud.com affected by OpenSSH 7.2p2 (CVE-2016-6210), the script attempts password authentication for each username in the list using an excessively long password. Existing usernames trigger longer processing (e.g., >0.047s), disclosing valid accounts remotely. This aids in reconnaissance for brute-force or phishing attacks. Prerequisites: Downloaded POC.py and prepared usernames.txt; requires network reachability to port 22.

## Requirements

1. POC.py script in current directory
2. usernames.txt file prepared
3. Python interpreter (2.x or 3.x)
4. Network access to newsletter.nextcloud.com:22

## Defense

Defensive measures and detection strategies:

- Patch OpenSSH to version >7.2p2 or apply timing normalization mitigations
- Enable fail2ban or SSH rate-limiting to detect rapid attempts
- Monitor SSH logs for anomalous connection timings and patterns

## Objectives

1. Perform timing-based enumeration on primary target
2. Identify valid usernames for further exploitation
3. Validate vulnerability presence

## Instructions

### Step 1: Run Enumeration Script

**Context**: Execute the POC to test all usernames against the target host.

**Command** ([[commands/python-poc-py-username-enumeration-newsletter-nextcloud-com]]):
```bash
python POC.py newsletter.nextcloud.com -U usernames.txt
```

> The script connects via SSH, attempts auth with a large password per username, and outputs times. Low times (<0.047s) indicate non-existent users; higher times reveal valid ones.

### Step 2: Analyze Output

**Context**: Review results to extract valid usernames.

**Command** (grep-valid-users):
```bash
grep -E "time > 0.047" output.log
```

> Assumes output redirected to log; filters for potential valid accounts.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/python-poc-py-username-enumeration-newsletter-nextcloud-com]]
- [[commands/grep-valid-users]]

## Tools Used

- [[tools/POC-py-for-CVE-2016-6210]]

## Tags

- ssh-enumeration
- timing-attack
