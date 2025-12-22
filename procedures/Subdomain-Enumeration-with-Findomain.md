---
id: 26933c78-ecde-48e6-b025-e68c73554e55
name: Subdomain-Enumeration-with-Findomain
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.550491+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather-Victim-Network-Information|T1590 - Gather Victim Network
    Information]]
sub_techniques: []
tags:
  - subdomain-enumeration
  - findomain
  - reconnaissance
commands:
  - '[[commands/download-findomain-linux-binary]]'
  - '[[commands/make-findomain-linux-executable]]'
  - '[[commands/set-findomain-api-tokens]]'
  - '[[commands/run-findomain-enumerate-subdomains]]'
platforms:
  - Linux
tools:
  - '[[tools/Findomain]]'
validated: true
---

# Subdomain-Enumeration-with-Findomain

## Summary

This procedure outlines how to perform subdomain enumeration on a target domain using Findomain, a fast and cross-platform subdomain enumerator. It involves downloading and setting up the tool, configuring API tokens for enhanced sources, and running the enumeration to discover subdomains through brute-force, search engines, and certificate transparency logs, aiding in reconnaissance to map the target's attack surface.

## Description

Subdomain enumeration is a key reconnaissance technique that helps identify hidden or forgotten subdomains of a target domain, which may host vulnerable services or expose sensitive information. Findomain leverages multiple sources including brute-force wordlists, passive sources like VirusTotal, Spyse, and Facebook's Certificate Transparency logs, as well as active DNS queries. This procedure is suitable for red team engagements or penetration testing where the goal is to expand the attack surface beyond the main domain. The target environment is typically the public internet, requiring no initial access but potentially API keys for optimal results. Expected outcomes include a list of discovered subdomains saved to an output file, which can be further probed for live hosts or vulnerabilities.

## Requirements

1. Linux-based attacker machine (e.g., Kali Linux) with internet access and wget installed.
2. Optional: API tokens from Spyse, VirusTotal, and Facebook for accessing passive intelligence sources.
3. Target domain name (e.g., example.com) in scope for enumeration.
4. Basic command-line proficiency.

## Defense

- Implement DNS monitoring and logging to detect unusual query patterns from external sources.
- Use certificate transparency monitoring tools to track subdomain registrations.
- Restrict subdomain sprawl by regularly auditing and decommissioning unused subdomains.
- Employ web application firewalls (WAFs) and DNS security extensions (DNSSEC) to protect against enumeration attempts.

## Objectives

1. Download and prepare the Findomain tool for use.
2. Configure API tokens to enable passive source enumeration.
3. Enumerate and output subdomains for the target domain.
4. Verify the discovery of valid subdomains for further reconnaissance.

## Instructions

### Step 1: Download Findomain Binary

**Context**: Obtain the latest Linux binary of Findomain from its GitHub releases to ensure you have the tool ready for execution. This step fetches the pre-compiled executable, avoiding compilation requirements.

**Command** ([[commands/download-findomain-linux-binary]]):
```bash
wget https://github.com/Edu4rdSHL/findomain/releases/latest/download/findomain-linux
```

> This command downloads the binary to the current directory. Expected output is a progress bar showing the download, followed by a saved 'findomain-linux' file. Verify the download with 'ls -la findomain-linux' to confirm the file size (around 10-20 MB).

### Step 2: Make Binary Executable

**Context**: Change the permissions on the downloaded binary to make it executable, allowing it to run as a command-line tool. This is a standard step for binaries distributed without execute permissions.

**Command** ([[commands/make-findomain-linux-executable]]):
```bash
chmod +x findomain-linux
```

> No output is produced on success. Verify with 'ls -la findomain-linux' showing '-rwxr-xr-x' permissions. If permissions are not set, the tool will fail to run with a 'Permission denied' error.

### Step 3: Set API Tokens

**Context**: Configure environment variables for API tokens from Spyse, VirusTotal, and Facebook to unlock passive enumeration sources, improving subdomain discovery without relying solely on brute-force. These tokens are optional but recommended for comprehensive results.

**Command** ([[commands/set-findomain-api-tokens]]):
```bash
export findomain_spyse_token="YourSpyseAccessToken"
export findomain_virustotal_token="YourVirusTotalAccessToken"
export findomain_fb_token="YourFacebookAccessToken"
```

> No output on success. These exports set the variables for the current session. If tokens are invalid or missing, Findomain will fall back to free sources but log warnings. Obtain tokens from the respective service dashboards; rate limits apply.

### Step 4: Run Subdomain Enumeration

**Context**: Execute Findomain against the target domain to discover subdomains, outputting results to a file for analysis. The '-t' flag specifies the target, and '-o' enables output; additional flags like '--format json' can be used for structured data.

**Command** ([[commands/run-findomain-enumerate-subdomains]]):
```bash
./findomain-linux -t example.com -o results.txt
```

> Expected output includes a progress summary like '[+] Enumerating subdomains for example.com' followed by discovered subdomains printed to console and saved to 'results.txt'. Success is indicated by a non-empty file with entries like 'sub.example.com'. If no subdomains are found, check API tokens or try recursive mode with '-r'. Post-run, review 'results.txt' for unique domains.
