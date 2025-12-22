---
id: 5c56665b-bb89-41ae-8603-a1bdd3e91e3e
name: Subdomain-Enumeration-and-Takeover-with-tko-subs
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.777352+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Search Open Technical Databases|T1596 - Search Open Technical
    Databases]]
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Subdomain-Enumeration]]'
  - '[[tags/Subdomain-Takeover]]'
  - '[[tags/tko-subs]]'
commands:
  - '[[commands/go-install-tko-subs]]'
  - '[[commands/tko-subs-scan-domains-for-takeover]]'
platforms:
  - Linux
tools:
  - '[[tools/tko-subs]]'
validated: true
---

# Subdomain-Enumeration-and-Takeover-with-tko-subs

## Summary

This procedure uses the tko-subs tool to enumerate subdomains of a target organization and identify opportunities for subdomain takeover. Subdomain takeover occurs when a subdomain points to an external service (like AWS S3 or GitHub Pages) that the domain owner no longer controls, allowing an attacker to claim it and potentially redirect traffic, host malicious content, or gain trusted access to the organization's infrastructure.

## Description

Subdomain enumeration involves discovering all subdomains associated with a target domain, often revealing forgotten or misconfigured assets. The tko-subs tool automates the detection of takeover vulnerabilities by checking DNS records against a database of known service providers' CNAME patterns. If a subdomain's CNAME matches an unused resource on a third-party service, an attacker can register that resource to hijack the subdomain. This technique is commonly used in reconnaissance to expand the attack surface and can lead to initial access if the hijacked subdomain is used for phishing, malware delivery, or bypassing security controls. The procedure assumes a Linux environment with Go installed and requires a list of target domains and provider data for accurate scanning.

## Requirements

1. Linux system with Go 1.16+ installed for building tko-subs.
2. Internet access to download the tool and query DNS.
3. A text file containing target domains (one per line).
4. The providers-data.csv file, which maps service providers to their CNAME fingerprints (downloaded or generated separately).
5. Basic command-line knowledge for running Go tools.

## Defense

- Regularly audit and inventory all subdomains using tools like DNS enumeration scanners.
- Implement automated monitoring for DNS changes and CNAME records pointing to third-party services.
- Remove or update unused cloud resources (e.g., S3 buckets, Heroku apps) to prevent takeover.
- Use domain shadowing prevention services and enforce strict DNS policies.
- Monitor for anomalous traffic from hijacked subdomains.

## Objectives

1. Enumerate subdomains associated with the target organization from a provided domain list.
2. Identify subdomains vulnerable to takeover by checking against known provider patterns.
3. Report potential takeover opportunities for further exploitation, such as claiming the subdomain for malicious use.

## Instructions

### Step 1: Install tko-subs

**Context**: Download and build the tko-subs tool from its GitHub repository using Go. This step ensures the tool is available locally for scanning.

**Command** ([[commands/go-install-tko-subs]]):
```bash
go install github.com/anshumanbh/tko-subs@latest
```

> This command fetches the source code and compiles the binary into $GOPATH/bin (ensure $GOPATH/bin is in your PATH). Expected output includes build progress and a success message if compilation completes without errors. Verify installation by running `tko-subs --help` to see usage options.

### Step 2: Prepare Input Files

**Context**: Create or obtain the necessary input files: a domains list and the providers data CSV. The domains file should contain target domains (e.g., example.com), and the CSV lists provider CNAMEs for takeover detection.

**Instructions**: 
- Create a file `domains_tkos.txt` with target domains, one per line:
```bash
echo "target.com" > lists/domains_tkos.txt
echo "sub.target.com" >> lists/domains_tkos.txt
```
- Download or generate `providers-data.csv`. If not available, fetch from the tool's repository or common sources:
```bash
mkdir -p lists
wget https://raw.githubusercontent.com/anshumanbh/tko-subs/master/providers-data.csv -O lists/providers-data.csv
```

> These steps set up the directory structure (e.g., `./lists/`) and files. Expected output: Files created or downloaded successfully, verifiable with `ls lists/` showing the files.

### Step 3: Scan for Subdomain Takeovers

**Context**: Run tko-subs to query DNS for subdomains and check for takeover vulnerabilities using the prepared files. This identifies dangling DNS records pointing to claimable services.

**Command** ([[commands/tko-subs-scan-domains-for-takeover]]):
```bash
tko-subs -domains=./lists/domains_tkos.txt -data=./lists/providers-data.csv
```

> The `-domains` flag points to the input domain list, and `-data` to the providers CSV. The tool will resolve DNS, match CNAMEs, and output vulnerable subdomains. Expected output: A report listing potential takeovers, e.g., "Vulnerable: sub.target.com -> github.io (claimable GitHub page)". If no vulnerabilities, it reports none found. Review the output for actionable items like service type and takeover instructions.
