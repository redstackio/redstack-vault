---
tags:
  - information-disclosure
  - api-keys
  - github
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/define-omise-api-keys]]'
verified: false
platforms:
  - Web
  - GitHub
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:32:10.371Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 041d11d6-780f-4ba8-99e4-7d431f1309cf
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover-Exposed-API-Keys-in-GitHub-Repository

## Summary

This procedure outlines the manual discovery of exposed API keys in a public GitHub repository's documentation, specifically targeting example code in README files that may contain unredacted placeholders or real credentials, enabling potential unauthorized access to services like Omise payment API.

## Description

In this scenario, an attacker browses a public GitHub repository for the omise-php library and locates placeholder public and secret API keys in the README.md file's example code section. Although confirmed as non-functional placeholders by Omise, valid keys would allow operations such as creating customers, cards, charges, and retrieving account balances. The root cause is the inclusion of sensitive-looking example data without proper obfuscation in a public repo. This procedure requires only a web browser and internet access, with no authentication needed, making it accessible for reconnaissance in open-source projects.

## Requirements

1. Web browser with JavaScript enabled for GitHub navigation.
2. Internet connection to access public repositories.
3. Basic understanding of API keys and code repositories.

## Defense

Defensive measures and detection strategies:

- Regularly scan public repositories for sensitive data using tools like GitHub's secret scanning or TruffleHog.
- Implement code review processes to redact or use fake placeholders in example code before committing to public repos.
- Monitor API usage logs for anomalous activity from exposed keys.
- Use repository permissions to limit public access where possible.

## Objectives

1. Identify and extract potentially sensitive API keys from public documentation.
2. Assess the impact of disclosure on the target service (e.g., Omise API operations).
3. Report findings to prevent real credential exposure.

## Instructions

### Step 1: Access the Target Repository

**Context**: Navigate to the specific GitHub repository and commit to load the README file containing the example code.

No command required; use a web browser to visit: https://github.com/omise/omise-php/blob/1158aeceb83c55d4b2188b75ae0f899d7af3881a/README.md

> This loads the historical version of the README.md where the exposure occurred. Scroll down to the 'Example Usage' or similar section.

### Step 2: Locate and Extract API Keys

**Context**: Review the PHP example code for definitions of API constants, which reveal the public and secret keys.

**Command** ([[commands/define-omise-api-keys]]):
```php
<?php
require_once dirname(__FILE__).'/vendor/autoload.php';
define('OMISE_PUBLIC_KEY', 'pkey_test_54ot96fkr3i2op60cng');
define('OMISE_SECRET_KEY', 'skey_test_54ot96fkr3i2op60cng');
define('OMISE_API_VERSION', '2017-11-02');
```

> This code snippet defines the Omise API keys and version. Copy the values: Public key 'pkey_test_54ot96fkr3i2op60cng' for token creation, Secret key 'skey_test_54ot96fkr3i2op60cng' for server-side operations. Expected output is the definition of constants for library integration; no runtime execution is needed for discovery.

### Step 3: Validate Key Exposure

**Context**: Confirm the keys are visible in plain text and assess potential misuse.

Manually note the keys and test if they are placeholders by attempting a simple API call (if valid, this would confirm functionality; here, they fail as placeholders).

> Success is confirmed by the presence of the keys in the file. If valid, an attacker could use the secret key for actions like retrieving balance via Omise's API endpoints.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/define-omise-api-keys]]

## Tools Used


## Tags

- information-disclosure
- api-keys
- github
- reconnaissance
