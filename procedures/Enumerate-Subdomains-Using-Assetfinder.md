---
id: 653188aa-3f50-4c10-8e5a-8cf698c40059
name: Enumerate-Subdomains-Using-Assetfinder
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:30.492249+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
sub_techniques: []
tags:
  - reconnaissance
  - dns
  - subdomain-enumeration
commands:
  - '[[commands/assetfinder-enumerate-subdomains]]'
platforms:
  - Linux
tools:
  - '[[tools/Assetfinder]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Enumerate-Subdomains-Using-Assetfinder

## Summary

This procedure uses the assetfinder tool to perform passive subdomain enumeration for a target domain, discovering potential subdomains through public sources like certificate transparency logs and search engines. It is a foundational reconnaissance step to map the attack surface without direct interaction with the target's infrastructure.

## Description

Subdomain enumeration is a critical initial phase in reconnaissance, helping identify hidden or forgotten subdomains that may expose additional attack vectors, such as administrative interfaces or misconfigured services. Assetfinder aggregates data from multiple passive sources, including crt.sh, Facebook Certificate Transparency logs, and VirusTotal, to compile a list of subdomains efficiently. This technique is non-intrusive, as it does not query the target's DNS servers directly, reducing the risk of detection. It is particularly useful in red team engagements or penetration tests targeting web applications and domains. Expected outcomes include a comprehensive list of subdomains, which can be further validated for liveliness using tools like httpx or massdns.

## Requirements

1. Assetfinder tool installed on a Linux system (see [[tools/Assetfinder]] for installation).
2. Network access to public sources (internet connectivity required; no direct access to the target domain needed).
3. Target domain name (e.g., example.com) provided as input.
4. Basic command-line familiarity.

## Defense

Defensive measures and detection strategies:

- Monitor for passive reconnaissance tools via network traffic to known sources like crt.sh or VirusTotal APIs.
- Implement certificate transparency monitoring to track subdomain registrations.
- Use DNS logging to correlate discovered subdomains with actual queries.
- Deploy tools like Subfinder or Amass on the defensive side to simulate and baseline expected enumeration results.

## Objectives

1. Discover all known subdomains associated with the target domain passively.
2. Compile a list for further validation and mapping of the attack surface.
3. Identify potential entry points without alerting the target.

## Instructions

### Step 1: Prepare the Target Domain

**Context**: Identify the root domain to enumerate. This ensures the tool targets the correct scope and avoids irrelevant results.

Ensure you have the domain name ready. No command is needed here; simply note the target (e.g., owasp.com).

### Step 2: Run Assetfinder Enumeration

**Context**: Execute the assetfinder tool to query passive sources and retrieve subdomain data. This step performs the core enumeration, outputting unique subdomains to stdout or a file for review.

**Command** ([[commands/assetfinder-enumerate-subdomains]]):
```bash
assetfinder $_DOMAIN
```

> This command queries multiple passive data sources and lists discovered subdomains. Redirect output to a file if needed for further processing (e.g., `assetfinder $_DOMAIN > subdomains.txt`). The process typically takes seconds to minutes depending on the domain's visibility.

### Step 3: Review and Deduplicate Results

**Context**: Examine the output for unique subdomains and remove duplicates if any. This verifies the completeness of the enumeration and prepares data for the next reconnaissance steps.

Use standard Unix tools to process the output:
```bash
sort subdomains.txt | uniq > unique_subdomains.txt
```

> Manually inspect the list for relevant subdomains (e.g., admin.example.com, api.example.com). Success is indicated by a non-empty list of subdomains beyond the root domain.
