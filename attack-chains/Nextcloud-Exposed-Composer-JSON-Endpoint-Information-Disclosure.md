---
tags:
  - information-disclosure
  - nextcloud
  - composer
  - json-leak
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Exposed-Composer-JSON-Endpoint]]'
  - '[[procedures/Inspect-Leaked-Sensitive-Data]]'
step_count: 2
techniques:
  - '[[Software]]'
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:26:00.660Z'
description: >-
  A reconnaissance attack exploiting an exposed JSON endpoint in Nextcloud's
  lookup service to disclose sensitive user and vendor details, including emails
  and software versions.
skill_level: beginner
impact_level: medium
id: 9b046e34-ada9-4745-b56d-198bd0e962cb
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
  - '[[Vulnerability Scanning]]'
---
# Nextcloud Exposed Composer JSON Endpoint Information Disclosure

Multi-stage attack chain demonstrating reconnaissance via an exposed endpoint in Nextcloud's vendor lookup service, leading to the leakage of sensitive installation details for users and vendors.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Exposed Endpoint] --> B[Inspect Leaked Data]
    B --> C[Reconnaissance Complete]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- Web platform
- Nextcloud lookup service accessible
- No authentication required

### Initial Access Requirements

- Public internet access
- Knowledge of the target URL: https://lookup.nextcloud.com/vendor/composer/installed.json
- No credentials or prior access needed

## Detailed Attack Procedures

### Step 1: Access Exposed Endpoint
procedure: [[procedures/Access-Exposed-Composer-JSON-Endpoint]]

**Objective**: Retrieve the raw JSON data from the unprotected endpoint to initiate information gathering.

**Instructions**: Use [[commands/curl-fetch-json-endpoint]] to access the URL and save the response:

```bash
curl https://lookup.nextcloud.com/vendor/composer/installed.json -o composer_data.json
```

**Expected Output**: A JSON file containing package details.

**Success Indicators**:
- HTTP 200 response received
- JSON file downloaded without errors

### Step 2: Inspect Leaked Data
procedure: [[procedures/Inspect-Leaked-Sensitive-Data]]

**Objective**: Analyze the JSON content to extract sensitive information such as usernames, emails, and software versions for reconnaissance.

**Instructions**: Open the downloaded JSON file and parse it manually or with a tool like jq. For example, use [[commands/jq-parse-json]] to filter emails:

```bash
jq '.[] | .authors[] | .email' composer_data.json
```

**Expected Output**: List of leaked details including emails, versions, and installation paths.

**Success Indicators**:
- Sensitive data like emails and versions visible
- Potential targets for phishing identified

## Attack Chain Summary

### Key Achievements

1. Accessed unprotected endpoint without authentication
2. Disclosed user emails, usernames, and software versions
3. Enabled further reconnaissance or targeted attacks like phishing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Software]]
- [[Vulnerability Scanning]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
