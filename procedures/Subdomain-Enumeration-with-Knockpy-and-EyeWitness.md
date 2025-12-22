---
id: f98a740e-d770-4441-882e-5defe5f97904
name: Subdomain-Enumeration-with-Knockpy-and-EyeWitness
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25Z'
updated_at: '2023-04-10T20:25:35Z'
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - subdomain-enumeration
  - dns-recon
  - active-scanning
commands:
  - '[[commands/git-clone-seclists-repository]]'
  - '[[commands/git-clone-knock-repository]]'
  - '[[commands/knockpy-enumerate-subdomains]]'
  - '[[commands/git-clone-eyewitness-repository]]'
  - '[[commands/run-eyewitness-setup-script]]'
  - '[[commands/eyewitness-run-with-filename-and-timeout]]'
  - '[[commands/eyewitness-run-web-scan]]'
  - '[[commands/eyewitness-run-headless-xml-scan]]'
  - '[[commands/eyewitness-run-rdp-scan]]'
platforms:
  - Linux
  - macOS
tools:
  - '[[tools/knockpy]]'
  - '[[tools/eyewitness]]'
validated: true
---

# Subdomain-Enumeration-with-Knockpy-and-EyeWitness

## Summary

This procedure performs subdomain enumeration on a target domain using Knockpy, a Python tool that brute-forces subdomains with a wordlist from SecLists. It then uses EyeWitness to capture screenshots and gather visual intelligence on the discovered subdomains, helping identify web interfaces, RDP services, or other exposed assets for further reconnaissance.

## Description

Subdomain enumeration reveals hidden or forgotten subdomains that may expose sensitive services or misconfigurations. Knockpy sends DNS queries for potential subdomains based on a wordlist, identifying valid ones through responses. EyeWitness then automates browser-based reconnaissance by taking screenshots of HTTP/HTTPS services, RDP logins, or other protocols on those subdomains, providing visual confirmation of technologies in use without manual browsing. This is ideal for initial reconnaissance in red team engagements or vulnerability assessments, targeting environments like corporate networks where subdomains might host admin panels or legacy systems. The procedure assumes Kali Linux or similar pentesting distro and requires internet access for cloning repositories.

## Requirements

1. Kali Linux or Ubuntu with Python 3 and Git installed
2. Network access to the target domain's DNS resolver
3. Administrative privileges on the attacking machine for tool installation
4. A wordlist file (e.g., from SecLists) for brute-forcing subdomains

## Defense

- Implement DNS monitoring and logging to detect anomalous queries (e.g., high-volume subdomain lookups)
- Use DNSSEC to prevent spoofing and limit wildcard subdomain resolutions
- Deploy web application firewalls (WAFs) to block automated screenshot tools like EyeWitness via user-agent or behavior analysis
- Regularly audit and remove unused subdomains using tools like DNS Dumpster or internal scans

## Objectives

1. Discover all valid subdomains of the target domain
2. Capture screenshots and metadata of web/RDP services on discovered subdomains
3. Identify potential entry points for further exploitation, such as exposed login pages or unusual ports

## Instructions

### Step 1: Clone SecLists Repository for Wordlists

**Context**: SecLists provides comprehensive wordlists, including subdomain names for brute-forcing. Cloning ensures access to the latest subdomains-top1mil-110000.txt or similar files.

**Command** ([[commands/git-clone-seclists-repository]]):
```bash
git clone https://github.com/danielmiessler/SecLists.git
```

> This clones the SecLists repository. Navigate to SecLists/Discovery/DNS afterward to find wordlists like subdomains-top1mil-110000.txt.

### Step 2: Clone Knock Repository and Enumerate Subdomains

**Context**: Knockpy is cloned from its GitHub repo and run against the target domain using the SecLists wordlist to discover subdomains via DNS brute-forcing.

**Command** ([[commands/git-clone-knock-repository]]):
```bash
git clone https://github.com/guelfoweb/knock.git
```

**Command** ([[commands/knockpy-enumerate-subdomains]]):
```bash
knockpy $_DOMAIN -w $_WORDLIST_PATH
```

> Replace $_DOMAIN with the target (e.g., example.com) and $_WORDLIST_PATH with the full path to the wordlist (e.g., SecLists/Discovery/DNS/subdomains-top1mil-110000.txt). Knockpy will output discovered subdomains to the console and a file like $_DOMAIN.txt. This step may take several minutes depending on wordlist size.

### Step 3: Clone and Setup EyeWitness

**Context**: EyeWitness is a Python tool for automated screenshotting of web and RDP services. Clone and run the setup to install dependencies like Python libraries and PhantomJS.

**Command** ([[commands/git-clone-eyewitness-repository]]):
```bash
git clone https://github.com/ChrisTruncer/EyeWitness.git
```

**Command** ([[commands/run-eyewitness-setup-script]]):
```bash
cd EyeWitness && ./setup/setup.sh
```

> The setup script installs required packages. Ensure you are in the EyeWitness directory before running.

### Step 4: Prepare Input File from Subdomain Enumeration

**Context**: Convert Knockpy output to a format suitable for EyeWitness (e.g., a text file with URLs like http://sub.example.com).

Use a simple script or manual edit to prefix discovered subdomains with http:// and save to urls.txt. For example:
```bash
echo "http://$(cat example.com.txt)" > urls.txt
```

### Step 5: Run EyeWitness Scans on Discovered Subdomains

**Context**: Use EyeWitness variants to scan web, RDP, or headless modes based on the input file from subdomain results. Adjust options for timeout and output.

**Command** ([[commands/eyewitness-run-web-scan]]):
```bash
./EyeWitness.py -f urls.txt --web
```

> Scans web services in urls.txt, taking screenshots and generating an HTML report in /reports.

**Command** ([[commands/eyewitness-run-with-filename-and-timeout]]):
```bash
./EyeWitness.py -f urls.txt -t $_TIMEOUT --open
```

> Adds a custom timeout (e.g., 10 seconds) per page and auto-opens the report in a browser.

**Command** ([[commands/eyewitness-run-headless-xml-scan]]):
```bash
./EyeWitness.py -f urls.xml -t 8 --headless
```

> For XML input (e.g., from Nmap), runs without GUI using headless browser.

**Command** ([[commands/eyewitness-run-rdp-scan]]):
```bash
./EyeWitness.py -f rdp.txt --rdp
```

> Scans RDP endpoints if subdomains expose port 3389; prepare rdp.txt with rdp://sub.example.com entries.

> Review the generated HTML report for screenshots, titles, and tech stack hints (e.g., login pages indicating CMS).
