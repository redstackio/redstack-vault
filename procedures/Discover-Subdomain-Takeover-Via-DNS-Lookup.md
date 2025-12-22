---
id: proc-discover-subdomain-takeover-dns
tags:
  - subdomain-takeover
  - dns-recon
type: procedure
tools:
  - '[[tools/nslookup]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/nslookup-dns-query-for-cname]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:39:01.859Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover Subdomain Takeover Via DNS Lookup

## Summary

This procedure uses DNS queries to identify subdomains with dangling CNAME records pointing to unclaimed cloud services, such as AWS CloudFront, enabling potential takeover for malicious content serving.

## Description

In the Uber attack, a DNS lookup on saostatic.uber.com revealed a CNAME to an unclaimed CloudFront distribution (d3i4yxtzktqr9n.cloudfront.net). Visiting the subdomain confirmed the error page, indicating takeover susceptibility. This reconnaissance step is crucial for identifying forgotten DNS configurations in large organizations.

## Requirements

1. Access to a DNS resolver like Google DNS (8.8.8.8)
2. Target subdomain name (e.g., saostatic.uber.com)
3. Browser for verifying unclaimed status

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMES using tools like dnsdumpster or subjack
- Implement DNS monitoring for unclaimed cloud hostnames
- Use CAA records to restrict certificate issuance on subdomains

## Objectives

1. Identify vulnerable subdomains for takeover
2. Confirm unclaimed status of cloud resources
3. Gather evidence for further exploitation

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the target subdomain to resolve its CNAME record and check for cloud service pointers.

**Command** ([[commands/nslookup-dns-query-for-cname]]):
```bash
nslookup saostatic.uber.com 8.8.8.8
```

> This command queries Google DNS for the subdomain's records. Expected output includes the canonical name (CNAME) to a cloud resource like d3i4yxtzktqr9n.cloudfront.net.

### Step 2: Verify Unclaimed Status

**Context**: Access the subdomain in a browser to confirm it's not configured, showing a cloud provider error.

**Instructions**: Navigate to http://saostatic.uber.com. Look for an error page stating the hostname is not configured for the distribution.

> No command needed; manual browser verification. Success if error indicates claimable resource.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/nslookup-dns-query-for-cname]]

## Tools Used

- [[tools/nslookup]]

## Tags

- subdomain-takeover
- dns-recon
