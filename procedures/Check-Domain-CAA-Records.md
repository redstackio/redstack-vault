---
id: proc-uuid-001
name: Check-Domain-CAA-Records
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:36.538Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Domain Properties]]'
sub_techniques: []
tags:
  - dns
  - caa
  - reconnaissance
  - misconfiguration
platforms:
  - DNS
  - Web
tools:
  - '[[tools/caatest-co-uk]]'
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Domain Properties]]'
---

# Check-Domain-CAA-Records

## Summary

This procedure involves querying DNS records for Certificate Authority Authorization (CAA) entries on a target domain to detect misconfigurations that allow any compliant Certificate Authority to issue certificates, increasing risks of unauthorized issuance, phishing, or man-in-the-middle attacks.

## Description

CAA records (DNS type 257) specify which Certificate Authorities are permitted to issue certificates for a domain. Their absence leaves the domain vulnerable to misissuance by unauthorized CAs, potentially enabling attackers to obtain valid-looking certificates for phishing sites or MITM intercepts. This procedure uses an online DNS lookup service to perform the check, simulating reconnaissance in a security assessment. Prerequisites include internet access and the target domain name. Expected outcomes include confirmation of missing records, highlighting the need for remediation.

## Requirements

1. Internet access for DNS queries
2. Target domain name (e.g., sifchain.finance)
3. Web browser to access the CAA testing service

## Defense

Defensive measures and detection strategies:

- Configure CAA records in DNS to whitelist authorized CAs (e.g., issue="letsencrypt.org;account=12345")
- Monitor DNS changes and certificate transparency logs for unauthorized issuances
- Use tools like DNSSEC to enhance DNS integrity

## Objectives

1. Identify absence of CAA records to assess certificate issuance risks
2. Document the misconfiguration for reporting
3. Recommend remediation to prevent potential domain takeover or MITM

## Instructions

### Step 1: Access CAA Testing Service

**Context**: Navigate to a reliable online tool for querying CAA records to avoid local DNS tool setup.

Use [[tools/caatest-co-uk]] by visiting https://caatest.co.uk/.

> Enter the domain in the search field and submit the query.

### Step 2: Query and Analyze Results

**Context**: Perform the DNS lookup for type 257 records and review for presence or absence.

Submit the domain (e.g., sifchain.finance) and inspect the output for CAA entries.

> If no records are found, the output will indicate "No CAA records" or similar, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Domain Properties]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/caatest-co-uk]]

## Tags

- [[DNS]]
- [[caa]]
- [[Reconnaissance]]
- [[misconfiguration]]
