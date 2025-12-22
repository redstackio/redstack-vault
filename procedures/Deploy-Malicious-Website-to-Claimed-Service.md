---
id: proc-deploy-website-azure
tags:
  - azure
  - deployment
  - payload
type: procedure
tools:
  - '[[tools/Azure-Portal]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Azure
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:38:49.770Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Deploy-Malicious-Website-to-Claimed-Service

## Summary

This procedure deploys a custom webpage, including proof-of-concept or malicious content, to the claimed Azure Cloud Service, making it accessible via the hijacked subdomain.

## Description

After claiming the service, upload a packaged website (e.g., HTML/JS for phishing or cookie theft) following Azure's deployment process. The target environment is the classic Cloud Service dashboard. Prerequisites: Owned service and basic web development skills. Outcomes: Malicious site live on the subdomain, enabling attacks like XSS or data exfiltration.

## Requirements

1. Claimed Azure Cloud Service
2. Packaged deployment files (.cspkg and .cscfg)
3. Content for the website (e.g., index.html with malicious script)

## Defense

Defensive measures and detection strategies:

- Enable Azure Security Center alerts for unusual deployments
- Scan uploaded packages for malware using Azure Defender
- Implement web application firewalls (WAF) on subdomains

## Objectives

1. Host arbitrary content on the trusted subdomain
2. Enable phishing, cookie theft, or security bypass
3. Demonstrate full takeover impact

## Instructions

### Step 1: Prepare Deployment Package

**Context**: Create the necessary files for Azure deployment.

**Instructions**: Develop a simple webpage (e.g., POC HTML showing takeover message). Package it into a .cspkg file using Azure SDK tools or manually zip with roles. Create a .cscfg config file specifying endpoints (e.g., HTTP on port 80).

> Reference Microsoft's guide: https://docs.microsoft.com/en-us/azure/cloud-services/cloud-services-how-to-create-deploy

### Step 2: Upload and Deploy

**Context**: Use the portal to deploy the package to the service.

**Instructions**: In Azure Portal, select the Cloud Service > Dashboard > Upload. Choose the .cspkg and .cscfg files, then deploy. Monitor the status for success.

> Deployment takes 5-15 minutes; check logs for errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Azure-Portal]]

## Tags

- [[azure]]
- [[deployment]]
- [[payload]]
