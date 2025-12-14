---
id: proc-uuid-4
name: Analyze Exfiltrated Data and Trace Victim Location
tags:
  - ssrf
  - analysis
  - geolocation
  - exfil
type: procedure
tools:
  - '[[tools/ngrok]]'
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-ip-geolocation-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.266Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze Exfiltrated Data and Trace Victim Location

## Summary

This procedure examines the captured request in ngrok for victim details like IP, browser, and OS, then uses curl to query geolocation services for physical tracing based on the leaked IP.

## Description

Post-exploit, ngrok logs contain headers from the SSRF request, revealing victim connection info. Curl queries public IP services to map the IP to location data. This applies to web-based SSRF leaks. Prerequisites: Successful trigger and ngrok logs. Outcomes: Detailed victim profile including approximate location for further reconnaissance or targeting.

## Requirements

1. Ngrok dashboard with captured request data
2. Captured victim IP address from headers
3. Curl installed for geolocation queries

## Defense

Defensive measures and detection strategies:

- Anonymize internal requests with proxies or VPNs to mask real IPs
- Block access to IP geolocation APIs from internal networks
- Audit logs for exfiltrated PII and implement data loss prevention (DLP)

## Objectives

1. Extract and parse victim metadata from request headers
2. Perform IP-based geolocation to approximate physical location
3. Enable potential follow-on attacks like port scanning

## Instructions

### Step 1: Review Ngrok Logs

**Context**: Inspect the incoming request for key headers containing victim info.

**Command** (Monitoring):
```bash
# Access ngrok interface
open http://127.0.0.1:4040
```

> Note the request's remote IP (victim's), User-Agent (browser/OS, e.g., Firefox 80.0.1), and other headers like Referer.

### Step 2: Query Geolocation

**Context**: Use the captured IP to fetch location details via a public API.

**Command** ([[commands/curl-ip-geolocation-query]]):
```bash
curl ipinfo.io/IP-address-of-victim
```

> Replace IP-address-of-victim with the actual IP (e.g., curl ipinfo.io/192.0.2.1). Output includes JSON with city, region, country, and ISP.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-ip-geolocation-query]]

## Tools Used

- [[tools/ngrok]]
- [[tools/curl]]

## Tags

- ssrf
- analysis
- geolocation
- exfil
