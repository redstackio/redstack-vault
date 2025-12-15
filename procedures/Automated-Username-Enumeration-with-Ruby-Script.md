---
id: uuid-4
tags:
  - automation
  - ruby
  - enumeration
type: procedure
tools:
  - '[[tools/InstagramBrandEnumerationExploit.rb]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/run-enumeration-ruby-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:12.521Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Automated-Username-Enumeration-with-Ruby-Script

## Summary

This procedure automates username enumeration by running a custom Ruby script that sends bulk requests to the resend-verify endpoint using an email list, identifying valid accounts efficiently.

## Description

The script replicates the manual POST requests at scale, parsing responses to log valid emails. It exploits the lack of rate limiting, allowing ~100 attempts per minute, and can be run from any machine with Ruby.

## Requirements

1. Ruby installed (version 2+)
2. emails.txt file with one email per line
3. Target URL configured in script

## Defense

Defensive measures and detection strategies:

- Deploy WAF rules to block scripted traffic (e.g., user-agent checks)
- Implement IP-based throttling
- Monitor for bulk resend patterns in logs

## Objectives

1. Enumerate hundreds of valid usernames quickly
2. Avoid manual effort for large lists
3. Collect targets for subsequent brute-force

## Instructions

### Step 1: Prepare Input File

**Context**: Create the email list file.

Save target emails to emails.txt in the script directory.

### Step 2: Run the Script

**Context**: Execute automation to test the list.

**Command** ([[commands/run-enumeration-ruby-script]]):

```bash
ruby InstagramBrandEnumerationExploit.rb
```

> Script outputs valid emails to console; completes 1001 requests in ~10 minutes without issues.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/run-enumeration-ruby-script]]

## Tools Used

- [[tools/InstagramBrandEnumerationExploit.rb]]

## Tags

- automation
- ruby
- enumeration
