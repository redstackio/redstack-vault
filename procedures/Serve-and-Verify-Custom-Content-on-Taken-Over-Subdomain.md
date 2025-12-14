---
id: proc-serve-verify-subdomain
name: Serve and Verify Custom Content on Taken Over Subdomain
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.591Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - verification
  - malicious-content
commands:
  - '[[commands/curl-fetch-subdomain]]'
platforms:
  - AWS
  - Web
tools:
  - '[[tools/curl]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Serve and Verify Custom Content on Taken Over Subdomain

## Summary

This procedure configures a web server on the claimed EC2 instance to serve arbitrary content under the subdomain and verifies control via HTTP requests.

## Description

After claiming the IP, set up a server to host phishing pages or payloads. Verification confirms the takeover by fetching the custom content. This can lead to TLS cert acquisition via Let's Encrypt or exploitation of domain trusts.

## Requirements

1. Control of the EC2 instance on the subdomain's IP
2. Web server software installed (e.g., Apache)
3. Network access to query the subdomain

## Defense

Defensive measures and detection strategies:

- Monitor subdomain traffic for anomalies using AWS WAF or CloudTrail
- Implement certificate transparency monitoring
- Regularly test subdomains for takeover vulnerability with tools like Subjack

## Objectives

1. Serve custom or malicious content on the subdomain
2. Verify attacker control
3. Enable phishing or payload delivery

## Instructions

### Step 1: Configure Web Server

**Context**: Update the server's default page with proof-of-concept content.

**Command** (On EC2 instance):
```bash
echo "<!-- hackerone.com/ian -->" | sudo tee /var/www/html/index.html
```

> This adds a comment to the HTML. Restart the server if needed: sudo systemctl restart apache2.

### Step 2: Verify Control

**Context**: Fetch the content from an external machine to confirm the subdomain resolves and serves the custom page.

**Command** ([[commands/curl-fetch-subdomain]]):
```bash
curl fr1.vpn.zomans.com
```

> Expected output: The HTML content including the hackerone comment, indicating successful takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-subdomain]]

## Tools Used

- [[tools/curl]]

## Tags

- [[subdomain-takeover]]
- [[verification]]
