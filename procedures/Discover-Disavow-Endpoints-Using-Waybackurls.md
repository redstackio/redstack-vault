---
tags:
  - reconnaissance
  - url-discovery
  - wayback-machine
type: procedure
tools:
  - '[[tools/waybackurls]]'
  - '[[tools/grep]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/waybackurls-grep-disavow]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:31:30.752Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c699ce96-2e6c-4b4a-8a5f-4656dc601d95
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-Disavow-Endpoints-Using-Waybackurls

## Summary

This procedure uses the Wayback Machine to retrieve archived URLs for a target domain and filters them for sensitive endpoints like 'disavow' paths, enabling discovery of unprotected access control vulnerabilities on web applications such as Liberapay.

## Description

In the context of Liberapay, this reconnaissance step identifies disavow endpoints that allow email disassociation without authentication. By querying the Internet Archive, attackers can uncover historical URLs that may still be active and vulnerable, bypassing direct scanning of the live site. Prerequisites include command-line access and internet connectivity; no target credentials are needed. Expected outcomes include a list of exploitable URLs leading to further account manipulation.

## Requirements

1. Command-line environment (Linux/macOS/Windows with bash)
2. Installed waybackurls and grep tools
3. Internet access to archive.org

## Defense

Defensive measures and detection strategies:

- Monitor for unusual queries to archival services in logs
- Implement rate limiting on endpoint access and require authentication for sensitive actions like email changes
- Regularly audit archived URLs and deprecate unused endpoints

## Objectives

1. Identify hidden or archived sensitive endpoints
2. Map potential vulnerability surfaces without direct interaction
3. Prepare for exploitation by confirming endpoint existence

## Instructions

### Step 1: Fetch Archived URLs

**Context**: Retrieve all known URLs for the target domain from the Wayback Machine to build a comprehensive list of potential endpoints.

**Command** ([[commands/waybackurls-grep-disavow]]):
```bash
waybackurls liberapay.com
```

> This command outputs a stream of URLs archived for liberapay.com. Expected output is a plain text list of URLs, one per line.

### Step 2: Filter for Sensitive Keywords

**Context**: Pipe the URL list to grep to isolate endpoints containing keywords indicative of sensitive operations, such as 'disavow'.

**Command** ([[commands/waybackurls-grep-disavow]]):
```bash
waybackurls liberapay.com | grep disavow
```

> This filters the output to show only URLs with 'disavow', revealing paths like /account/disavow/email/. Expected output is a refined list of matching URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/waybackurls-grep-disavow]]

## Tools Used

- [[tools/waybackurls]]
- [[tools/grep]]

## Tags

- reconnaissance
- url-discovery
- archived-endpoints
