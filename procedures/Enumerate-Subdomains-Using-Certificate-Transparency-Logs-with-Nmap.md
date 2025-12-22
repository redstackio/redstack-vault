---
id: 1df850c8-2298-4ac6-af8e-8502e1b8962d
name: Enumerate-Subdomains-Using-Certificate-Transparency-Logs-with-Nmap
type: procedure
verified: true
submitted: false
created_at: '2020-06-30T01:33:49.208576+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Hardware]]'
sub_techniques:
  - '[[Hardware]]'
tags:
  - reconnaissance
  - subdomain-enumeration
  - certificate-transparency
commands:
  - '[[commands/nmap-hostmap-crtsh-enumerate-subdomains]]'
platforms:
  - Linux
tools:
  - '[[tools/Nmap]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Enumerate-Subdomains-Using-Certificate-Transparency-Logs-with-Nmap

## Summary

This procedure uses Nmap's hostmap-crtsh script to query Google's Certificate Transparency Logs (via crt.sh) for subdomains associated with a target domain. It is a passive reconnaissance technique that reveals potential subdomains without directly interacting with the target's infrastructure, helping to map the attack surface early in an engagement.

## Description

Certificate Transparency Logs publicly record SSL/TLS certificates issued for domains, including subdomains. The hostmap-crtsh Nmap Scripting Engine (NSE) script automates queries to crt.sh, extracting subdomain information from these logs. This method is useful during reconnaissance phases to identify hidden or forgotten subdomains that could serve as entry points for further attacks. It requires no authentication or direct network access to the target beyond resolving the domain name and is effective against organizations with issued certificates. The output lists discovered subdomains, which can be fed into other tools for validation and enumeration.

## Requirements

1. Nmap installed with NSE support (version 7.0 or later).
2. Internet access to query crt.sh.
3. Target domain name (e.g., example.com) that has issued certificates.
4. Basic command-line proficiency.

## Defense

Defensive measures and detection strategies:

- Monitor for automated queries to certificate transparency services like crt.sh from reconnaissance tools.
- Implement certificate issuance policies to limit unnecessary subdomain certificates.
- Use tools like Certificate Transparency monitoring services to track and revoke exposed certificates.
- Network logs may show DNS resolutions or HTTP requests to crt.sh, though this is passive and hard to attribute.

## Objectives

1. Discover subdomains associated with the target domain via public certificate logs.
2. Compile a list of potential attack surfaces without alerting the target.
3. Provide input for active scanning or further reconnaissance.

## Instructions

### Step 1: Prepare the Target Domain

**Context**: Identify the root domain to query. Ensure it is a valid domain with likely certificate issuances. This step involves no execution but sets up the parameter for the scan.

Resolve the domain if needed to confirm it's active, but no command is required here.

### Step 2: Run the Nmap hostmap-crtsh Script

**Context**: Execute the NSE script to query crt.sh for subdomains. This performs a host discovery (-sn) combined with the script, focusing on passive enumeration.

**Command** ([[commands/nmap-hostmap-crtsh-enumerate-subdomains]]):
```bash
nmap -sn --script hostmap-crtsh $_TARGET_DOMAIN
```

> This command initiates a ping scan (-sn) on the target domain and runs the hostmap-crtsh script, which fetches subdomain data from crt.sh. Replace $_TARGET_DOMAIN with the actual domain (e.g., redstack.io). The script handles the query and parses the JSON response from crt.sh to list unique subdomains.

### Step 3: Review and Parse Output

**Context**: Analyze the script results to extract subdomains. If successful, the output includes a table of subdomains under the host script results section.

Save the output to a file for further processing:
```bash
nmap -sn --script hostmap-crtsh $_TARGET_DOMAIN -oN subdomains.txt
```

> Manually extract subdomains from the output or use grep/awk for automation, e.g., `grep -oE '[a-zA-Z0-9.-]+\.$_TARGET_DOMAIN' subdomains.txt`. Verify subdomains with tools like httpx or dnsx for liveliness.
