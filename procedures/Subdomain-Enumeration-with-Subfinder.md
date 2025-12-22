---
id: 75436540-8c96-4524-876c-e65e93d01e2b
name: Subdomain-Enumeration-with-Subfinder
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.509044+00:00'
updated_at: '2023-04-10T20:25:39.498551+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Search Open Technical Databases|T1596 - Search Open Technical
    Databases]]
sub_techniques:
  - '[[sub-techniques/DNS/Passive DNS|T1596.001 - DNS/Passive DNS]]'
tags:
  - '[[tags/enumerate-all-subdomains-scope-wildcard]]'
  - '[[tags/subdomain-enumeration]]'
  - '[[tags/using-subfinder]]'
commands:
  - '[[commands/install-subfinder]]'
  - '[[commands/run-subfinder-enumeration]]'
  - '[[commands/set-censys-credentials-for-subfinder]]'
  - '[[commands/set-passivetotal-credentials-for-subfinder]]'
  - '[[commands/set-riddler-credentials-for-subfinder]]'
  - '[[commands/set-securitytrails-credentials-for-subfinder]]'
platforms:
  - Linux
tools:
  - '[[tools/Subfinder]]'
validated: true
---

# Subdomain-Enumeration-with-Subfinder

## Summary

This procedure uses Subfinder, a fast and efficient subdomain discovery tool, to enumerate subdomains for a target domain by querying multiple passive sources such as Certificate Transparency logs, VirusTotal, and DNS databases. It is ideal for the reconnaissance phase to map out an organization's attack surface without direct interaction with the target infrastructure.

## Description

Subdomain enumeration identifies valid subdomains associated with a target domain, revealing hidden or forgotten assets that could serve as entry points for further attacks. Subfinder leverages passive intelligence from public APIs and databases, including PassiveTotal, Riddler, Censys, and SecurityTrails, to compile a comprehensive list of subdomains. Written in Go, it supports both passive resolution and optional brute-forcing, making it suitable for red team engagements where stealth is prioritized. In an attack scenario, this procedure helps attackers discover services like admin portals or staging environments that may have weaker security controls. Prerequisites include API keys from the supported providers for optimal results, and it assumes a Linux environment with Go installed for setup. Expected outcomes include a text file listing unique subdomains, which can be fed into tools like httpx for live host probing.

## Requirements

1. Linux-based command-line interface with internet access.
2. Go programming language installed (version 1.16 or higher) for installation.
3. API keys from PassiveTotal, Riddler, Censys, and SecurityTrails for enhanced data sources (optional but recommended for comprehensive results).
4. Write permissions to a output directory (e.g., /tmp).

## Defense

Defensive measures and detection strategies:

- Limit subdomain registrations and monitor for unexpected DNS resolutions using tools like DNS logging in BIND or Cloudflare.
- Implement API rate limiting and monitoring on public intelligence services to detect anomalous queries.
- Use DNSSEC to validate responses and prevent spoofing during passive enumeration.
- Deploy network monitoring for unusual outbound API calls from reconnaissance tools.

## Objectives

1. Discover all resolvable subdomains for the target domain to expand the attack surface.
2. Collect passive intelligence without alerting the target.
3. Generate a list of subdomains for further validation and targeting.

## Instructions

### Step 1: Install Subfinder

**Context**: Install Subfinder using Go to make it available for configuration and execution. This step ensures the tool is downloaded and built from the official repository.

**Command** ([[commands/install-subfinder]]):
```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

> This command fetches and compiles the latest version of Subfinder. Run it in a directory where Go binaries are accessible (e.g., $GOPATH/bin). Expected output includes build progress and a success message like "go: downloading github.com/projectdiscovery/subfinder/v2 v2.x.x". Verify installation by running `subfinder -version`.

### Step 2: Configure PassiveTotal Credentials

**Context**: Set API credentials for PassiveTotal to enable queries against their DNS and WHOIS database, improving subdomain discovery from historical records.

**Command** ([[commands/set-passivetotal-credentials-for-subfinder]]):
```bash
subfinder -update-config -set-config PassivetotalUsername='$_USERNAME',PassivetotalKey='$_API_KEY'
```

> Replace $_USERNAME and $_API_KEY with your PassiveTotal account details. This updates Subfinder's configuration file (~/.config/subfinder/config.yaml). Expected output is a confirmation message like "Configuration updated successfully". If credentials are invalid, it will error with authentication failure.

### Step 3: Configure Riddler Credentials

**Context**: Provide Riddler credentials to access their search engine for subdomain data derived from certificate logs and other sources.

**Command** ([[commands/set-riddler-credentials-for-subfinder]]):
```bash
subfinder -update-config -set-config RiddlerEmail='$_EMAIL',RiddlerPassword='$_PASSWORD'
```

> Substitute $_EMAIL and $_PASSWORD with your Riddler account information. This persists the config for future runs. Expected output confirms the update. Test by running a small enumeration to ensure no auth errors.

### Step 4: Configure Censys Credentials

**Context**: Authenticate with Censys to query their internet-wide scan data for hostnames and certificates, uncovering subdomains from global observations.

**Command** ([[commands/set-censys-credentials-for-subfinder]]):
```bash
subfinder -update-config -set-config CensysUsername='$_USERNAME',CensysSecret='$_SECRET'
```

> Use your Censys API username and secret key. Expected output is a success notification. Invalid credentials will prevent Censys data from being included in scans.

### Step 5: Configure SecurityTrails Credentials

**Context**: Set the API key for SecurityTrails to pull historical DNS records and identify subdomains over time.

**Command** ([[commands/set-securitytrails-credentials-for-subfinder]]):
```bash
subfinder -update-config -set-config SecurityTrailsKey='$_API_KEY'
```

> Insert your SecurityTrails API key. This enables access to their DNS history database. Expected output confirms configuration. Without this, Subfinder falls back to free tiers or skips the source.

### Step 6: Run Subdomain Enumeration

**Context**: Execute Subfinder against the target domain to gather subdomains from all configured sources, outputting results to a file for analysis.

**Command** ([[commands/run-subfinder-enumeration]]):
```bash
subfinder -d $_DOMAIN -o $_OUTPUT_FILE -silent -t 50
```

> Specify the target domain (e.g., example.com) for $_DOMAIN and output path (e.g., /tmp/subdomains.txt) for $_OUTPUT_FILE. The -silent flag reduces verbosity, and -t 50 sets 50 threads for speed. Expected output is a progress log showing sources queried, ending with the number of subdomains found (e.g., "[INF] Found 45 subdomains for example.com"). The output file contains one subdomain per line.
