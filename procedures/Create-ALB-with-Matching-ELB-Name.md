---
id: proc-uuid-3
tags:
  - aws
  - alb-creation
  - domain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1583.001]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:24.112Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.001]]'
  - '[[Exploit Public-Facing Application]]'
---
# Create-ALB-with-Matching-ELB-Name

## Summary

This procedure initiates the creation of an Application Load Balancer using the exact name prefix from the dangling ELB CNAME, setting the stage for subdomain resolution hijacking.

## Description

The dangling record points to a specific ELB format; by selecting ALB type and inputting the prefix (e.g., a0e7eaaaa82f611e9b1cc0e9ccd15f3e), the attacker ensures the generated DNS name can match the target upon deployment.

## Requirements

1. Access to Load Balancers dashboard
2. Knowledge of CNAME prefix from DNS query (e.g., via dig or nslookup)

## Defense

Defensive measures and detection strategies:

- Implement ELB naming conventions with prefixes to prevent collisions
- Use AWS Organizations to restrict resource creation in sensitive regions

## Objectives

1. Select appropriate LB type
2. Input matching name for DNS alignment
3. Advance to configuration without errors

## Instructions

### Step 1: Initiate Load Balancer Creation

**Context**: Start the wizard for new resource.

Click the 'Create Load Balancer' button on the Load Balancers page.

> Creation wizard opens with type selection.

### Step 2: Choose Application Load Balancer and Set Name

**Context**: Match the original ELB type and name.

Select 'Application Load Balancer', then in the name field, enter the prefix from the CNAME (e.g., a0e7eaaaa82f611e9b1cc0e9ccd15f3e).

> Form validates the name; proceed to next steps like network configuration (use defaults for basic takeover).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1583.001]] Domains
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- alb-setup
- name-matching
