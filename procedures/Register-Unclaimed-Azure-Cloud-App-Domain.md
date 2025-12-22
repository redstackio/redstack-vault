---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - azure-hijack
  - domain-registration
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/Azure-Portal]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Azure
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.796Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register Unclaimed Azure Cloud App Domain

## Summary

This procedure claims an unclaimed Azure .cloudapp.net domain identified from DNS reconnaissance, granting control over any subdomain pointing to it via CNAME.

## Description

After identifying a dangling CNAME to an unregistered Azure domain, attackers use the Azure Portal to create a Cloud Service (classic) with the exact domain name. This hijacks traffic from the original subdomain, as DNS resolution directs to the new Azure resource. In the Starbucks case, registering 1fd05821-7501-40de-9e44-17235e7ab48b.cloudapp.net enables full subdomain control for svcgatewayus.starbucks.com.

## Requirements

1. Valid Azure subscription
2. Exact unclaimed domain name from DNS analysis
3. Access to Azure Portal

## Defense

Defensive measures and detection strategies:

- Monitor Azure for new registrations of known dangling domains
- Automate DNS cleanup on resource deletion using Azure policies
- Use third-party services like Cloudflare for DNS validation

## Objectives

1. Secure ownership of the unclaimed cloud domain
2. Redirect traffic from vulnerable subdomains
3. Prepare for content deployment

## Instructions

### Step 1: Access Azure Portal

**Context**: Log in and navigate to resource creation.

Open https://portal.azure.com and sign in with Azure credentials.

### Step 2: Create Cloud Service

**Context**: Provision a classic Cloud Service matching the domain.

Search for 'Cloud Services (classic)' > Create > Enter name: 1fd05821-7501-40de-9e44-17235e7ab48b > Select region and subscription > Create.

> Expected: Confirmation of deployment; domain now owned by your account.

### Step 3: Confirm Registration

**Context**: Verify the domain is active in Azure.

In Portal, check the Cloud Service dashboard for the domain status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Azure-Portal]]

## Tags

- [[azure-hijack]]
- [[subdomain-takeover]]
