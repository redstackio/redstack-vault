---
tags:
  - subdomain-takeover
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:49.537Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 8b5897e6-c323-4f32-982d-db4a87ab0c06
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Detect-Unclaimed-Subdomain

## Summary

This procedure detects if a target subdomain is unclaimed by accessing it and observing service-specific error messages indicating misconfiguration, such as non-activated hubs in third-party content services.

## Description

In subdomain takeover attacks, attackers first probe target subdomains to identify those pointed to external services (e.g., Uberflip) but not properly configured in any account. Accessing the URL reveals errors like 'Non-hub domain' for Uberflip, signaling availability for claiming. This step is reconnaissance-focused and requires no special access, targeting web platforms with DNS-resolved subdomains. Expected outcome: Confirmation of potential takeover vector without alerting defenses.

## Requirements

1. Internet access to resolve and visit HTTPS URLs
2. Basic knowledge of HTTP responses and error messages
3. Optional: Command-line tools like curl for automated probing

## Defense

Defensive measures and detection strategies:

- Monitor DNS changes and subdomain registrations in services like Uberflip
- Implement certificate transparency monitoring for subdomains
- Use automated scanners (e.g., Subjack) to detect dangling DNS records

## Objectives

1. Identify misconfigured subdomains serving error pages from third-party services
2. Confirm the subdomain is not actively controlled by the owner
3. Gather evidence for further takeover validation

## Instructions

### Step 1: Access the Subdomain URL

**Context**: Probe the target subdomain to check for service-specific errors indicating an unclaimed configuration.

**Command** ([[commands/curl-access-url]]):
```bash
curl -i https://resources.hackerone.com/
```

> This command sends an HTTP HEAD request (or GET with -i for headers) and displays the response. Look for body text like 'Non-hub domain, The URL you've accessed does not provide a hub. Please check the URL and try again.' Success confirms the subdomain points to an inactive service endpoint.

### Step 2: Validate Response Manually

**Context**: If using a browser, visit the URL directly to inspect the error page for clues about the underlying service.

No command needed; manual inspection. Expected: Error page without legitimate content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-access-url]]

## Tools Used

- None

## Tags

- [[subdomain-takeover]]
- [[recon]]
