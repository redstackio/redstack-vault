---
id: proc-uuid-1
tags:
  - enumeration
  - information-disclosure
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-robots-txt]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:55.598Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Enumerate-Robots-Txt-for-Information-Disclosure

## Summary

This procedure involves basic web enumeration to access the robots.txt file, which often contains sensitive information or flags in CTF scenarios, leading to direct information disclosure without authentication.

## Description

In web applications, robots.txt is a standard file that instructs web crawlers on site navigation. Attackers enumerate it early in reconnaissance to uncover hidden paths or, in CTFs, embedded flags. This targets public-facing web servers like Apache on port 80, requiring only HTTP access. Success reveals plaintext flags, enabling further chain progression.

## Requirements

1. Network access to target HTTP endpoint
2. Basic tools like curl or browser
3. No credentials needed

## Defense

Defensive measures and detection strategies:

- Remove sensitive data from robots.txt
- Implement WAF to log unusual /robots.txt accesses
- Use robots.txt disallows strategically without exposing paths

## Objectives

1. Discover exposed files and flags
2. Map initial attack surface
3. Achieve low-risk information disclosure

## Instructions

### Step 1: Access Robots.txt

**Context**: Directly request the robots.txt file to inspect its contents for flags.

**Command** ([[commands/curl-access-robots-txt]]):
```bash
curl https://hackyholidays.h1ctf.com/robots.txt
```

> This command fetches the file; expect plaintext flag in the response body.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-access-robots-txt]]

## Tools Used

- [[tools/Curl]]

## Tags

- [[enumeration]]
- [[information-disclosure]]
