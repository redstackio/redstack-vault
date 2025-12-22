---
id: 4cd57084-ad1f-4e97-be7f-fdb450e1d9cf
name: Subdomain-Enumeration-and-Takeover-using-Hostile-Subdomain-Bruteforcer
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.807525+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Host Information|T1592 - Gather Victim Host
    Information]]
  - >-
    [[techniques/Gather Victim Network Information|T1590 - Gather Victim Network
    Information]]
sub_techniques: []
tags:
  - '[[tags/Subdomain-Enumeration]]'
  - '[[tags/Subdomain-Takeover]]'
  - '[[tags/Hostile-Subdomain-Bruteforcer]]'
commands:
  - '[[commands/git-clone-hostile-subbruteforcer-repo]]'
  - '[[commands/chmod-plus-x-sub-brute-rb]]'
  - '[[commands/run-hostile-subdomain-bruteforcer]]'
platforms:
  - Linux
tools:
  - '[[tools/Hostile-Subdomain-Bruteforcer]]'
validated: true
---

# Subdomain-Enumeration-and-Takeover-using-Hostile-Subdomain-Bruteforcer

## Summary

This procedure uses the Hostile Subdomain Bruteforcer tool to perform automated subdomain enumeration via bruteforce against a target domain and identify potential subdomain takeover vulnerabilities. It discovers hidden subdomains that may point to unused or misconfigured services, allowing attackers to claim control for phishing, malware hosting, or data interception. The tool combines wordlist-based bruteforcing with checks against known vulnerable CNAME providers like GitHub Pages or Heroku.

## Description

Subdomain enumeration reveals the attack surface of a target by identifying subdomains, which often expose internal applications, forgotten services, or weak configurations. Subdomain takeover occurs when a subdomain's DNS record points to a third-party service (e.g., AWS S3 bucket) that is no longer in use by the owner, allowing an attacker to register the service and hijack traffic. Hostile Subdomain Bruteforcer automates this by bruteforcing potential subdomains using a wordlist, resolving them via DNS, and fingerprinting responses to detect takeover opportunities. This is useful in red team engagements for reconnaissance and in blue team scenarios for auditing domain hygiene. The procedure assumes a Linux environment with Ruby installed and requires internet access for DNS queries.

## Requirements

1. Linux system with Ruby 2.0+ installed (e.g., via `apt install ruby` on Ubuntu).
2. Target domain name (e.g., example.com).
3. Wordlist file for bruteforcing (default or custom, e.g., common subdomains like 'www', 'admin', 'api').
4. Internet access for DNS resolution and GitHub cloning.
5. Optional: Custom wordlist with subdomain names (e.g., SecLists or custom).

## Defense

- Regularly audit and remove unused subdomains using tools like DNS Dumpster or Subdomain Takeover scanners.
- Implement monitoring for DNS changes with services like Cloudflare or Route 53 notifications.
- Use DNSSEC to validate records and prevent spoofing.
- Scan for dangling CNAMEs pointing to third-party services and delete or update them.
- Employ certificate transparency logs to detect unauthorized subdomain registrations.

## Objectives

1. Enumerate potential subdomains of the target domain using bruteforce.
2. Identify subdomains vulnerable to takeover by checking for dangling records.
3. Generate a report of discovered subdomains and takeover candidates for further exploitation or remediation.

## Instructions

### Step 1: Clone the Hostile Subdomain Bruteforcer Repository

**Context**: Download the tool from GitHub to obtain the sub_brute.rb script and default wordlist. This sets up the local environment for execution.

**Command** ([[commands/git-clone-hostile-subbruteforcer-repo]]):
```bash
git clone https://github.com/nahamsec/HostileSubBruteforcer
```

> This command fetches the repository. Expected output includes progress messages ending with 'Cloning into 'HostileSubBruteforcer'...'. Verify by listing the directory contents to see sub_brute.rb and wordlist.txt.

### Step 2: Navigate and Prepare the Script

**Context**: Change to the tool's directory and make the Ruby script executable to run it directly.

**Command** ([[commands/chmod-plus-x-sub-brute-rb]]):
```bash
cd HostileSubBruteforcer
chmod +x sub_brute.rb
```

> The cd command moves into the directory (expected: no output, confirm with `pwd`). The chmod sets execute permissions (expected: no output, verify with `ls -l sub_brute.rb` showing -rwxr-xr-x).

### Step 3: Run Subdomain Enumeration and Takeover Check

**Context**: Execute the tool against the target domain, specifying a wordlist and threads for efficiency. The script will bruteforce subdomains, resolve DNS, and check for takeover fingerprints.

**Command** ([[commands/run-hostile-subdomain-bruteforcer]]):
```bash
./sub_brute.rb -d $_DOMAIN -w $_WORDLIST -t $_THREADS
```

> Replace placeholders with actual values (e.g., -d example.com -w wordlist.txt -t 50). This performs the bruteforce and scanning. Expected output includes discovered subdomains, resolved IPs, and alerts like 'TAKEOVER POSSIBLE: subdomain.example.com points to vulnerable GitHub Page'. If no wordlist is specified, it uses the default. Decision point: If threads cause rate-limiting, reduce $_THREADS; if no hits, try a larger wordlist.
