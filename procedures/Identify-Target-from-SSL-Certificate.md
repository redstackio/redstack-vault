---
tags:
  - reconnaissance
  - ssl-certificate
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 9a4d8d83-1d00-4ad2-a31c-67f181b6a9d2
created_at: '2025-12-14T03:16:37.270Z'
updated_at: '2025-12-14T03:16:37.270Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Target-from-SSL-Certificate

## Summary

This procedure involves reviewing SSL certificate details, such as during renewal processes, to identify target domains like http://nodebb.ubnt.com/ that may be protected by .htaccess on port 80, setting the stage for further discovery of bypasses.

## Description

In offensive security testing, attackers often start with passive reconnaissance by examining public SSL certificate transparency logs or renewal notifications. This reveals hidden subdomains or services, such as a NodeBB forum instance. In this case, the certificate mentioned http://nodebb.ubnt.com/, which was noted to use .htaccess password protection on the standard HTTP port, prompting deeper scanning for unprotected access points. Expected outcomes include target IP resolution (e.g., 104.131.159.88) and awareness of initial security measures.

## Requirements

1. Access to public SSL certificate transparency tools or logs (e.g., crt.sh)
2. Basic knowledge of domain resolution and port protections
3. Network access to query certificate details

## Defense

Defensive measures and detection strategies:

- Monitor certificate issuance and avoid exposing internal services in public certs
- Use certificate pinning to limit exposure
- Log and alert on unusual certificate queries

## Objectives

1. Discover target domains from certificate metadata
2. Note protection mechanisms like .htaccess
3. Resolve target IP for subsequent scanning

## Instructions

### Step 1: Review Certificate Details

**Context**: Examine SSL renewal or transparency logs for target mentions.

Search for the domain in certificate logs to confirm http://nodebb.ubnt.com/ and resolve its IP to 104.131.159.88. Note the .htaccess protection on port 80.

### Step 2: Document Findings

**Context**: Record the target for scanning.

Document the domain, IP, and protection notes to prepare for port enumeration.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[ssl-certificate]]
