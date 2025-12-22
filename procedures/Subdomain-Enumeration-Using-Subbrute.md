---
type: procedure
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Network Information|T1590 - Gather Victim Network
    Information]]
sub_techniques:
  - '[[sub-techniques/DNS|T1590.002 - DNS]]'
tags:
  - '[[tags/Enumerate all subdomains (only if the scope is *.domain.ext)]]'
  - '[[tags/Subdomains Enumeration]]'
  - '[[tags/Using Subbrute]]'
commands:
  - '[[commands/git-clone-subbrute-repository]]'
  - '[[commands/python-run-subbrute-enumeration]]'
tools:
  - '[[tools/Subbrute]]'
platforms:
  - Linux
skill_level: beginner
impact_level: low
detection_risk: low
verified: true
validated: true
---

# Subdomain-Enumeration-Using-Subbrute

## Summary

This procedure uses the Subbrute tool to perform brute-force subdomain enumeration against a target domain by querying DNS servers with a list of common subdomain names, helping to identify potential subdomains that may not be publicly listed.

## Description

Subdomain enumeration involves discovering valid subdomains associated with a target domain, which expands the attack surface for further reconnaissance or exploitation. Subbrute is a Python-based tool that employs a brute-force approach, generating permutations of common subdomain names (e.g., www, mail, admin) and querying the authoritative DNS server for valid responses. This technique is particularly useful in offensive security to uncover hidden infrastructure, such as development servers or internal services. From a defensive standpoint, it highlights the need to monitor for anomalous DNS queries. The procedure assumes access to a nameserver and requires the Subbrute tool to be cloned and executed in a Linux environment.

## Requirements

1. Network access to query the target's DNS server (no authentication typically required for public domains).
2. Permission to perform reconnaissance activities (ethical hacking or authorized testing only).
3. Subbrute tool installed via git clone.
4. Python 2 or 3 installed on the attacking machine.

## Defense

Defensive measures and detection strategies:

- Monitor DNS queries for suspicious activity, such as high volumes from a single source targeting multiple subdomains.
- Implement rate limiting on DNS queries to prevent abuse and brute-force attempts.
- Use DNSSEC to protect against DNS spoofing attacks and validate responses.

## Objectives

1. Discover subdomains of a target domain through brute-force DNS queries.
2. Identify potential targets for further attacks by expanding the visible attack surface.
3. Identify hidden services or infrastructure that may be vulnerable.

## Instructions

### Step 1: Clone the Subbrute Repository

**Context**: Download the Subbrute tool from its GitHub repository to make it available for execution. This step sets up the tool on your local machine.

**Command** ([[commands/git-clone-subbrute-repository]]):
```bash
git clone https://github.com/TheRook/subbrute
```

> This command clones the repository into a local directory named 'subbrute'. Navigate into the directory after cloning to prepare for the next step. Expected output includes progress messages like 'Cloning into 'subbrute'...'

### Step 2: Run Subbrute Against the Target Domain

**Context**: Execute the Subbrute tool to perform brute-force enumeration by querying the DNS server with common subdomain names. Replace the domain placeholder with the actual target.

**Command** ([[commands/python-run-subbrute-enumeration]]):
```bash
python subbrute.py $_DOMAIN
```

> This launches the enumeration process, which will output any valid subdomains discovered. The tool uses its built-in wordlist to generate queries. If successful, it lists resolved subdomains; otherwise, it reports no matches. Run from within the cloned subbrute directory.
