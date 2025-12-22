---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - dns-recon
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.444Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify DNS Configuration for Subdomain Takeover

## Summary

This procedure involves querying DNS records to identify misconfigurations, such as ANAME or CNAME records pointing to unclaimed third-party services, enabling subdomain takeover attacks.

## Description

In the context of subdomain takeovers, attackers scan DNS records for dangling pointers to expired or unclaimed resources on platforms like Tumblr, AWS, or GitHub Pages. For blog.snapchat.com, the ANAME record redirects to snapchat-blog.com, which uses a Tumblr CNAME. This step uncovers such chains, setting the stage for claiming control and hosting malicious content like phishing pages on what appears to be an official subdomain.

## Requirements

1. Access to DNS resolution tools (e.g., dig, nslookup, or online DNS checkers)
2. Knowledge of the target domain (e.g., blog.snapchat.com)
3. Internet connectivity for queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAME/ANAME entries using automated tools like dnsdumpster or subjack
- Monitor third-party service claims and set up alerts for expirations
- Implement DNSSEC to prevent unauthorized resolutions

## Objectives

1. Discover DNS misconfigurations leading to takeover opportunities
2. Map the chain from subdomain to external service
3. Identify vulnerable third-party integrations

## Instructions

### Step 1: Query ANAME Record

**Context**: Use a DNS tool to retrieve the ANAME record for the target subdomain, revealing the external domain it points to.

For blog.snapchat.com, execute a DNS lookup:

(Use an online tool or command-line: dig ANAME blog.snapchat.com)

> This reveals the ANAME points to snapchat-blog.com.

### Step 2: Trace CNAME Chain

**Context**: Follow the CNAME from the external domain to identify the third-party service.

Query the CNAME for snapchat-blog.com:

(Use dig CNAME snapchat-blog.com)

> Confirms it points to Tumblr's infrastructure, indicating a potential custom domain setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dns-recon]]
- [[subdomain-takeover]]
