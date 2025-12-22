---
id: proc-visit-inspect-subdomain-takeover
tags:
  - subdomain-takeover
  - dns
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T05:32:23.033Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Visit-and-Inspect-Subdomain-for-Takeover

## Summary

This procedure involves accessing a suspected vulnerable subdomain to inspect its content for signs of takeover availability, such as unclaimed service messages, enabling early detection of dangling DNS records.

## Description

In scenarios where a subdomain like support.urbandictionary.com has a dangling DNS record pointing to a decommissioned third-party service (e.g., Zendesk), visiting the URL reveals an unconfigured page. This allows attackers to identify takeover opportunities without specialized tools, leading to potential impersonation or malicious hosting. The procedure targets public-facing web subdomains and requires only browser access, with outcomes including confirmation of vulnerability for further exploitation.

## Requirements

1. Public internet access to resolve and visit the subdomain
2. A standard web browser
3. Basic understanding of DNS and subdomain services

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using tools like DNS enumeration scanners
- Implement subdomain monitoring services to alert on unclaimed third-party pointers
- Remove or null-route unused DNS records post-decommissioning

## Objectives

1. Confirm the subdomain loads content from an unclaimed service
2. Identify the specific service provider (e.g., Zendesk) for takeover
3. Gather evidence for reporting or exploitation

## Instructions

### Step 1: Navigate to the Subdomain

**Context**: Use a browser to directly access the target subdomain and observe the raw page response.

No specific command required; manually enter the URL in the browser address bar: http://support.urbandictionary.com/

> The page should display a default message indicating no configuration, such as 'No help desk at support.urbandictionary.com', along with a signup link to the service provider.

### Step 2: Document Page Content

**Context**: Capture screenshots or notes on the page elements to verify the unclaimed status.

Inspect the HTML source for service-specific indicators (e.g., Zendesk branding or scripts).

> Expected output includes text prompts for claiming the address and links to signup pages like http://www.zendesk.com/signup/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[recon]]
