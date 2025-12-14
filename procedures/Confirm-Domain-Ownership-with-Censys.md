---
tags:
  - ownership-verification
  - certificates
  - recon
type: procedure
tools:
  - '[[tools/Censys]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.737Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: fb2f2d81-9e48-4bef-9343-e6def8eda300
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Confirm Domain Ownership with Censys

## Summary

This procedure uses certificate search tools to verify that a dangling subdomain belongs to the intended target organization, ensuring the takeover targets the correct entity.

## Description

For subdomains like fastly.sc-cdn.net, attackers query public certificate databases to link the domain to Snapchat via SSL/TLS certificate details. This step prevents wasting effort on unrelated domains and provides evidence for reporting or exploitation justification. It leverages passive reconnaissance to avoid direct interaction with the target.

## Requirements

1. Access to a certificate search platform like Censys.
2. The subdomain name to query.
3. Basic understanding of certificate fields (e.g., subject, issuer).

## Defense

Defensive measures and detection strategies:

- Monitor certificate transparency logs for unexpected subdomain certificates.
- Rotate certificates regularly to limit exposure.
- Use private CAs for internal subdomains.

## Objectives

1. Link the subdomain to Snapchat ownership.
2. Gather supporting evidence from certificate metadata.
3. Confirm no ownership disputes.

## Instructions

### Step 1: Search Certificates

**Context**: Query Censys for certificates associated with the subdomain.

**Command** (Web Query):
Use the Censys search interface at https://censys.io/certificates?q=fastly.sc-cdn.net

> Expected output: Certificates showing Snapchat as the organization, e.g., via Common Name or Subject Alternative Names.

### Step 2: Analyze Results

**Context**: Review certificate details for ownership confirmation.

No command; manually inspect results.

> Look for links like https://censys.io/certificates/65ba2e172a1eb85eb1071c9fd7a4e8371ef12625409890507c89a54978305558 confirming Snapchat ties.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Censys]]

## Tags

- [[ownership-verification]]
- [[certificates]]
- [[recon]]
