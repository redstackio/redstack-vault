---
id: proc-uuid-2
tags:
  - aws
  - console-navigation
  - elb
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
updated_at: '2025-12-14T05:32:24.130Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.001]]'
---
# Navigate-AWS-Console-to-Load-Balancers

## Summary

This procedure guides navigation within the AWS console to the Elastic Load Balancing section, preparing for the creation of a new load balancer to exploit a dangling CNAME.

## Description

After setting the region, accessing the Load Balancers dashboard allows initiation of ELB creation. This step is crucial in the takeover chain as it leads directly to resource provisioning that can hijack the subdomain's traffic.

## Requirements

1. Active AWS session in us-west-2
2. EC2 service permissions (default for new accounts)

## Defense

Defensive measures and detection strategies:

- Use AWS Config to track console access patterns
- Enable GuardDuty for anomalous service navigations

## Objectives

1. Locate Load Balancing services
2. Prepare for ALB creation interface
3. Confirm access to ELB management

## Instructions

### Step 1: Access EC2 Dashboard

**Context**: EC2 hosts the Load Balancing category.

From the AWS services search bar, type 'EC2' and select the EC2 service to open the dashboard.

> EC2 console loads with resource overviews.

### Step 2: Select Load Balancers

**Context**: Navigate to the specific ELB management area.

In the left sidebar under 'Load Balancing', click 'Load Balancers'.

> The Load Balancers list view appears, showing any existing ELBs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1583.001]] Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- aws-navigation
- load-balancer
