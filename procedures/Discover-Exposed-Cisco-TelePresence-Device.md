---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - recon
  - scanning
  - cisco
type: procedure
tools:
  - '[[tools/ipinfo-io]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Network Device
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:31:19.078Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-Exposed-Cisco-TelePresence-Device

## Summary

This procedure involves scanning IP ranges near known vulnerable devices to identify exposed Cisco TelePresence SX80 instances on the internet, verifying ownership via ASN details to target high-value assets like DoD communications equipment.

## Description

In scenarios where prior vulnerabilities are reported (e.g., report #684070), attackers expand reconnaissance by checking adjacent IP ranges for similar exposures. The SX80's web interface, if unprotected, reveals itself through accessible HTTPS endpoints. Ownership verification prevents false positives and focuses on relevant targets. This step sets up initial access without direct interaction, relying on public tools for passive and active scanning.

## Requirements

1. Access to internet-facing IP scanning tools
2. Knowledge of a seed IP from prior reports
3. No credentials needed; assumes public exposure

## Defense

Defensive measures and detection strategies:

- Implement network access controls (ACLs) to block unsolicited scans
- Use intrusion detection systems (IDS) to monitor for IP range probes
- Regularly audit exposed devices with tools like Shodan or internal scanners

## Objectives

1. Identify SX80 web interfaces at specific IPs
2. Confirm organizational ownership via ASN
3. Establish reconnaissance baseline for exploitation

## Instructions

### Step 1: Scan IP Range

**Context**: Start from a known vulnerable IP and expand to nearby addresses to locate the SX80.

No specific command; use browser or tools to probe https://[IP] for the login page.

> Probe adjacent IPs manually or with automated scanners; look for Cisco TelePresence indicators in responses.

### Step 2: Verify Ownership

**Context**: Use IP info services to tie the device to the target organization.

Access [[tools/ipinfo-io]] and query the IP:

Visit https://ipinfo.io/[IP] in a browser.

> Output includes ASN (e.g., AS257) and organization details confirming DoD linkage.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ipinfo-io]]

## Tags

- recon
- scanning
- cisco
