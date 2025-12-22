---
id: 4580bc90-1e62-4f50-ac1b-90a68da04c84
name: Subdomain-Enumeration-and-Takeover-Detection-using-SubOver
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.839553+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
  - '[[tactics/Resource Development|TA0042 - Resource Development]]'
techniques:
  - '[[techniques/Acquire Infrastructure|T1583 - Acquire Infrastructure]]'
  - '[[techniques/Active Scanning|T1595 - Active Scanning]]'
  - >-
    [[techniques/Search Open Technical Databases|T1596 - Search Open Technical
    Databases]]
sub_techniques: []
tags:
  - '[[tags/Subdomain-Enumeration]]'
  - '[[tags/Subdomain-Takeover]]'
  - '[[tags/SubOver]]'
commands:
  - '[[commands/install-subover-via-go]]'
  - '[[commands/run-subover-subdomain-check]]'
platforms:
  - Linux
tools:
  - '[[tools/subover]]'
validated: true
---

# Subdomain-Enumeration-and-Takeover-Detection-using-SubOver

## Summary

This procedure utilizes the SubOver tool to analyze a list of subdomains for a target domain, identifying those vulnerable to subdomain takeover. Subdomain takeover occurs when a subdomain's DNS record points to a decommissioned third-party service (e.g., AWS S3, GitHub Pages), allowing an attacker to claim control of the subdomain and potentially host malicious content under the trusted domain.

## Description

Subdomain enumeration involves discovering all subdomains associated with a target domain to map the attack surface. SubOver extends this by performing automated checks against a database of known service fingerprints, resolving DNS records and verifying if they match patterns of unused or dangling services. This is particularly useful in reconnaissance phases to identify low-hanging fruit for infrastructure acquisition. The procedure assumes a pre-existing list of subdomains (e.g., from tools like Subfinder or Amass) and focuses on takeover detection. Successful execution reveals exploitable subdomains that can be claimed via the respective service providers, enabling phishing, malware distribution, or further attacks while masquerading as legitimate infrastructure.

## Requirements

1. Go programming language installed (version 1.13 or later) for tool installation.
2. A text file containing a list of subdomains to check (one per line, e.g., subdomains.txt).
3. Network access to perform DNS resolutions and connect to third-party services for fingerprinting.
4. Basic command-line proficiency on a Linux-based system (e.g., Kali Linux).

## Defense

- Regularly audit and monitor all DNS records using tools like DNS reconnaissance scanners to detect dangling entries.
- Implement automated cleanup processes to remove DNS records for decommissioned services.
- Enable DNSSEC to validate DNS responses and prevent spoofing or unauthorized claims.
- Use subdomain validation and certificate pinning to restrict unverified subdomains from serving content.

## Objectives

1. Load and process a list of target subdomains for analysis.
2. Perform DNS resolution and service fingerprinting to detect takeover vulnerabilities.
3. Output a report of vulnerable subdomains with details on the affected service for potential exploitation or remediation.

## Instructions

### Step 1: Install SubOver

**Context**: Before running the takeover detection, install the SubOver tool from its GitHub repository using Go. This step ensures the binary is available in your GOPATH for execution.

**Command** ([[commands/install-subover-via-go]]):
```bash
go get github.com/Ice3man543/SubOver
```

> This command fetches and installs SubOver. After installation, navigate to the directory (typically $GOPATH/src/github.com/Ice3man543/SubOver) and build the binary if necessary with 'go build'. Expected output includes download progress and a success message indicating the tool is installed. Verify by running './SubOver -h' to see usage options.

### Step 2: Run SubOver for Takeover Detection

**Context**: With SubOver installed and a subdomain list prepared (e.g., subdomains.txt generated from prior enumeration), execute the tool to check each subdomain for takeover vulnerabilities. This step resolves CNAME records and matches them against known dangling service patterns.

**Command** ([[commands/run-subover-subdomain-check]]):
```bash
./SubOver -l subdomains.txt
```

> This scans the provided list and outputs results for each subdomain, flagging vulnerabilities like 'Vulnerable: blog.example.com -> AWS-S3 (CNAME points to non-existent bucket)'. Successful execution produces a console report listing safe, vulnerable, and unknown subdomains. Review the output for actionable takeovers, such as claiming a GitHub page by creating a repository with the matching name.
