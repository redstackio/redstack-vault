---
tags:
  - subdomain-takeover
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:38:39.384Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 30cc12d3-385e-4e1e-b2cd-02438297232e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Access-and-Observe-Subdomain-Response

## Summary

This procedure involves accessing a target subdomain via a web browser to check for active hosting, typically resulting in a 404 error that indicates potential DNS misconfigurations like dangling records.

## Description

In subdomain takeover attacks, the first step is to probe the subdomain for responsiveness. Navigating to the URL in a browser reveals if it's actively served or returns an error, signaling it might be abandoned but still resolvable via DNS. This is crucial for identifying takeover opportunities on third-party services like SendGrid. Prerequisites include public internet access; no special tools are needed beyond a standard browser.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Internet connectivity to resolve and access the subdomain
3. Target subdomain URL (e.g., email.smule.com)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like DNS linters
- Implement monitoring for 404 errors on subdomains with alerts for potential takeovers
- Use certificate transparency logs to detect unauthorized subdomain claims

## Objectives

1. Confirm subdomain inactivity
2. Identify signs of misconfiguration for further investigation
3. Set stage for DNS enumeration

## Instructions

### Step 1: Navigate to Subdomain

**Context**: Load the subdomain in a browser to observe the HTTP response.

No command required; use browser URL bar:

Enter `http://email.smule.com` or `https://email.smule.com`.

> This should return a 404 Not Found page from the browser or a default error, indicating no active hosting.

### Step 2: Document Response

**Context**: Note the error details for correlation with DNS checks.

Screenshot or log the 404 response headers and body.

> Expected: HTTP 404 status, no custom content from the target organization.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[recon]]
- [[web]]
