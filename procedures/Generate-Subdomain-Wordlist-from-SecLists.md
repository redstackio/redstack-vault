---
id: 8a000891-ef7a-4676-903b-4b2316bd25f7
type: procedure
verified: true
submitted: true
created_at: '2020-06-30T04:41:15.237461+00:00'
updated_at: '2023-05-26T00:48:26.948250+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Vulnerability Scanning]]'
sub_techniques: []
tags:
  - wordlist
  - brute-force
  - dns
platforms:
  - Linux
commands:
  - '[[commands/build-subdomain-wordlist-with-sed]]'
tools:
  - '[[tools/SecLists]]'
validated: true
---

# Generate-Subdomain-Wordlist-from-SecLists

## Summary

This procedure generates a brute-force wordlist of potential subdomains by appending the target domain to a comprehensive list of common subdomain names from SecLists, preparing input for DNS resolution tools like MassDNS.

## Description

SecLists provides curated wordlists from real-world data; the top1million-20000.txt file contains frequent subdomains like 'www', 'mail', 'admin'. Using sed to concatenate with the target domain creates a targeted list (e.g., admin.target.com), enabling efficient brute-forcing without generic permutations. Download SecLists via git clone if needed.

## Requirements

- SecLists repository cloned (git clone https://github.com/danielmiessler/SecLists.git)
- Target domain
- Basic Unix tools (sed, bash)

## Defense

- No direct defense, as this is offline preparation
- Monitor for subsequent DNS brute-force queries

## Objectives

- Produce a wordlist of 20,000+ potential subdomains
- Ensure format is one per line for tool compatibility

## Instructions

### Step 1: Build Wordlist

**Context**: Transform the SecLists file by appending the target domain to each entry.

**Command** ([[commands/build-subdomain-wordlist-with-sed]]):

```bash
sed 's/$/.$_TARGET_DOMAIN/' $_SECLISTS_WORDLIST > $_OUTPUT_FILE
```

Uses $_SECLISTS_WORDLIST=/path/to/subdomains-top1million-20000.txt; outputs to hosts.txt.
