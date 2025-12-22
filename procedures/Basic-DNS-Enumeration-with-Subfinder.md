---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
sub_techniques: []
tags:
  - dns
  - enumeration
  - reconnaissance
  - subdomain-discovery
commands:
  - '[[commands/subfinder-enumerate-subdomains]]'
platforms:
  - Linux
  - Windows
  - macOS
tools:
  - '[[tools/Subfinder]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Basic-DNS-Enumeration-with-Subfinder

## Summary

This procedure uses Subfinder, a fast passive subdomain discovery tool, to enumerate subdomains associated with a target domain. It leverages online passive sources for reconnaissance without directly querying the target's DNS infrastructure, making it stealthy and effective for initial attack surface mapping in red team engagements or vulnerability assessments.

## Description

Subdomain enumeration is a critical reconnaissance step to identify potential entry points into a target's network by discovering hidden or forgotten subdomains. Subfinder aggregates data from multiple passive sources such as certificate transparency logs, search engines, and threat intelligence feeds. For optimal results, configure API keys for premium sources like VirusTotal or SecurityTrails. This procedure assumes a basic setup and focuses on command-line execution to output a list of discovered subdomains to a file, which can then be used for further probing with tools like httpx or masscan.

## Requirements

1. Subfinder tool installed on the attacker's machine.
2. Network access to the internet for querying passive sources.
3. Optional: API keys configured for enhanced source coverage (e.g., via environment variables or config file).
4. Basic command-line proficiency.

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous DNS queries or traffic to known reconnaissance services (e.g., certificate transparency logs).
- Implement DNS sinkholing and query logging on authoritative servers.
- Use threat intelligence feeds to detect passive reconnaissance attempts against your domains.
- Rate-limit or block access to public APIs used by tools like Subfinder.

## Objectives

1. Discover all accessible subdomains for the target domain to map the attack surface.
2. Output results to a file for chaining with other enumeration tools.
3. Validate the enumeration without generating direct noise on the target network.

## Instructions

### Step 1: Prepare Subfinder Configuration (Optional but Recommended)

**Context**: Setting up API keys enhances Subfinder's coverage by enabling access to premium passive sources, increasing the yield of discovered subdomains without additional effort. This step is performed once before enumeration.

Create or edit the Subfinder config file at `~/.config/subfinder/config.yaml` and add your API keys for sources like VirusTotal, PassiveTotal, or Shodan. For example:

```yaml
virustotal:
  apikey: $_VIRUSTOTAL_API_KEY

passivetotal:
  username: $_PT_USERNAME
  password: $_PT_PASSWORD
```

Replace placeholders with actual keys. Why: Without keys, Subfinder relies on free tiers, which may limit results.

**Expected Output**: No output; configuration is silent. Verify by running `subfinder -h` to ensure no errors on startup.

### Step 2: Enumerate Subdomains Using Subfinder

**Context**: This core step runs the enumeration against the target domain, querying passive sources to compile a list of subdomains. It performs the actual discovery in a non-intrusive manner, avoiding direct interaction with the target's infrastructure.

**Command** ([[commands/subfinder-enumerate-subdomains]]):
```bash
subfinder -d $_DOMAIN -o $_OUTPUT_FILE -silent
```

Why: The `-d` flag specifies the target domain, `-o` directs output to a file for easy parsing, and `-silent` suppresses unnecessary console noise for cleaner logs. Run this from a Kali Linux or similar environment.

**Expected Output**: A file `$_OUTPUT_FILE` containing one subdomain per line, e.g.:
```
mail.example.com
www.example.com
api.example.com
```
If no subdomains are found, the file will be empty or contain only headers.

### Step 3: Verify and Clean Results

**Context**: Post-enumeration, review the output file to remove duplicates or invalid entries, ensuring the subdomain list is usable for subsequent steps like probing for live hosts. This step adds a validation layer to confirm the procedure's success.

Use standard Unix tools to process the output:

```bash
sort -u $_OUTPUT_FILE > $_CLEANED_OUTPUT_FILE
wc -l $_CLEANED_OUTPUT_FILE
```

Why: Subfinder may return duplicates from overlapping sources; sorting and unique-ing ensures efficiency in downstream tools.

**Expected Output**: A cleaned file with unique subdomains and a line count, e.g., `150 $_CLEANED_OUTPUT_FILE`. If the count is zero, revisit API configuration or try a different domain.
