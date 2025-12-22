---
type: procedure
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
sub_techniques: []
tags:
  - dns
  - enumeration
  - reconnaissance
  - subdomain
commands:
  - '[[commands/findomain-target-domain-scan]]'
platforms:
  - Network
tools:
  - '[[tools/Finddomain]]'
skill_level: beginner
impact_level: low
detection_risk: low
verified: true
validated: true
---

# Basic-DNS-Enumeration-with-Finddomain

## Summary

This procedure uses the Finddomain tool to perform passive DNS enumeration on a target domain, discovering associated subdomains that can reveal the attack surface for further reconnaissance activities. It leverages multiple passive sources like search engines, certificate transparency logs, and public databases to gather subdomain information without directly querying the target's DNS servers, minimizing detection risk.

## Description

DNS enumeration is a foundational reconnaissance technique in offensive security operations, aimed at mapping the target's domain infrastructure. Finddomain automates the collection of subdomains by querying passive intelligence sources, providing a fast and stealthy alternative to active scanning methods like brute-forcing. This procedure is typically used during the initial phases of an engagement to identify potential entry points, such as web applications on subdomains. It assumes the attacker has no prior access and is operating from an external network position. Expected outcomes include a list of valid subdomains that can be probed for vulnerabilities or used in phishing campaigns. The technique aligns with gathering victim host information to understand the target's digital footprint.

## Requirements

1. Finddomain tool installed on a Linux-based system (e.g., Kali Linux).
2. Network access to the internet for querying passive sources.
3. A target domain name (e.g., example.com) with no special permissions required.
4. Basic command-line proficiency.

## Defense

Defensive measures and detection strategies:

- Implement DNS query logging and monitoring for unusual patterns from passive sources.
- Use certificate transparency monitoring tools to track subdomain registrations.
- Rate-limit or block automated queries to search engines and public APIs used by enumeration tools.
- Employ web application firewalls (WAFs) to detect reconnaissance attempts on discovered subdomains.

## Objectives

1. Identify all publicly discoverable subdomains associated with the target domain.
2. Compile a list of subdomains for subsequent active probing or vulnerability assessment.
3. Minimize active network interactions to reduce the risk of detection during reconnaissance.

## Instructions

### Step 1: Verify Tool Installation

**Context**: Ensure Finddomain is properly installed and accessible to avoid execution errors. This step confirms the tool's availability and version, which is crucial for reliable enumeration.

Refer to the [[tools/Finddomain]] documentation for installation if needed. Run a help command to verify functionality.

**Command** ([[commands/findomain-help]]):
```bash
finddomain --help
```

> This displays the tool's usage options and confirms installation. If the command is not found, install via the tool's repository.

### Step 2: Execute Subdomain Enumeration

**Context**: Perform the core enumeration by specifying the target domain. Finddomain will query passive sources like VirusTotal, CRT.sh, and search engines to compile a list of subdomains. This step is the primary action and should be run in a directory where output can be saved for further analysis.

**Command** ([[commands/findomain-target-domain-scan]]):
```bash
findomain -t $_TARGET_DOMAIN -o $_OUTPUT_FILE
```

> Replace $_TARGET_DOMAIN with the actual domain (e.g., owasp.org) and $_OUTPUT_FILE with a filename like subdomains.txt. The tool runs passively, so expect it to take 1-5 minutes depending on the domain's exposure. Success is indicated by the generation of an output file without errors.

### Step 3: Review and Validate Results

**Context**: Examine the output file to identify unique subdomains and remove duplicates or false positives. This step ensures the data is usable for the next reconnaissance phases, such as probing for live hosts.

Use standard Linux commands to inspect the file:

```bash
sort -u $_OUTPUT_FILE | tee unique_subdomains.txt
wc -l unique_subdomains.txt
```

> The sort -u command deduplicates the list, and wc -l counts the number of subdomains. Expected results include 10-100+ subdomains for a typical organization. If the list is empty, consider alternative tools or verify the target domain's validity.
