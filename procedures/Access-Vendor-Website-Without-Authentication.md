---
tags:
  - access-control
  - unauthorized-access
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.303Z'
sub_techniques: []
id: 6bea5092-56c2-427d-b7bf-c43e6bc6b5e2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Vendor-Website-Without-Authentication

## Summary

This procedure exploits a lack of authentication on a vendor's web application to directly access internal pages, enabling unauthorized viewing and potential extraction of sensitive business documents, such as tax records from Uber Brazil.

## Description

In this scenario, a third-party vendor website operated for Uber services fails to implement proper access controls, allowing any unauthenticated visitor to reach restricted areas. By simply navigating to internal URLs without logging in, an attacker can view confidential data. The target environment is a standard web application, likely built on common frameworks without session or role-based checks. Prerequisites include only a modern web browser and internet access. Expected outcomes include immediate exposure of sensitive information, highlighting risks in supply chain security for organizations like Uber.

## Requirements

1. Internet connectivity to reach the public vendor website
2. A standard web browser (no extensions or special software needed)
3. Knowledge of potential internal URL paths (e.g., via directory guessing or prior reconnaissance)

## Defense

Defensive measures and detection strategies:

- Implement robust authentication (e.g., OAuth, JWT) on all internal endpoints
- Use role-based access control (RBAC) to restrict pages by user permissions
- Monitor access logs for anomalous unauthenticated requests to sensitive paths
- Conduct regular vendor security audits and enforce secure development practices

## Objectives

1. Achieve initial unauthorized entry into the internal web system
2. Expose and potentially download sensitive documents like tax files
3. Demonstrate the vulnerability for reporting and remediation

## Instructions

### Step 1: Navigate to the Vendor Website

**Context**: Begin by accessing the root of the vendor's public website to confirm accessibility, then attempt to reach internal sections without providing credentials.

Directly enter the URL `https://█████████.com` in your browser's address bar and press Enter. Observe that no login page appears.

> If the site loads publicly available content, proceed to test internal paths.

### Step 2: Attempt Access to Internal Pages

**Context**: Target restricted areas by appending common internal path segments to the base URL, exploiting the absence of authentication checks.

In the browser, navigate to suspected internal URLs such as `https://█████████.com/internal`, `https://█████████.com/admin`, or `https://█████████.com/documents`. No login or authorization is required, granting direct access.

> Successful navigation reveals internal interfaces, including Uber Brazil tax documents and system tools. Download or screenshot evidence if needed for verification.

### Step 3: Verify Sensitive Data Exposure

**Context**: Confirm the impact by inspecting the loaded content for confidential information.

Review the page content for sensitive elements like financial documents or operational data. If documents are listed, attempt to open or download them to validate exposure.

> Expected result: Unrestricted access to files containing Uber-specific tax and operational details, confirming the access control failure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-control
- unauthorized-access
- web
