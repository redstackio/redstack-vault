---
tags:
  - information-disclosure
  - api-keys
  - github
  - credentials-leak
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - GitHub
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Exposed-API-Keys-in-GitHub-Repository]]'
step_count: 1
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:32:10.377Z'
description: >-
  Discovery of exposed placeholder API keys in the public GitHub repository for
  the omise-php library, leading to potential unauthorized access if keys were
  valid.
skill_level: beginner
impact_level: high
id: 0f2aea37-1ad3-4b0c-a2cd-f5b5e30bff59
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Information Disclosure of Omise API Keys via Public GitHub Repository

Multi-stage attack chain demonstrating a complete attack workflow for discovering exposed credentials in a public code repository.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Access Repository] --> B[Discovery: Review README for Keys]
    B --> C[Objective: Extract Exposed Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Public GitHub repository
- No authentication required
- Internet access

### Initial Access Requirements

- No credentials needed
- Publicly accessible URL
- No prior access

## Detailed Attack Procedures

### Step 1: Repository Reconnaissance and Credential Discovery
procedure: [[procedures/Discover-Exposed-API-Keys-in-GitHub-Repository]]

**Objective**: Access the target GitHub repository and identify exposed API keys in the documentation files.

**Instructions**: Navigate to the Omise PHP library repository on GitHub. Use a web browser to open the specific commit of the README.md file and scroll to the example code section to locate the API key definitions.

Directly access the URL: https://github.com/omise/omise-php/blob/1158aeceb83c55d4b2188b75ae0f899d7af3881a/README.md

Scroll down to the PHP example code, where the following constants are defined:

```php
<?php
require_once dirname(__FILE__).'/vendor/autoload.php';
define('OMISE_PUBLIC_KEY', 'pkey_test_54ot96fkr3i2op60cng');
define('OMISE_SECRET_KEY', 'skey_test_54ot96fkr3i2op60cng');
define('OMISE_API_VERSION', '2017-11-02');
```

Extract the keys: Public key `pkey_test_54ot96fkr3i2op60cng` and Secret key `skey_test_54ot96fkr3i2op60cng`.

**Expected Output**: Visibility of placeholder API keys in the example code, which could be copied for testing.

**Success Indicators**:
- README.md file loads successfully
- Example code section reveals API key definitions
- Keys are present and readable in plain text

## Attack Chain Summary

### Key Achievements

1. Identified exposed placeholder API keys in a public repository README.
2. Demonstrated potential for unauthorized API operations if keys were valid.
3. Highlighted risks of unredacted example code in public repos.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
