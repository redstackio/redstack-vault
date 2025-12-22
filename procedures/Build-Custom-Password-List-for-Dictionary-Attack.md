---
id: c21a0cdc-15f1-495f-931b-1e994e88f310
name: Build-Custom-Password-List-for-Dictionary-Attack
type: procedure
verified: true
submitted: true
created_at: '2020-03-18T23:35:23.678761+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques: []
platforms:
  - Linux
tags:
  - enumeration
  - password-cracking
commands:
  - '[[commands/cewl-generate-wordlist-from-website]]'
  - '[[commands/hashcat-mutate-wordlist-append-digit]]'
tools:
  - '[[tools/CeWL]]'
  - '[[tools/Hashcat]]'
validated: true
---

# Build-Custom-Password-List-for-Dictionary-Attack

## Summary

This procedure constructs a targeted password dictionary by combining enumerated usernames, common passwords, web-crawled terms, and mutations to support efficient online brute force attacks against services like SMB, minimizing noise and detection risk.

## Description

Online dictionary attacks require small, contextual wordlists to avoid rate limiting and alerts. Starting from LDAP-enumerated usernames, this adds top common passwords, crawls target websites for relevant terms (e.g., company names), and mutates entries (e.g., append digits) based on policy. It's ideal for Active Directory where default passwords or simple patterns are common. The result is a focused list (e.g., 1,000-5,000 entries) suitable for tools like CrackMapExec.

## Requirements

- Enumerated usernames from prior LDAP query
- Access to target's website (if available) for crawling
- CEWL and Hashcat installed
- Knowledge of password policy (e.g., requires digit)

## Defense

- Enforce strong password policies (length >12, no common words)
- Implement account lockout after failed attempts
- Monitor for unusual login patterns (e.g., SIEM rules for multiple failures from one IP)
- Use MFA to mitigate brute force success

## Objectives

- Create base list from common passwords and usernames
- Crawl for contextual terms
- Mutate list to match policy requirements
- Produce optimized dictionary for brute force

## Instructions

### Step 1: Compile Base Wordlist from Common Sources

**Context**: Start with curated common passwords (e.g., SecLists top 100) and add usernames as potential passwords (common lazy admin practice). This forms the core dictionary.

**Command** (No specific command; manual concatenation):

> Download top-passwords.txt from SecLists. Append usernames: echo -e "$(cat usernames.txt)" >> top-passwords.txt. Why: Reduces list size while covering high-probability guesses.

### Step 2: Crawl Website for Contextual Terms

**Context**: If the target has a public site, extract words as potential passwords (e.g., 'admin', 'company123'). CEWL spiders the site to build vocabulary.

**Command** ([[commands/cewl-generate-wordlist-from-website]]):
```bash
cewl http://$_TARGET_IP -d 2 -m 5 -w web_terms.txt
```

> -d 2 limits depth to 2 pages, -m 5 min word length, -w outputs to file. Merge: cat web_terms.txt >> passwords.txt. Expected: Terms like 'welcome', 'login'.

### Step 3: Mutate Wordlist for Policy Compliance

**Context**: If policy requires digits, append 0-9 to each entry. This exponentially grows the list but targets common user behaviors.

**Command** ([[commands/hashcat-mutate-wordlist-append-digit]]):
```bash
hashcat -a 6 --stdout passwords.txt ?d > passwords_mutated.txt
```

> -a 6 is append mask, ?d is digit placeholder. Use sparingly to avoid oversized lists. Expected: Entries like 'password1', 'admin0'.
