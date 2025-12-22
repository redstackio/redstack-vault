---
type: procedure
description: >-
  Perform passive reconnaissance on a target domain and infrastructure to gather
  information without direct interaction, using tools like Shodan, Wayback
  Machine, theHarvester, and GitRob.
verified: true
submitted: false
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Search Open Websites/Domains|T1593 - Search Open
    Websites/Domains]]
  - >-
    [[techniques/Search Victim-Owned Websites|T1594 - Search Victim-Owned
    Websites]]
  - >-
    [[techniques/Gather Victim Host Information|T1592 - Gather Victim Host
    Information]]
sub_techniques: []
tags:
  - '[[tags/Bug Hunting Methodology and Enumeration]]'
  - '[[tags/Passive recon]]'
  - reconnaissance
  - information-gathering
commands:
  - '[[commands/nmap-shodan-hq-integration-scan]]'
  - '[[commands/wayback-machine-search-old-endpoints]]'
  - '[[commands/theharvester-domain-reconnaissance-all-sources]]'
  - '[[commands/gitrob-analyze-user-repositories]]'
tools:
  - '[[tools/Nmap]]'
  - '[[tools/theHarvester]]'
  - '[[tools/gitrob]]'
platforms:
  - Linux
  - Web
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Passive Reconnaissance and Information Gathering

## Summary

This procedure outlines passive reconnaissance techniques to collect information about a target domain and its infrastructure without direct interaction, minimizing detection risk. It covers identifying similar applications via Shodan integration with Nmap, discovering forgotten endpoints using the Wayback Machine, harvesting domain details with theHarvester, and analyzing GitHub repositories for sensitive data leaks using GitRob. These steps help map the attack surface, identify assets, and uncover potential vulnerabilities for further exploitation.

## Description

Passive reconnaissance involves gathering publicly available information about a target to understand its digital footprint, including subdomains, historical web content, host details, and leaked credentials. This procedure targets web-based and cloud infrastructures, assuming the attacker has internet access but no initial foothold. Techniques include querying search engines and archives for domain intel, scanning for similar tech stacks, and reviewing public repositories. Expected outcomes include lists of subdomains, historical URLs, email addresses, and exposed secrets. This is ideal for the initial phases of bug hunting or red teaming, where stealth is paramount. Note that while mostly passive, the Shodan-Nmap integration may involve minimal active probing; use with caution in sensitive environments.

## Requirements

1. Internet access to query public APIs and services like Shodan, Wayback Machine, and GitHub.
2. Installed tools: Nmap with shodan-hq NSE script, theHarvester, GitRob, and curl (standard on Linux).
3. API keys: Shodan API key for integrated scans; GitHub personal access tokens for repository analysis.
4. Target details: Domain name, IP/hostname, or GitHub username/organization.
5. Kali Linux or similar environment for tool execution.

## Defense

- Reduce public exposure by implementing domain privacy (e.g., WHOIS protection) and removing sensitive data from GitHub repositories.
- Monitor for reconnaissance tools via API usage logs (Shodan, GitHub) and web archive queries.
- Use certificate transparency logs and subdomain enumeration defenses like DNSSEC to limit harvestable data.
- Regularly audit public repos with tools like GitHub's secret scanning and rotate exposed credentials immediately.

## Objectives

1. Identify the target's digital assets, such as subdomains, historical endpoints, and technology stack, without alerting defenses.
2. Gather contact information, emails, and potential entry points for social engineering or targeted attacks.
3. Uncover leaked sensitive data in public sources to assess compromise risk and plan next steps.
4. Build a comprehensive target profile for subsequent active reconnaissance or exploitation.

## Instructions

### Step 1: Detect Similar Applications Using Shodan Integration

**Context**: Use Shodan to passively identify applications and services similar to those on the target, providing insights into infrastructure without direct scanning. Integrate with Nmap's NSE script for automated querying.

**Command** ([[commands/nmap-shodan-hq-integration-scan]]):
```bash
nmap --script shodan-hq.nse --script-args 'apikey=$_SHODAN_API_KEY,target=$_TARGET_HOST' $_TARGET_HOST
```

> This command queries Shodan's database via Nmap to retrieve information on open ports, services, and similar devices. Replace $_SHODAN_API_KEY with your API key and $_TARGET_HOST with the target's IP or hostname. The script outputs details like service banners and vulnerability indicators if available. This step is useful early to infer tech stack (e.g., web servers, databases) and potential weak points.

**Expected Output**: Nmap scan results including Shodan data, such as "Host: example.com | shodan-hq: Similar devices found: Apache/2.4 on port 80".

### Step 2: Search for Forgotten Endpoints with Wayback Machine

**Context**: Query the Internet Archive's Wayback Machine to find historical versions of the target's website, revealing deprecated endpoints, JavaScript files, or old links that may expose sensitive info or vulnerabilities.

**Command** ([[commands/wayback-machine-search-old-endpoints]]):
```bash
curl -sX GET "http://web.archive.org/cdx/search/cdx?url=$_TARGET_DOMAIN&output=text&fl=original&collapse=urlkey&matchType=prefix"
```

> This curl command uses the CDX API to fetch archived URLs matching the target domain prefix. Replace $_TARGET_DOMAIN with the domain (e.g., example.com). It collapses duplicates and outputs original URLs in text format. Pipe to grep for JS files (e.g., | grep '\.js') to focus on potential API endpoints or configs. This helps discover forgotten admin panels or debug pages.

**Expected Output**: A list of archived URLs, e.g., "http://example.com/old/admin.js" or "http://example.com/api/v1/users".

### Step 3: Harvest Domain Information with theHarvester

**Context**: Collect emails, subdomains, hosts, and IPs associated with the target domain using multiple public sources like Google, Bing, and LinkedIn, all passively.

**Command** ([[commands/theharvester-domain-reconnaissance-all-sources]]):
```bash
theharvester -b all -d $_TARGET_DOMAIN -f output.html
```

> Run theHarvester to query all available sources ('all') for the domain. Replace $_TARGET_DOMAIN with the target (e.g., example.com). The -f flag saves output to HTML for easy review. This aggregates data from search engines, PGP key servers, and more, providing a broad view of the target's online presence without direct contact.

**Expected Output**: Report with sections like "Emails found: user@example.com", "Subdomains: mail.example.com", and virtual hosts.

### Step 4: Analyze GitHub Repositories for Sensitive Information

**Context**: Scan a user's or organization's GitHub repositories for accidentally committed secrets like API keys, passwords, or configs using GitRob, targeting GitHub Enterprise or public instances.

**Command** ([[commands/gitrob-analyze-user-repositories]]):
```bash
gitrob analyze $_USERNAME --site=https://github.com --endpoint=https://api.github.com --access-tokens=$_GITHUB_TOKENS
```

> This launches GitRob to clone and analyze repos for the specified user. Replace $_USERNAME with the target (e.g., johndoe), and $_GITHUB_TOKENS with comma-separated tokens for rate limiting. Use --site and --endpoint for GitHub Enterprise if applicable. It searches for patterns like AWS keys or private certs and generates a report.

**Expected Output**: Console output and JSON report listing findings, e.g., "Found potential AWS key in repo/file.py at line 42".
