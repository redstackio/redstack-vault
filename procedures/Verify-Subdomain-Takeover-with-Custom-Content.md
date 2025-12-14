---
id: proc-verify-subdomain-takeover
tags:
  - subdomain-takeover
  - web
  - verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-fetch-subdomain-content]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.481Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Subdomain-Takeover-with-Custom-Content

## Summary

This procedure verifies successful subdomain takeover by serving custom content from the controlled infrastructure and fetching it via HTTP request, confirming attacker dominance over the domain.

## Description

After claiming the IP, the attacker configures a web server on the EC2 instance to serve arbitrary content. This procedure tests the setup by curling the subdomain, ensuring traffic routes to the attacker's server. Applicable to cloud environments like AWS; requires prior IP claim. Outcomes include proof-of-concept for further exploits like phishing or cert issuance.

## Requirements

1. Control over the EC2 instance with web server installed
2. DNS propagation (may take minutes)
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Monitor web traffic logs for unexpected content or sources
- Use certificate transparency monitoring to detect unauthorized TLS issuance on subdomains
- Implement DNSSEC to prevent easy takeovers

## Objectives

1. Confirm traffic redirection to attacker server
2. Validate ability to serve malicious payloads
3. Demonstrate impact on domain-trusting services

## Instructions

### Step 1: Serve Custom Content

**Context**: On the controlled EC2 instance, set up a simple web page with a unique marker to prove ownership.

**Command** (On instance):
```bash
echo "<!-- hackerone.com/ian --> <h1>Controlled Content</h1>" > /var/www/html/index.html
systemctl restart apache2  # or nginx
```

> Ensures the server responds with identifiable content.

### Step 2: Fetch and Verify Content

**Context**: From an external machine, request the subdomain to retrieve and inspect the served content.

**Command** ([[commands/curl-fetch-subdomain-content]]):
```bash
curl v.zego.com
```

> This sends a GET request and outputs the HTML. Expected output includes the marker "<!-- hackerone.com/ian -->", confirming takeover. If not, check DNS propagation with dig.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/curl-fetch-subdomain-content]]

## Tools Used

-

## Tags

- [[subdomain-takeover]]
- [[web]]
- [[verification]]
