---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Network Information|T1590 - Gather Victim Network
    Information]]
sub_techniques: []
tags:
  - subdomain-enumeration
  - nmap
  - crtsh
  - reconnaissance
commands:
  - '[[commands/nmap-hostmap-crtsh-scan]]'
platforms:
  - Linux
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Subdomain-Enumeration-using-Nmap-CRTsh-Script

## Summary

This procedure performs subdomain enumeration on a target domain by leveraging Nmap's hostmap-crtsh script, which queries Certificate Transparency (CT) logs to discover subdomains associated with SSL certificates. It is useful during the reconnaissance phase to map the attack surface without direct interaction with the target infrastructure, helping identify hidden or forgotten subdomains for further exploitation.

## Description

Subdomain enumeration is a key reconnaissance technique to identify all subdomains under a target domain, revealing potential entry points such as administrative interfaces, staging environments, or third-party integrations. The hostmap-crtsh script integrates with Nmap to fetch subdomain data from public CT logs maintained by services like crt.sh, which log SSL certificate issuances. This passive approach avoids alerting defensive tools while providing a comprehensive list of subdomains. The procedure assumes the target domain is publicly resolvable and focuses on domains with issued certificates. It is particularly effective against organizations with complex domain structures and can be combined with active scanning for validation. Expected outcomes include a list of subdomains that can be probed for vulnerabilities or used in phishing campaigns.

## Requirements

1. Network access to the internet for querying CT logs (no direct access to the target domain required beyond DNS resolution).
2. Nmap installed with NSE (Nmap Scripting Engine) enabled and the hostmap-crtsh script available (part of Nmap's official scripts).
3. Target domain name (e.g., example.com) that is in scope for enumeration.
4. Basic command-line proficiency on a Linux-based system like Kali Linux.

## Defense

- Implement certificate transparency monitoring to track and review all issued certificates for the domain.
- Use DNS filtering and rate-limiting to detect anomalous subdomain queries or enumerations.
- Regularly audit and decommission unused subdomains to minimize the attack surface.
- Deploy tools like DNS firewalls (e.g., RPZ) to block known reconnaissance scripts or IPs.

## Objectives

1. Discover subdomains associated with the target domain via CT logs.
2. Compile a list of potential attack vectors without active probing.
3. Gather intelligence for targeted follow-up reconnaissance or exploitation.

## Instructions

### Step 1: Update Nmap Scripts

**Context**: Ensure the Nmap Scripting Engine has the latest scripts, including hostmap-crtsh, to avoid missing updates or errors during execution. This step verifies the script's availability and prepares the environment.

**Command** ([[commands/nmap-update-scripts]]):
```bash
nmap --script-updatedb
```

> This command downloads and updates the Nmap scripts database. Run it periodically or if the script is not found. Expected output includes a list of updated scripts or a confirmation message if no updates are needed.

### Step 2: Perform Subdomain Enumeration with CRTsh Script

**Context**: Execute the core enumeration using the hostmap-crtsh script in a ping-scan mode to query CT logs passively. This identifies subdomains without port scanning, reducing noise.

**Command** ([[commands/nmap-hostmap-crtsh-scan]]):
```bash
nmap -sn --script hostmap-crtsh $_TARGET_DOMAIN
```

> Replace $_TARGET_DOMAIN with the target (e.g., example.com). The -sn flag performs host discovery only, and the script fetches subdomains from crt.sh. Expected output: A table of discovered subdomains with IP resolutions if available, or a note if none are found.

### Step 3: Extract and Save Subdomains

**Context**: Parse the Nmap output to isolate subdomains for further use, such as feeding into other tools like httpx or subfinder for validation.

**Command** ([[commands/grep-extract-subdomains]]):
```bash
nmap -sn --script hostmap-crtsh $_TARGET_DOMAIN | grep 'subdomain' | awk '{print $NF}' > subdomains.txt
```

> This pipes the output through grep to find subdomain lines and awk to extract the domain names, saving them to a file. Adjust the grep pattern based on output format. Expected output: A text file (subdomains.txt) listing unique subdomains, e.g., api.example.com, mail.example.com.

### Step 4: Verify and Deduplicate Results

**Context**: Clean the results to remove duplicates and invalid entries, ensuring a reliable list for subsequent reconnaissance steps.

**Command** ([[commands/sort-unique-subdomains]]):
```bash
sort -u subdomains.txt > unique_subdomains.txt
wc -l unique_subdomains.txt
```

> The sort -u command removes duplicates, and wc counts the lines. Expected output: A deduplicated file and a line count, e.g., "50 unique_subdomains.txt", confirming the number of valid subdomains.
