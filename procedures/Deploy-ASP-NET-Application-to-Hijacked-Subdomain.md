---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - asp-net-deployment
  - azure-deploy
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/Visual-Studio]]'
  - '[[tools/Azure-Portal]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Azure
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T04:38:49.791Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Deploy ASP.NET Application to Hijacked Subdomain

## Summary

This procedure involves creating, packaging, and deploying a custom ASP.NET web application to the hijacked Azure Cloud Service, allowing arbitrary content hosting on the subdomain.

## Description

Using Visual Studio, attackers build an ASP.NET app in Azure-compatible format (e.g., .cspkg), then upload it via the Portal. The app can serve malicious payloads. In the example, a PoC page with 'Subdomain takeover PoC' is deployed, demonstrating control over svcgatewayus.starbucks.com for potential XSS, phishing, or malware.

## Requirements

1. Visual Studio installed with Azure SDK
2. Registered Cloud Service and storage
3. Azure Portal access

## Defense

Defensive measures and detection strategies:

- Monitor Azure deployments for suspicious packages
- Use WAF to inspect traffic to subdomains
- Implement certificate pinning to prevent fake SSL

## Objectives

1. Host custom content on the hijacked domain
2. Demonstrate full control for exploitation
3. Enable advanced attacks like auth bypass

## Instructions

### Step 1: Create ASP.NET App

**Context**: Develop a simple web app in Visual Studio.

New Project > ASP.NET Web Application (.NET Framework) > Empty > Add Default.aspx with PoC content.

### Step 2: Package for Azure

**Context**: Generate deployment package per Azure docs.

Right-click project > Publish > Azure > Cloud Service > Package.

> Expected: .cspkg and .cscfg files generated.

### Step 3: Deploy via Portal

**Context**: Upload to Cloud Service.

In Azure Portal > Cloud Service > Upload > Select .cspkg > Configure > Deploy.

> Expected: Deployment status 'Ready'; app live on domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Visual-Studio]]
- [[tools/Azure-Portal]]

## Tags

- [[asp-net]]
- [[subdomain-takeover]]
