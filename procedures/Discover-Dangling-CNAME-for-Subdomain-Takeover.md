---
id: proc-discover-dangling-cname
tags:
  - subdomain-takeover
  - dns-recon
type: procedure
tools:
  - '[[tools/nslookup]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nslookup-dns-query-for-subdomain]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:38:39.654Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover Dangling CNAME for Subdomain Takeover

## Summary

This procedure identifies subdomains with dangling DNS CNAME records pointing to unclaimed cloud services like AWS Cloudfront, enabling potential takeover attacks.

## Description

In the Ubiquiti attack, a DNS lookup on ping.ubnt.com revealed a CNAME chain to an unregistered Cloudfront distribution, creating an opportunity for takeover. This reconnaissance step is crucial for mapping attack surfaces in cloud-integrated environments, where forgotten DNS pointers can lead to full subdomain control.

## Requirements

1. Access to public DNS resolvers (e.g., Google's 8.8.8.8)
2. Target subdomain name (e.g., ping.ubnt.com)
3. Basic networking knowledge for interpreting DNS responses

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or cloud provider consoles
- Implement DNS monitoring for unclaimed resolutions and automate alerts for error pages on subdomains

## Objectives

1. Uncover misconfigured DNS pointers to cloud services
2. Confirm the hostname is unclaimed by observing resolution errors
3. Gather evidence for potential subdomain takeover

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the target's DNS to reveal CNAME chains and identify cloud service pointers.

**Command** ([[commands/nslookup-dns-query-for-subdomain]]):
```bash
nslookup ping.ubnt.com 8.8.8.8
```

> This command resolves the hostname using Google's DNS, showing the CNAME to dl.ubnt.com and then to d2cnv2pop2xy4v.cloudfront.net. Expected output includes non-authoritative answers with the chain and an IP like 54.192.96.244; an error on direct access confirms dangling status.

### Step 2: Validate Unclaimed Status

**Context**: Access the resolved endpoint to check for cloud provider error pages indicating no registered hostname.

**Instructions**: Use a browser or curl to visit the subdomain; look for Cloudfront's default error indicating the hostname is not configured.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/nslookup-dns-query-for-subdomain]]

## Tools Used

- [[tools/nslookup]]

## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
