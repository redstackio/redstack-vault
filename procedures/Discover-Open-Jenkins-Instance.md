---
tags:
  - recon
  - jenkins
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Jenkins
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: dccc90d7-6125-4140-a105-bdb248985099
created_at: '2025-12-11T03:47:56.631Z'
updated_at: '2025-12-11T03:47:56.631Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Discover Open Jenkins Instance

## Summary

This procedure involves reconnaissance to identify publicly accessible Jenkins instances, potentially misconfigured for unauthorized access.

## Description

Jenkins servers exposed to the internet can be discovered through scanning or probing for specific headers and endpoints. This is often the first step in exploiting misconfigurations like open OAuth logins. The target environment is a web-based CI/CD platform, and success leads to identifying login pages for further exploitation.

## Requirements

1. Network access to the target domain or IP
2. Reconnaissance tools like curl
3. Knowledge of Jenkins default ports (e.g., 8080)

## Defense

Defensive measures and detection strategies:

- Restrict Jenkins access to internal networks or VPN
- Monitor for unusual probes to /login or root endpoints

## Objectives

1. Identify accessible Jenkins server
2. Confirm presence of login page
3. Prepare for authentication attempts

## Instructions

### Step 1: Probe for Jenkins Headers

**Context**: Send a HEAD request to detect Jenkins-specific headers.

**Command** ([[commands/curl-jenkins-probe]]):

```bash
curl -I https://jenkins.target.com
```

> This command checks for headers like 'X-Jenkins' to confirm the service.

### Step 2: Verify Login Page

**Context**: Access the root or login endpoint to confirm accessibility.

**Command** ([[commands/curl-jenkins-probe]]):

```bash
curl https://jenkins.target.com/login
```

> Look for HTML content indicating a login form or OAuth options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-jenkins-probe]]

## Tools Used

- #curl

## Tags

- #recon
- [[commands/curl-jenkins-probe]]
