---
id: proc-uuid-001
tags:
  - subdomain-takeover
  - dns
  - recon
type: procedure
tools:
  - '[[tools/AWS-CloudFront]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:49.168Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Detect Dangling CNAME Subdomain

## Summary

This procedure involves accessing a target subdomain to detect signs of a dangling CNAME record, such as error messages from unconfigured cloud services like AWS CloudFront, indicating potential for subdomain takeover.

## Description

In scenarios where organizations reconfigure DNS without cleaning up old records, subdomains may point to unused cloud resources. Accessing such a subdomain over HTTP/HTTPS reveals service-specific errors, like CloudFront's "no distribution configured" message. This is the initial reconnaissance step in identifying takeover opportunities, applicable to AWS environments where CNAMEs trail to CloudFront endpoints.

## Requirements

1. Public access to the target subdomain (e.g., rider.uber.com)
2. Web browser or HTTP client for probing
3. Basic knowledge of DNS and cloud services

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or AWS Route 53 logs
- Implement monitoring for unresolved subdomains and automate takedown of unused cloud resources
- Use certificate transparency logs to detect unauthorized claims on subdomains

## Objectives

1. Identify misconfigured subdomains pointing to cloud services
2. Gather evidence of vulnerability for further analysis
3. Establish initial access vector for takeover

## Instructions

### Step 1: Probe the Subdomain

**Context**: Visit the subdomain to trigger and observe the service error.

No specific command; use a browser to navigate to http://rider.uber.com and https://rider.uber.com.

> Observe the response: Expect an XML or HTML error from CloudFront stating "The specified CloudFront distribution does not exist" or similar, confirming no active distribution.

### Step 2: Document the Response

**Context**: Capture the error for analysis, including headers and body.

Use browser developer tools or curl to screenshot/log the page.

> This step confirms the subdomain is live but unserved, pointing to a takeover candidate.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-CloudFront]]

## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[recon]]
