---
tags:
  - subdomain-takeover
  - dns-enumeration
  - misconfiguration
type: procedure
tools:
  - '[[tools/Subfinder]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/subfinder-enumerate-subdomains]]'
  - '[[commands/dig-query-cname]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:31.131Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Software]]'
id: 39d1090a-cd60-43bd-82a9-8781975654a2
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Enumerate-and-Verify-Subdomain-Takeover
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Reconnaissance]], [[Initial Access]]
techniques: [[Gather Victim Host Information]], [[Exploit Public-Facing Application]]
sub_techniques: [[Software]]
tags: subdomain-takeover, dns-enumeration, misconfiguration
commands: [[commands/subfinder-enumerate-subdomains]], [[commands/dig-query-cname]]
platforms: Web
tools: [[tools/Subfinder]]
---

# Enumerate-and-Verify-Subdomain-Takeover

## Summary

This procedure outlines the process of enumerating subdomains of a target like OWOX, Inc., verifying DNS records for dangling pointers to unused third-party services, and assessing takeover potential, which can lead to subdomain hijacking and compromise of integrated services such as Google Workspace.

## Description

In the context of the OWOX vulnerability, attackers enumerate subdomains using passive and active techniques to uncover those with DNS records pointing to decommissioned services (e.g., Heroku, AWS). Verification involves checking if these services are claimable, allowing an attacker to host malicious content under the trusted domain. The outcome is potential phishing or unauthorized access to Google services like Gmail and Drive, enabling privilege escalation. Prerequisites include public DNS access and basic reconnaissance tools; no authentication is needed for discovery.

## Requirements

1. Internet access for DNS queries and subdomain enumeration
2. Installation of Subfinder and dig (standard on Linux/macOS)
3. Target domain knowledge (e.g., owow.com)

## Defense

Defensive measures and detection strategies:

- Regularly audit and clean up DNS records using automated tools like DNS monitoring services
- Implement domain shadowing detection and CNAME monitoring alerts
- Use certificate transparency logs to detect unauthorized subdomain claims

## Objectives

1. Identify vulnerable subdomains with dangling records
2. Verify takeover feasibility without full exploitation
3. Assess impact on linked cloud services like Google Workspace

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Perform comprehensive subdomain discovery to build a list of potential targets.

**Command** ([[commands/subfinder-enumerate-subdomains]]):
```bash
subfinder -d owow.com -all -o subdomains.txt
```

> This command uses multiple sources (passive DNS, search engines) to enumerate subdomains and saves them to a file. Expected output: A list of subdomains like "api.owow.com", "mail.owow.com".

### Step 2: Query DNS Records for Dangling Entries

**Context**: For each subdomain, check CNAME or other records to identify pointers to unused services.

**Command** ([[commands/dig-query-cname]]):
```bash
dig subdomain.owow.com CNAME +short
```

> This queries the CNAME record; replace "subdomain.owow.com" with actual subdomains from the list. Expected output: A response like "unused-service.herokuapp.com" if dangling.

### Step 3: Verify Takeover Potential

**Context**: Manually or with scripts, check if the pointed service (e.g., Heroku) is claimable by attempting registration or using takeover verification tools.

**Command** (Manual verification, no specific command):
```bash
# Example: Visit https://unused-service.herokuapp.com and check for claim page
curl -I https://unused-service.herokuapp.com
```

> Look for 404 or claim prompts. If claimable, assess Google Workspace linkage by testing subdomain access to services like calendar.owow.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[Software]] Software

## Commands Used

- [[commands/subfinder-enumerate-subdomains]]
- [[commands/dig-query-cname]]

## Tools Used

- [[tools/Subfinder]]

## Tags

- [[subdomain-takeover]]
- [[dns-enumeration]]
- [[misconfiguration]]
