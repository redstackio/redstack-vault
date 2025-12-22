---
tags:
  - phishing
  - malware
  - xss
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8e1ad825-28df-4cc6-9c31-711b0cf0ab46
created_at: '2025-12-14T04:51:26.612Z'
updated_at: '2025-12-14T04:51:26.612Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Serve-Arbitrary-Content-on-Taken-Over-Subdomains

## Summary

This procedure hosts custom content on hijacked subdomains to intercept legitimate traffic, enabling attacks like phishing, malware distribution, XSS, or authentication bypass.

## Description

After claiming Azure endpoints, configure them to serve arbitrary web content on subdomains like svcgatewayloadus.starbucks.com. In the PoC, this resulted in 1603 requests from 29 unique IPs over 45 minutes, demonstrating real traffic diversion. The target environment is web-facing cloud services, with outcomes including user deception on trusted domains.

## Requirements

1. Control over claimed Azure Traffic Manager endpoints
2. A web server (e.g., Apache, Nginx) to host content
3. HTTPS setup if emulating trusted services

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning or HSTS on subdomains
- Monitor web traffic anomalies and unexpected content
- Use subdomain isolation and regular security scans

## Objectives

1. Divert and serve malicious content to users
2. Collect traffic data for further attacks
3. Exploit trust in the subdomain for phishing or injection

## Instructions

### Step 1: Set Up Web Server

**Context**: Prepare hosting for arbitrary content.

**Instructions**: Deploy a simple web server on a VM or use services like GitHub Pages, configuring it to serve HTML with phishing forms or JavaScript for XSS.

### Step 2: Route Traffic in Azure

**Context**: Link the Traffic Manager to your server.

**Instructions**: In the Azure portal, edit the claimed profile's endpoints to point to your server's IP/hostname. Ensure HTTP/HTTPS listeners are active.

### Step 3: Test and Monitor

**Context**: Verify serving and observe traffic.

**Instructions**: Access http://svcgatewayloadus.starbucks.com/ in a browser to confirm custom content loads. Use server logs to track requests from unique IPs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[Malware]]
- [[xss]]
- [[subdomain-takeover]]
