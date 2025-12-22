---
tags:
  - dns-recon
  - subdomain-enum
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:39.989Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b691080e-d237-4b38-ba9c-1ea00311f556
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Perform-DNS-Lookup-to-Identify-Dangling-Record

## Summary

This procedure uses DNS queries to detect subdomains with dangling records pointing to cloud services like AWS S3, revealing potential takeover vulnerabilities by checking for non-responsive endpoints.

## Description

In cloud environments, deleting a resource like an S3 bucket without updating DNS can leave a 'dangling' record. This procedure queries DNS for a target subdomain to see if it resolves to cloud provider endpoints (e.g., S3 CNAMEs) that return errors, indicating the resource is gone and claimable. It's a key reconnaissance step for subdomain takeover attacks, applicable to AWS, Azure, or GCP misconfigurations. Prerequisites include public DNS access; outcomes include identification of exploitable records leading to arbitrary content serving.

## Requirements

1. Access to a DNS resolution tool like dig
2. Target subdomain name (e.g., images.crossinstall.com)
3. Internet connectivity for queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records against active cloud resources using automated scripts
- Implement DNS monitoring for anomalous resolutions (e.g., S3 errors)
- Use subdomain management tools to flag dangling pointers

## Objectives

1. Detect resolution to non-existent cloud endpoints
2. Confirm potential for resource takeover
3. Gather evidence for vulnerability reporting

## Instructions

### Step 1: Query DNS Records

**Context**: Resolve the subdomain to check for cloud-specific CNAMEs or IPs indicating a dangling record.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig images.crossinstall.com +short
```

> This command performs a quick DNS lookup, outputting only the resolved records. Expected output includes S3 endpoints like assets.crossinstall.com.s3.amazonaws.com. and IPs (e.g., 52.217.103.180) if dangling; follow up by accessing the endpoint to confirm 403/no bucket errors.

### Step 2: Validate Resolution

**Context**: Manually verify if the resolved endpoint serves content or errors, confirming the dangling state.

**Command** (Manual browser or curl check):
```bash
curl -I https://images.crossinstall.com
```

> Look for S3 'NoSuchBucket' errors in the response, indicating takeover opportunity.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[dns-recon]]
- [[subdomain-takeover]]
