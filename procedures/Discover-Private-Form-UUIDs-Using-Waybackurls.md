---
id: proc-discover-uuids-waybackurls
tags:
  - reconnaissance
  - uuid
  - web-archive
type: procedure
tools:
  - '[[tools/waybackurls]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:30:47.011Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-Private-Form-UUIDs-Using-Waybackurls

## Summary

This procedure uses the waybackurls tool to perform reconnaissance on historical web archives, extracting UUIDs from previously public embedded submission form URLs that are now private or inactive, enabling subsequent IDOR exploitation.

## Description

In the context of targeting platforms like HackerOne, this reconnaissance step leverages archived web data to uncover identifiers (UUIDs) for resources that were once publicly accessible but have since been restricted. By querying the Wayback Machine, attackers can identify these UUIDs without direct access to the current site structure. This is particularly effective against systems using UUIDs for object references without robust access validation. Prerequisites include internet access and the waybackurls tool installed. Expected outcomes include a list of UUIDs ready for exploitation queries.

## Requirements

1. Installed waybackurls tool (Go-based, requires Go 1.16+)
2. Public internet access to query archive.org
3. Basic knowledge of regex for filtering UUID patterns
4. Target domain known (e.g., hackerone.com)

## Defense

Defensive measures and detection strategies:

- Implement URL archiving controls or robots.txt to limit historical exposure
- Monitor for unusual archive queries or tool usage in logs
- Use predictable ID schemes with server-side access checks beyond UUID validation

## Objectives

1. Gather historical URLs containing UUIDs for private resources
2. Extract and validate UUIDs for use in direct object references
3. Enable unauthorized access to restricted program data

## Instructions

### Step 1: Fetch Historical URLs

**Context**: Query the Wayback Machine for all archived URLs from the target domain to build a dataset of past exposures.

**Command** ([[waybackurls-fetch]]):
```bash
echo "https://hackerone.com" | waybackurls > historical_urls.txt
```

> This command pipes the target domain to waybackurls, which retrieves and outputs all unique URLs archived by the Wayback Machine. Expected output is a text file with thousands of URLs; review for paths like /embed/form/uuid.

### Step 2: Extract UUIDs

**Context**: Filter the URLs to isolate UUID patterns, focusing on those associated with embedded forms.

**Command** ([[grep-uuid-extract]]):
```bash
grep -E '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}' historical_urls.txt | cut -d'/' -f5 | sort -u > uuids.txt
```

> This greps for standard UUID format, extracts the UUID segment (assuming it's in the path), and deduplicates. Expected output: A file uuids.txt with candidate UUIDs for private forms.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/waybackurls]]

## Tags

- [[Reconnaissance]]
- [[web-archive]]
