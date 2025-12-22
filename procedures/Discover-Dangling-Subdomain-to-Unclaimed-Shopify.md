---
tags:
  - subdomain-takeover
  - dns
  - shopify
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - DNS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9ea48ab9-ae47-4d05-b726-54c8f7ca3d79
created_at: '2025-12-14T04:51:10.901Z'
updated_at: '2025-12-14T04:51:10.901Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Dangling Subdomain to Unclaimed Shopify

## Summary

This procedure identifies subdomains misconfigured with CNAME records pointing to unclaimed resources on platforms like Shopify, enabling potential takeover by revealing abandoned integrations.

## Description

In this reconnaissance step, attackers scan or manually check target subdomains for dangling DNS records. Accessing the URL reveals if it redirects to a default unclaimed page on a third-party service, indicating the resource is no longer maintained by the original owner. For Shopify, this appears as a generic store setup page. This sets the stage for claiming the subdomain and highlights risks from decommissioned services without proper DNS cleanup.

## Requirements

1. Public access to the target's DNS records
2. Web browser for URL access
3. Basic knowledge of DNS resolution and third-party services

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like DNS enumeration scanners
- Implement monitoring for unclaimed subdomains on third-party platforms via API checks
- Use domain shadowing prevention by revoking or null-routing unused records

## Objectives

1. Confirm the presence of a vulnerable dangling subdomain
2. Verify it points to an unclaimed Shopify store
3. Gather evidence for further exploitation steps

## Instructions

### Step 1: Access Suspected Subdomain

**Context**: Directly visit the subdomain to check its resolution and content.

Navigate to the URL, such as https://de-headless.staging.gymshark.com/, in a web browser.

> The page should load a default Shopify unclaimed store template, confirming the vulnerability.

### Step 2: Verify Unclaimed Status

**Context**: Inspect the page for indicators of abandonment.

Look for Shopify's standard messaging about setting up a new store or claiming the domain, with no custom branding from the target.

> Successful verification shows no active store content, only Shopify defaults.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[shopify]]
