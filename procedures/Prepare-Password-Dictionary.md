---
id: proc-prepare-password-dict
tags:
  - wordlist
  - password-guessing
type: procedure
tools:
  - '[[tools/SecLists]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/count-passwords-in-dictionary]]'
  - '[[commands/view-end-of-password-list]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Password Guessing]]'
updated_at: '2025-12-14T17:31:52.787Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Password Guessing]]'
---
# Prepare-Password-Dictionary

## Summary

This procedure downloads and customizes a common password wordlist for brute-force attacks, verifying its contents to ensure inclusion of likely targets.

## Description

Download 10k_most_common.txt from SecLists (10,000 common passwords), append the test password 'Geniaal2!!' to create 10,001 entries. Verify count and contents to confirm readiness for brute-force scripting.

## Requirements

1. Internet access for download
2. Linux environment or Git
3. Text editor for appending

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies (no commons)
- Monitor for downloads of known wordlists from security repos
- Use password hashing with high iterations

## Objectives

1. Obtain comprehensive common password list
2. Customize with known test passwords
3. Validate file integrity and size

## Instructions

### Step 1: Download Wordlist

**Context**: Fetch the password dictionary from SecLists.

```bash
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10k_most_common.txt
```

> Expected: File with 10,000 lines of common passwords.

### Step 2: Append Test Password

**Context**: Add the specific test password to the end.

```bash
echo 'Geniaal2!!' >> 10k_most_common.txt
```

> Expected: File now has 10,001 entries.

### Step 3: Verify Count

**Context**: Count lines to confirm size.

Execute [[commands/count-passwords-in-dictionary]]:

```bash
cat 10k_most_common.txt | wc -l
```

> Expected output: 10001

### Step 4: Inspect End

**Context**: Check last entries to confirm append.

Execute [[commands/view-end-of-password-list]]:

```bash
tail 10k_most_common.txt
```

> Expected output: shoes
howie
hevnm4
hugohugo
eighty
epson
 evangeli
eeeee1
eyphed
Geniaal2!!

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Password Guessing]] Password Guessing

### Sub-Techniques


## Commands Used

- [[commands/count-passwords-in-dictionary]]
- [[commands/view-end-of-password-list]]

## Tools Used

- [[tools/SecLists]]

## Tags

- [[wordlist]]
- [[password-guessing]]
