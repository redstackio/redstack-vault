---
tags:
  - ci-exposure
  - access-control
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 5800c45a-fd65-4aa2-822c-6dc733281310
created_at: '2025-12-11T06:10:24.998Z'
updated_at: '2025-12-11T06:10:24.998Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Access Publicly Exposed CI Instance

## Summary

This procedure involves discovering and accessing a publicly exposed internal Continuous Integration (CI) instance that lacks proper authentication, allowing unauthorized retrieval of sensitive data such as source code and credentials.

## Description

In this attack scenario, an internal CI tool used for building and deploying applications is inadvertently made accessible over the public internet without access controls. The procedure targets web and cloud environments where services like Jenkins or similar CI platforms are misconfigured. The expected outcome is the disclosure of critical assets, potentially leading to further compromise. Prerequisites include public internet access and basic knowledge of the target's domain.

## Requirements

1. Public internet connection to the target endpoint
2. Knowledge of the exposed CI URL (discovered via reconnaissance)
3. No special tools required; a web browser suffices

## Defense

Defensive measures and detection strategies:

- Implement strict access controls, such as VPN requirements or IP whitelisting for internal tools
- Regularly scan for exposed services using tools like Shodan or internal vulnerability scanners

## Objectives

1. Gain unauthorized access to the CI instance
2. Retrieve sensitive source code and credentials
3. Demonstrate the impact of improper access control

## Instructions

### Step 1: Identify the Exposed Endpoint

**Context**: Perform reconnaissance to locate the publicly accessible CI instance, such as through search engine dorking or subdomain scanning.

No specific command needed; use a web search or tools like Shodan to find endpoints like 'ci.snapchat.internal'.

> Expected: Discovery of the target URL without authentication barriers.

### Step 2: Access and Retrieve Data

**Context**: Directly navigate to the exposed CI instance and browse for sensitive information.

Use a web browser or curl to access:

```bash
curl https://exposed-ci-instance.snapchat.internal/
```

> Explanation: This retrieves the root page or directory listing, allowing download of build artifacts, source code, or credentials stored in configurations.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[ci-exposure]]
- [[access-control]]
