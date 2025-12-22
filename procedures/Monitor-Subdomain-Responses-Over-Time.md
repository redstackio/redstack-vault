---
tags:
  - subdomain-takeover
  - dns
  - monitoring
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-probe-http]]'
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:23.956Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e675a56d-e30b-47cd-a7d2-961b28dffd1c
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Monitor-Subdomain-Responses-Over-Time

## Summary

This procedure involves periodically querying a target subdomain to record HTTP responses, headers, and port status over time, enabling detection of changes indicative of resource decommissioning and potential takeover vulnerabilities.

## Description

In scenarios like subdomain takeovers, attackers monitor DNS-resolved subdomains for shifts in behavior, such as a previously unresponsive port becoming active with foreign server signatures. This passive reconnaissance identifies dangling DNS records pointing to stopped resources like AWS EC2 instances that may be reassigned. The procedure requires no special access and relies on public DNS resolution, making it suitable for long-term surveillance in cloud environments.

## Requirements

1. Internet access for DNS queries and HTTP requests
2. Basic HTTP client (e.g., curl or browser)
3. Logging capability to track responses over multiple sessions (days or weeks)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using tools like dnsdumpster or internal scripts
- Implement DNS monitoring alerts for resolution changes
- Use certificate transparency logs to detect unauthorized subdomain usage

## Objectives

1. Detect transition from non-responsive to responsive state on target subdomain
2. Capture baseline and anomalous HTTP headers/bodies
3. Identify potential resource repurposing for takeover assessment

## Instructions

### Step 1: Initial Baseline Query

**Context**: Establish the initial state of the subdomain to compare against future queries.

**Command** ([[commands/curl-probe-http]]):
```bash
curl -i -m 10 https://mk.prd.vine.co/
```

> This command sends a HEAD-like request with a 10-second timeout to check port 443. Expected output initially: Connection timeout or no response, indicating closed port.

### Step 2: Periodic Monitoring

**Context**: Repeat queries at intervals (e.g., daily) and log changes in responses.

**Command** ([[commands/curl-probe-http]]):
```bash
curl -i -m 10 https://mk.prd.vine.co/ > response_$(date +%Y%m%d).log
```

> Log full responses including headers. Look for new Server headers like awselb/2.0, signaling repurposing.

### Step 3: Analyze Logs

**Context**: Review logs for anomalies, such as port opening and foreign server indicators.

**Command** (Manual review or grep):
```bash
grep -i "server:" *.log
```

> Expected output: Evolution from no response to HTTP/1.1 with AWS headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains and Subdomains

### Sub-Techniques


## Commands Used

- [[commands/curl-probe-http]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[recon]]
