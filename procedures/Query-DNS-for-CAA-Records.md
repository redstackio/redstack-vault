---
id: proc-uuid-123
tags:
  - dns
  - caa
  - reconnaissance
  - configuration
type: procedure
tools:
  - '[[tools/Google-DNS-Lookup]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:29:28.167Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Query-DNS-for-CAA-Records

## Summary

This procedure involves querying DNS for Certificate Authority Authorization (CAA) records (resource record type 257) on target domains to detect the absence of restrictions on which certificate authorities can issue certificates, exposing a configuration weakness that heightens the risk of misissuance of fraudulent certificates.

## Description

In this reconnaissance technique, an attacker uses public DNS lookup services to probe for CAA records on domains like hacker101.com and ctf.hacker101.com. CAA records specify which CAs are authorized to issue certificates for a domain, preventing unauthorized issuances. The absence of these records allows any CA to potentially issue certificates, enabling attacks such as phishing or impersonation by tricking CAs into signing phony certificates. This procedure requires no special access and can be performed from any internet-connected device, targeting public DNS infrastructure.

## Requirements

1. Internet access to a DNS query service like Google DNS
2. Target domain names (e.g., hacker101.com)
3. Basic understanding of DNS record types

## Defense

Defensive measures and detection strategies:

- Implement CAA records in DNS to explicitly list authorized CAs (e.g., issue="letsencrypt.org;account=12345")
- Monitor DNS queries for type 257 from unusual sources using tools like DNS logging in BIND or Cloudflare
- Regularly audit DNS configurations with automated scanners like dnsrecon or Zonemaster

## Objectives

1. Confirm presence or absence of CAA records to assess certificate issuance risks
2. Identify domains vulnerable to unauthorized certificate misissuance
3. Gather intelligence for potential follow-on attacks like phishing

## Instructions

### Step 1: Access DNS Lookup Tool

**Context**: Navigate to a reliable public DNS query interface to perform the lookup without local tools.

Use [[tools/Google-DNS-Lookup]] by visiting https://dns.google.com/query.

No command execution; this is a web-based interaction.

> Enter the domain and record type in the web form.

### Step 2: Query for CAA Records on Primary Domain

**Context**: Perform the DNS query for type 257 on the main target domain to check for authorization rules.

Configure the tool with: name=hacker101.com, type=257, dnssec=true.

Submit the query.

> The response will show authoritative answers; look for empty or no CAA section, indicating no restrictions.

### Step 3: Query for CAA Records on Subdomain

**Context**: Repeat the process for subdomains to ensure comprehensive coverage.

Configure the tool with: name=ctf.hacker101.com, type=257, dnssec=true.

Submit the query.

> Similar to Step 2, absence of records confirms the vulnerability across the domain tree.

### Step 4: Analyze Results

**Context**: Interpret the query outputs to validate the configuration issue.

Review the DNS responses for any CAA records (e.g., issue="ca.example.com").

If none are present, document the finding as a misconfiguration.

> Expected: "No CAA records found," increasing risk of unauthorized certificate issuance.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-DNS-Lookup]]

## Tags

- [[DNS]]
- [[caa]]
- [[Reconnaissance]]
- [[configuration]]
