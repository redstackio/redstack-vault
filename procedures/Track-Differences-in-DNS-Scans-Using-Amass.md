---
id: 2838ee6c-c272-40c5-8b9c-fb54eb29cb80
name: Track-Differences-in-DNS-Scans-Using-Amass
type: procedure
verified: true
submitted: false
created_at: '2020-07-02T14:57:18.386822+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Network Information]]'
sub_techniques:
  - '[[Domain Properties]]'
tags:
  - dns
  - reconnaissance
  - amass
  - subdomain-enumeration
commands:
  - '[[commands/amass-track-scan-differences]]'
platforms:
  - Linux
tools:
  - '[[tools/amass]]'
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
---

# Track-Differences-in-DNS-Scans-Using-Amass

## Summary

This procedure uses the Amass tool to compare results from previous DNS enumeration scans stored in a database directory, identifying new or changed domains since the last scan. It is particularly useful during re-engagement pentests to quickly spot newly registered subdomains or alterations in the target's DNS footprint without manually reviewing old reports or spreadsheets.

## Description

Amass is a DNS reconnaissance and network mapping tool that can perform both passive and active enumeration of subdomains and related assets. When run with the `-dir` option, it stores scan results in a SQLite database file within the specified directory. The `amass track` subcommand allows diffing these databases to highlight differences between scans, such as newly discovered domains. This technique assumes prior scans have been conducted and saved in the same directory. It maps to MITRE ATT&CK under Reconnaissance for gathering victim network information, specifically domain properties. The procedure is low-risk for detection as it involves passive comparison of local data but requires initial network access for the original scans.

## Requirements

1. Amass tool installed and accessible in the PATH.
2. A directory containing at least two previous Amass scan databases (e.g., from `amass enum -dir output_dir -d target.com` runs).
3. Network access to the target domain if verifying new findings (optional for diffing).
4. Basic command-line proficiency on a Linux-based system like Kali.

## Defense

Defensive measures and detection strategies:

- Monitor for repeated DNS queries from known reconnaissance tools like Amass via network logs or DNS server analytics.
- Implement DNS rate limiting and anomaly detection to flag bulk subdomain enumeration attempts.
- Use certificate transparency logs and passive DNS monitoring services to track new subdomain registrations proactively.
- Regularly audit and clean up stale subdomains to reduce the attack surface revealed in diffs.

## Objectives

1. Identify newly registered or altered subdomains since the last scan.
2. Streamline re-pentest workflows by automating comparison of historical DNS data.
3. Provide actionable intelligence on changes in the target's digital footprint.
4. Verify the diff output to prioritize new assets for further enumeration or testing.

## Instructions

### Step 1: Verify Previous Scan Databases

**Context**: Before running the diff, confirm that the output directory contains multiple Amass database files from prior scans. Each scan creates a timestamped SQLite file (e.g., `amass_YYYYMMDD_HHMMSS.db`). If no prior scans exist, perform an initial enumeration using Amass's `enum` mode to generate the first database.

This step ensures the prerequisites are met and prevents errors from missing data.

### Step 2: Run Amass Track to Diff Scans

**Context**: Execute the `amass track` command to compare the last two scans (or specify a number with `-last N`). This will output differences, such as new domains found in the more recent scan.

**Command** ([[commands/amass-track-scan-differences]]):
```bash
amass track -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -last 2
```

> This command loads the databases from the specified directory, compares the most recent two scans for the given domain, and displays any differences like added or removed subdomains. The `-last 2` flag limits comparison to the two latest scans; adjust for more if needed. Run this from the terminal on your assessment machine.

### Step 3: Analyze and Export Differences

**Context**: Review the console output for new domains. If differences are found, export them to a file for further processing, such as feeding into other tools like httpx for liveliness checks or masscan for port scanning.

Redirect the output to a file for persistence:
```bash
amass track -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -last 2 > diff_results.txt
```

> Parse the output manually or with grep to isolate new domains (e.g., `grep 'new' diff_results.txt`). If no differences are shown, it indicates stability in the DNS records since the last scan. Follow up by validating new domains with additional reconnaissance procedures.
