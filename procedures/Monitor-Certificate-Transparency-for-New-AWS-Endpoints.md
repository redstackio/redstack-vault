---
tags:
  - aws
  - certificate-transparency
  - reconnaissance
type: procedure
tools:
  - '[[tools/Certificate-Transparency-Monitoring]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - AWS
  - Cloud
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: da3ebbad-8fc0-4a6e-9467-3555caa82973
created_at: '2025-12-14T17:32:39.244Z'
updated_at: '2025-12-14T17:32:39.244Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Monitor Certificate Transparency for New AWS Endpoints

## Summary

This procedure uses certificate transparency monitoring to detect newly issued SSL/TLS certificates for AWS services, identifying potential non-production API endpoints like those for Datazone that may lack logging.

## Description

In AWS environments, new API endpoints can be exposed through certificate issuances. By querying certificate transparency logs, attackers can discover non-production endpoints in real-time, such as those created within the last 24 hours for the Datazone service. This reconnaissance step is crucial for identifying unmonitored entry points that allow silent operations without CloudTrail logging, enabling subsequent permission enumeration.

## Requirements

1. Access to certificate transparency log services (e.g., crt.sh API or monitoring tools)
2. Scripting knowledge for automated queries (e.g., Python with requests library)
3. Focus on AWS-related domains (e.g., *.amazonaws.com subdomains)

## Defense

Defensive measures and detection strategies:

- Implement certificate issuance monitoring in AWS to alert on unexpected subdomain creations
- Use tools like AWS Certificate Manager logs to track and review new certificates
- Block or restrict access to non-production endpoints from external monitoring

## Objectives

1. Identify new non-production AWS Datazone endpoints
2. Gather URLs for subsequent API testing
3. Enable stealthy reconnaissance without direct AWS access

## Instructions

### Step 1: Query Certificate Transparency Logs

**Context**: Search for recent certificates issued to AWS Datazone-related domains to uncover new endpoints.

No specific command; use web-based tools or APIs like crt.sh to query for 'datazone' in AWS domains, filtering by issuance date (past 24 hours).

> Expected output: List of certificate details including subject alternative names (SANs) revealing endpoint URLs like custom non-prod subdomains.

### Step 2: Filter and Validate Endpoints

**Context**: Extract and verify potential non-production URLs from certificate data.

Manually or script to parse SANs for patterns indicating non-prod (e.g., dev, staging subdomains) and test basic connectivity.

> Expected output: Validated list of endpoint URLs ready for API probing.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Certificate-Transparency-Monitoring]]

## Tags

- [[aws]]
- [[certificate-transparency]]
- [[Reconnaissance]]
