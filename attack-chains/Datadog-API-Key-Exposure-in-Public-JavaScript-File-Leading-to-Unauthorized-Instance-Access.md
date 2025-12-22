---
tags:
  - api-key-exposure
  - information-disclosure
  - datadog
  - credentials-leak
type: attack_chain
tools: []
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Exposed-Datadog-API-Keys-in-JavaScript-File]]'
  - '[[procedures/Validate-Unauthorized-Access-Using-Exposed-Datadog-Keys]]'
step_count: 2
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:29.288Z'
description: >-
  Attack chain demonstrating the discovery and validation of exposed Datadog API
  and application keys in a client-side JavaScript file, enabling unauthorized
  read and write access to the Datadog instance.
skill_level: beginner
impact_level: high
id: b6c34733-2c85-47fc-b741-67267a9b7535
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Datadog API Key Exposure in Public JavaScript File Leading to Unauthorized Instance Access

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Exposed Keys] --> B[Validation of Access]
    B --> C[Unauthorized Datadog Access Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools (e.g., Chrome DevTools)
- curl or similar HTTP client for validation

### Target Environment

- Web platform with publicly accessible JavaScript files
- Datadog services integrated
- No authentication required for JS file access

### Initial Access Requirements

- Public internet access to the target website
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Discovery of Exposed Keys
procedure: [[procedures/Identify-Exposed-Datadog-API-Keys-in-JavaScript-File]]

**Objective**: Inspect the target website's JavaScript files to identify embedded Datadog API and application keys.

**Instructions**: Navigate to the target website (e.g., █████) and use browser developer tools to view the source of publicly accessible JS files. Search for strings like 'apiKey' or 'applicationKey' within the code.

**Expected Output**: Exposed keys visible in the JS file, such as API key patterns (e.g., 'aa...') and application keys.

**Success Indicators**:
- Keys identified in client-side code
- Confirmation that keys are Datadog-specific

### Step 2: Validation of Access
procedure: [[procedures/Validate-Unauthorized-Access-Using-Exposed-Datadog-Keys]]

**Objective**: Demonstrate that the exposed keys grant unauthorized read and write access to the Datadog instance without further exploitation.

**Instructions**: Use the extracted keys to make API requests to Datadog endpoints, such as querying sites or metrics, to verify access.

**Expected Output**: Successful API responses from Datadog, confirming read/write permissions.

**Success Indicators**:
- API calls succeed with the exposed keys
- Access to sensitive Datadog data or configuration

## Attack Chain Summary

### Key Achievements

1. Identified critical API keys exposed in public JS file
2. Validated unauthorized access to Datadog instance
3. Highlighted potential for full read/write compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]]

### MITRE ATT&CK Tactics

- [[Credential Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
