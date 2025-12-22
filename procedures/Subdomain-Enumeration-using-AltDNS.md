---
id: d8e51d8b-47d6-4540-9e86-a29e74895e0f
name: Subdomain-Enumeration-using-AltDNS
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather-Victim-Network-Information|T1590 - Gather Victim Network
    Information]]
sub_techniques: []
tags:
  - '[[tags/Enumerate all subdomains (only if the scope is *.domain.ext)]]'
  - '[[tags/Subdomains Enumeration]]'
  - '[[tags/Using AltDNS]]'
commands:
  - '[[commands/install-altdns]]'
  - '[[commands/generate-subdomain-permutations-with-altdns]]'
platforms:
  - Linux
tools:
  - '[[tools/altdns]]'
validated: true
---

# Subdomain-Enumeration-using-AltDNS

## Summary

This procedure uses AltDNS, a DNS reconnaissance tool, to generate permutations and combinations of potential subdomains for a target domain. By providing a base domain and a wordlist of common subdomain prefixes or suffixes, AltDNS creates a large set of possible subdomain names, which can then be resolved via DNS queries to identify valid, hidden subdomains that expand the attack surface.

## Description

Subdomain enumeration is a key reconnaissance technique to map out a target's digital footprint. Traditional tools like brute-forcers may miss creative or non-standard subdomains, but AltDNS excels at permutation-based generation, such as combining words like 'admin', 'api', 'dev' with the target domain (e.g., admin.target.com, api-dev.target.com). This is particularly useful in scoped engagements where the target is *.target.com, allowing broad enumeration without violating rules. The procedure assumes Kali Linux or similar environment with Python installed. Output permutations can be piped into resolvers like dnsx or massdns for validation. This maps to MITRE ATT&CK Reconnaissance tactic, focusing on gathering network information to identify potential entry points.

## Requirements

1. Linux environment (e.g., Kali) with internet access for installation.
2. Python 2.7 or 3.x installed.
3. A target domain name (e.g., target.com).
4. A wordlist file with potential subdomain components (e.g., common words like 'www', 'mail', 'ftp').
5. Input file with base subdomains or the main domain.

## Defense

- Implement DNS query rate limiting and monitoring to detect anomalous resolution patterns from permutation tools.
- Use DNSSEC to prevent unauthorized subdomain resolutions and logging via tools like BIND or PowerDNS.
- Regularly audit and remove unused subdomains to reduce the attack surface.

## Objectives

1. Generate a comprehensive list of potential subdomain permutations for the target domain.
2. Identify valid subdomains through subsequent DNS resolution (outside this procedure).
3. Expand reconnaissance scope to uncover hidden services or applications.

## Instructions

### Step 1: Install AltDNS

**Context**: AltDNS must be cloned and set up in a local directory before use. This ensures all dependencies are met for the Python script.

**Command** ([[commands/install-altdns]]):
```bash
git clone https://github.com/infosec-au/altdns.git
cd altdns/
pip install -r requirements.txt
```

> This clones the AltDNS repository and installs required Python packages like dnspython. Run from a directory where you have write permissions. Expected output includes successful git clone messages and pip installation completions without errors.

### Step 2: Prepare Input Files

**Context**: Create or obtain two files: one with the target domain(s) or known subdomains (inputdomains.txt), and a wordlist (words.txt) containing permutation bases like 'admin', 'test', 'staging', etc. This step sets up the data for generation.

No specific command here; manually create files, e.g., echo "target.com" > inputdomains.txt and use a standard wordlist like subdomains-top1million-5000.txt, stripping extensions to get words.txt.

> Ensure inputdomains.txt has one domain per line. words.txt should have one word per line without file extensions. Success is verified by checking file contents with cat inputdomains.txt and cat words.txt.

### Step 3: Generate Subdomain Permutations

**Context**: Run AltDNS to produce permutations by combining words from the wordlist with input domains, creating potential subdomains like word1.target.com, target.com.word2, etc. This generates a large output file for further processing.

**Command** ([[commands/generate-subdomain-permutations-with-altdns]]):
```bash
WORDLIST_PERMUTATION="./altdns/words.txt"
python ./altdns/altdns.py -i inputdomains.txt -o output_permutations.txt -w $WORDLIST_PERMUTATION
```

> Execute from the parent directory of altdns/. The -i flag specifies input domains, -o output file, -w wordlist. Use python2.7 if compatibility issues arise. Expected output is a file (output_permutations.txt) with thousands of generated subdomains, e.g., admin.target.com, dev-api.target.com. Verify with wc -l output_permutations.txt showing a large number of lines.

### Step 4: Validate Generated Subdomains (Optional Extension)

**Context**: While not core to AltDNS, pipe the output to a resolver like dnsx to check which permutations resolve, confirming live subdomains.

**Command** (using external tool):
```bash
cat output_permutations.txt | dnsx -silent -o live_subdomains.txt
```

> This filters to only resolving subdomains. Success: live_subdomains.txt contains valid entries like admin.target.com (A 192.168.1.1).
