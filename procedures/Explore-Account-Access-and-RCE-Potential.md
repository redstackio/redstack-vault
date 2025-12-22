---
id: proc-004
tags:
  - rce
  - deployment
  - aws-lambda
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/jq]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-list-netlify-site-functions]]'
verified: false
platforms:
  - Web
  - Cloud (AWS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:52.731Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Explore-Account-Access-and-RCE-Potential

## Summary

This procedure probes the compromised Netlify account for sites, functions, and deployment capabilities, identifying paths to remote code execution via arbitrary AWS Lambda function uploads.

## Description

With valid token access, query site-specific endpoints to list functions and explore deployment APIs. Netlify's Developer role allows uploading JavaScript or Go functions to AWS Lambda without validation, enabling RCE for malicious payloads, site defacement, or data exfiltration.

## Requirements

1. Validated Netlify token from prior step
2. curl and jq for API interactions
3. Knowledge of Netlify API docs for endpoints

## Defense

Defensive measures and detection strategies:

- Implement function code scanning and approval workflows
- Monitor API for unusual deployments or function uploads
- Use Netlify's audit logs to detect anomalous access

## Objectives

1. List account sites and functions
2. Identify RCE vectors
3. Assess impact on associated environments

## Instructions

### Step 1: List Site Functions

**Context**: Target a specific site to retrieve deployed functions, revealing Lambda integration.

**Command** ([[commands/curl-list-netlify-site-functions]]):
```bash
curl -X GET https://api.netlify.com/api/v1/sites/5a05c659-aa54-4184-bdbe-7faa4dd497b5/functions -H "Authorization: Bearer ████" -s | jq
```

> This queries functions for site ID 5a05c659-aa54-4184-bdbe-7faa4dd497b5 (crash-pings.mozilla.org). Use the token in the header; jq prettifies the response.

**Expected Output**: JSON with functions like {"id": "...", "name": "ping-details", "provider": "aws_lambda", "runtime": "nodejs18.x"}.

### Step 2: Explore Deployment Endpoints

**Context**: Review API docs for deploy endpoints to simulate RCE.

No specific command; manual review.

> Access Netlify API docs for PUT /deploys/{deploy_id}/functions/{name}. This allows uploading arbitrary code, e.g., malicious JS to execute on Lambda invocation.

**Expected Output**: Confirmation of unrestricted upload permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-list-netlify-site-functions]]

## Tools Used

- [[tools/curl]]
- [[tools/jq]]

## Tags

- [[rce]]
- [[aws-lambda]]
