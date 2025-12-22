---
type: procedure
description: >-
  Use Amass database subcommands to list prior enumeration scans and retrieve
  discovered assets like subdomains for reconnaissance review.
verified: true
submitted: false
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Org Information]]'
sub_techniques:
  - '[[Determine Physical Locations]]'
tags:
  - reconnaissance
  - dns
  - subdomain-enumeration
  - amass
  - osint
commands:
  - '[[commands/amass-db-list-previous-scans]]'
  - '[[commands/amass-db-display-assets-from-scan]]'
platforms:
  - Linux
tools:
  - '[[tools/amass]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Query-Amass-Database-for-Previous-Scans-and-Assets

## Summary

This procedure uses the Amass tool's database (db) subcommand to retrieve and review information from previous subdomain enumeration scans. It allows security testers to list all stored scans in a database directory and then display the specific assets (such as subdomains, IP addresses, and ASNs) discovered during a particular scan. This is useful for analyzing reconnaissance results without re-running full enumerations, supporting iterative OSINT and attack surface mapping in penetration testing or red team engagements.

## Description

Amass is a powerful open-source tool for automated network mapping and external asset discovery, particularly focused on DNS-based reconnaissance. After conducting subdomain enumeration with `amass enum`, results are stored in a SQLite database within an output directory. The db subcommand provides options to query this database, enabling efficient retrieval of historical data. This procedure is typically used post-reconnaissance to validate findings, export assets for further testing (e.g., vulnerability scanning), or document attack surface details. It assumes prior runs of Amass enumeration have populated the database and requires read access to the output directory. The technique aligns with gathering victim host information through DNS queries and database introspection, common in early-stage reconnaissance phases.

## Requirements

1. Amass tool installed and accessible via command line (version 3.0 or later recommended).
2. An output directory containing Amass database files (.db) from previous `amass enum` runs.
3. Knowledge of the target domain(s) enumerated in prior scans.
4. Bash shell environment (Linux or compatible, such as Kali Linux or WSL on Windows).
5. Sufficient disk space and permissions to read the database directory.

## Defense

Defensive measures and detection strategies:

- Monitor for Amass processes or similar reconnaissance tools via endpoint detection and response (EDR) tools, looking for `amass` executions or high-volume DNS queries.
- Implement network segmentation and DNS logging to detect anomalous query patterns from external IP ranges associated with known pentesting tools.
- Use database access controls on reconnaissance output directories in shared environments to prevent unauthorized querying.
- Enable application logging for DNS resolvers to identify repeated historical queries indicative of post-enumeration analysis.

## Objectives

1. Retrieve a list of all previous Amass enumeration scans stored in the database for review.
2. Display detailed assets (subdomains, IPs, ASNs) from a specific scan to analyze the discovered attack surface.
3. Validate and export reconnaissance data for integration into broader security assessments or reporting.

## Instructions

### Step 1: List Previous Scans

**Context**: This step queries the Amass database to enumerate all prior enumeration sessions, providing timestamps, durations, and associated domains. It helps identify which scan to review next, ensuring you select the correct enumeration ID for asset retrieval. This is essential for managing multiple reconnaissance runs on the same target without confusion.

**Command** ([[commands/amass-db-list-previous-scans]]):
```bash
amass db -dir $_OUTPUT_DIRECTORY -list
```

> This command scans the specified directory for database files and outputs a numbered list of scans. Each entry includes start and end times (in local timezone), duration, and the domains or reverse zones involved. If no scans exist, it will return an empty list. Review the output to note the enumeration number (e.g., '1)', '2)') for the desired scan. Common issues include incorrect directory paths leading to 'no database found' errors—verify the path contains .db files.

### Step 2: Display Assets from Specific Scan

**Context**: After identifying the scan number from Step 1, this step retrieves and displays the assets discovered in that enumeration, including subdomains, associated IPs, and ASN details. It provides a summary of findings like name sources (e.g., certificates, APIs) and network mappings, aiding in prioritizing targets for further exploitation or scanning. This step confirms the completeness of prior recon and supports decision points, such as exporting results if the asset count meets thresholds.

**Command** ([[commands/amass-db-display-assets-from-scan]]):
```bash
amass db -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -enum $_SCAN_NUMBER -show
```

> Execute this after Step 1, substituting $_SCAN_NUMBER with the ID from the list (e.g., 2 for the second scan). The command filters by domain and enum ID, outputting a list of discovered names followed by a summary of sources and network details (e.g., ASNs with IP ranges and subdomain counts). Success is indicated by a populated list of assets; if empty, check the enum ID or domain match. For large outputs, pipe to a file (e.g., `| tee assets.txt`) for analysis. If the scan included reverse DNS, additional IP-derived names may appear.
