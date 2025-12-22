---
id: proc-scan-subdomains-fdns
name: Scan-for-Subdomains-Using-Rapid7-FDNS-Dataset
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.664Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
tags:
  - reconnaissance
  - dns-enumeration
platforms:
  - DNS
tools:
  - '[[tools/Rapid7-FDNS-Dataset]]'
commands: []
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---

# Scan-for-Subdomains-Using-Rapid7-FDNS-Dataset

## Summary

This procedure uses Rapid7's Forward DNS (FDNS) dataset to passively scan and enumerate subdomains of a target domain, such as starbucks.bg, identifying potential entry points for subdomain takeover attacks as part of reconnaissance in academic or security research.

## Description

In a subdomain takeover attack, the first step is to discover all subdomains associated with the target organization. Rapid7's FDNS dataset, a comprehensive collection of forward DNS records crawled from the internet, allows querying for patterns like *.starbucks.* without alerting the target. This reveals subdomains like mail.starbucks.bg that may have dangling records pointing to unused third-party services. The procedure assumes access to the dataset (publicly available) and basic scripting for querying, targeting environments with exposed DNS configurations.

## Requirements

1. Download access to Rapid7's FDNS dataset (e.g., via their open data project)
2. Tools for querying large datasets (e.g., grep, awk, or Python scripts)
3. Internet connectivity for dataset retrieval

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAME/NS entries using tools like DNSdumpster or internal scanners
- Implement DNS monitoring with services like Cloudflare or Route 53 to alert on unresolved subdomains
- Use certificate transparency logs to track subdomain registrations

## Objectives

1. Enumerate all subdomains under the target domain
2. Identify candidates for takeover by spotting external service pointers
3. Build a reconnaissance map for further vulnerability assessment

## Instructions

### Step 1: Download and Prepare the Dataset

**Context**: Obtain the latest FDNS dataset from Rapid7, which contains billions of DNS records in a tabular format (e.g., domain, timestamp, resolved IP).

No specific command, but download via:

```bash
wget https://datasets.powerdns.com/fdns/YYYY-MM.csv.gz
```

> Decompress and load into a queryable format. Expected output: A large CSV file ready for searching.

### Step 2: Query for Target Subdomains

**Context**: Search the dataset for subdomains matching the target pattern to list all associated domains.

Use grep or similar:

```bash
zcat fdns-2023-01.csv.gz | grep "starbucks.bg" > starbucks_subdomains.txt
```

> This filters records containing starbucks.bg, outputting a list of subdomains. Expected output: Text file with entries like mail.starbucks.bg.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Rapid7-FDNS-Dataset]]

## Tags

- [[Reconnaissance]]
- [[dns-enumeration]]
