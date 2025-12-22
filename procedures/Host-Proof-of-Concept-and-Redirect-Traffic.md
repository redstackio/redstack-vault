---
id: p4d5e6f7-g8h9-0123-defg-4567890123
tags:
  - poc
  - hosting
  - redirect
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python-http-server]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:51:26.522Z'
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
# Host Proof-of-Concept and Redirect Traffic

## Summary

This procedure hosts a proof-of-concept file on the claimed domain and sets up redirects to demonstrate control and mitigate immediate risks.

## Description

After claiming ████, upload a POC file and redirect subdomain traffic to a blank page, showing potential for phishing or XSS without actual exploitation.

## Requirements

1. Hosting access on the domain
2. File upload capabilities
3. Basic web server knowledge

## Defense

Defensive measures and detection strategies:

- Monitor traffic anomalies on subdomains via Azure Application Insights
- Block unexpected redirects with WAF rules
- Audit hosted content regularly

## Objectives

1. Prove domain control
2. Redirect to safe page
3. Highlight vulnerability impact

## Instructions

### Step 1: Create and Host POC File

**Context**: Generate a simple text file as evidence.

**Command** ([[commands/python-http-server]]):
```bash
echo "POC: Subdomain taken over on $(date)" > proof.e7437329-ab61-4f22-a049-df5b3685313a.txt
python3 -m http.server 80
```

> Serves the file locally; upload to hosting provider. Access at https://████████/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt.

### Step 2: Configure Redirect

**Context**: Set up HTTP redirect to blank page.

Use registrar's DNS or .htaccess:

```apache
RewriteEngine On
RewriteRule ^(.*)$ https://blank-page.com [R=301,L]
```

Upload via hosting panel.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/python-http-server]]

## Tools Used


## Tags

- [[poc]]
- [[hosting]]
