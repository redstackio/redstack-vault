---
tags:
  - recon
  - endpoint-discovery
  - authorization-testing
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3f06d7a2-e5da-4c9d-9093-c4cf7627e754
created_at: '2025-12-14T17:29:44.918Z'
updated_at: '2025-12-14T17:29:44.918Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-UpdateEmployees-RPC-Endpoint

## Summary

This procedure involves locating and testing the updateEmployees RPC endpoint in Uber's Business platform to identify authorization flaws, particularly cross-tenant access issues that enable insecure direct object references.

## Description

In the context of Uber's Business platform, attackers with regular employee access can probe the RPC endpoints for improper checks on tenant boundaries. By examining the updateEmployees endpoint, flaws in authorization allow access to employee data across different tenants, setting the stage for privilege escalation. This is typically done via browser developer tools or an intercepting proxy to inspect requests and responses, revealing the lack of ownership verification for employeeUuid parameters.

## Requirements

1. Authenticated session as a regular Uber Business employee
2. Access to browser dev tools or HTTP client for endpoint inspection
3. Basic knowledge of RPC endpoints and JSON payloads

## Defense

Defensive measures and detection strategies:

- Implement strict tenant isolation checks on all employee-related endpoints
- Log and monitor anomalous cross-tenant requests
- Use role-based access controls (RBAC) to validate ownership before updates

## Objectives

1. Confirm the presence of the updateEmployees endpoint
2. Identify missing authorization for cross-tenant employeeUuid access
3. Gather details for crafting exploitative requests

## Instructions

### Step 1: Access the Platform and Monitor Traffic

**Context**: Log in to the Uber Business platform and navigate to employee management sections to capture RPC calls.

Open browser dev tools (Network tab) and perform actions like viewing employees to identify RPC requests.

**Expected Output**: Observation of requests to https://business.uber.com/_rpc?rpc=updateEmployees.

### Step 2: Test Endpoint Authorization

**Context**: Directly probe the endpoint to check for validation flaws.

Send a GET or OPTIONS request to the endpoint to see if it exposes information without proper checks.

**Expected Output**: Response indicating the endpoint is accessible, potentially without tenant restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]

