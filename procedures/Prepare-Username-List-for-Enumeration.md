---
id: proc-002
tags:
  - username-list
  - recon-prep
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:58.941Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Prepare-Username-List-for-Enumeration

## Summary

This procedure prepares a text file containing potential usernames for testing against vulnerable SSH servers, enabling efficient enumeration of valid accounts via the timing attack.

## Description

In the context of CVE-2016-6210 exploitation, a username list is crucial for batch-testing authentication attempts. Start with common usernames (e.g., admin, root, user) for quick validation, then scale to larger lists like rockyou.txt for exhaustive discovery. The list feeds into the POC script's -U parameter, targeting subdomains like newsletter.nextcloud.com. Expected outcomes include a formatted file ready for script input, facilitating information disclosure of valid accounts.

## Requirements

1. Text editor (e.g., vim, nano) or wordlist tools
2. Access to common username dictionaries (e.g., rockyou.txt)
3. Basic scripting knowledge for list generation if needed

## Defense

Defensive measures and detection strategies:

- Log and monitor file creation activities for suspicious wordlists
- Implement username obfuscation or rate-limiting on SSH
- Use anomaly detection on authentication attempt patterns

## Objectives

1. Create a comprehensive list of test usernames
2. Ensure list format compatibility with POC script
3. Optimize for initial small tests before full scans

## Instructions

### Step 1: Create Basic List

**Context**: Manually or script-generate a starting list of common usernames.

No command; use echo or editor:

```bash
echo -e "admin\nroot\nuser\nguest" > usernames.txt
```

> This creates usernames.txt with basic entries; expand manually or via cat for larger lists.

### Step 2: Expand with Wordlist

**Context**: Append from a known wordlist for broader coverage.

**Command** (cat-append-wordlist):
```bash
cat rockyou.txt | head -1000 >> usernames.txt
```

> Limits to first 1000 lines to avoid overload; adjust as needed for full enumeration.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/cat-append-wordlist]]

## Tools Used


## Tags

- username-list
- recon-prep
