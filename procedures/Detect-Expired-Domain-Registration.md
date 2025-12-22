---
id: proc-detect-expired-domain
tags:
  - domain-takeover
  - reconnaissance
  - whois
type: procedure
tools:
  - '[[tools/whois]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-url]]'
  - '[[commands/whois-query]]'
verified: false
platforms:
  - Web
  - Domain
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:26.358Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Detect Expired Domain Registration

## Summary

This procedure identifies expired domain registrations by observing site behavior changes and querying WHOIS data, enabling early detection of takeover risks in reconnaissance phases.

## Description

In scenarios where a domain like 'doesfranshaveashell.com' expires without renewal (e.g., on 2019-09-02), it enters a grace period and may be taken over by parking services. Attackers can exploit this for impersonation. This procedure uses web access and WHOIS queries to confirm expiration, focusing on status like 'clientTransferProhibited' and unexpected parking ads. Prerequisites include internet access; no credentials are needed.

## Requirements

1. Web browser or curl for HTTP requests
2. WHOIS tool or access to whois.com
3. Target domain name

## Defense

Defensive measures and detection strategies:

- Enable auto-renewal on domain registrars
- Monitor domain status via automated WHOIS alerts
- Use domain monitoring services like DomainTools

## Objectives

1. Confirm domain expiration to assess takeover risk
2. Gather evidence of parking service control
3. Identify potential for phishing or typosquatting

## Instructions

### Step 1: Access Domain Homepage

**Context**: Check for signs of expiration by loading the site and noting deviations from expected content.

**Command** ([[commands/curl-access-url]]):
```bash
curl -s http://doesfranshaveashell.com/ | head -n 20
```

> This fetches the first 20 lines of the homepage. Expect ad-laden HTML from a parking service if expired.

### Step 2: Perform WHOIS Query

**Context**: Retrieve registration details to verify expiration date and status.

**Command** ([[commands/whois-query]]):
```bash
whois doesfranshaveashell.com | grep -E 'Expiration|Status'
```

> Output includes expiration (2019-09-02) and status (clientTransferProhibited), confirming vulnerability post-grace period.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-access-url]]
- [[commands/whois-query]]

## Tools Used

- [[tools/whois]]

## Tags

- [[domain-takeover]]
- [[Reconnaissance]]
