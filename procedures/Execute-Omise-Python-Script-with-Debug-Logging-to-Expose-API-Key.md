---
tags:
  - debug-logging
  - credential-leak
  - python-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-omise-customer-with-api-secret]]'
verified: false
platforms:
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:20.770Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a945887f-4ff7-4fa2-8f1f-163d1c518146
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
  - '[[Unsecured Credentials]]'
---
# Execute-Omise-Python-Script-with-Debug-Logging-to-Expose-API-Key

## Summary

This procedure reproduces the cleartext logging vulnerability in the omise-python library by enabling debug mode and running a sample script that authenticates with a secret API key, capturing the key in console logs to demonstrate exposure risks.

## Description

In debug mode, the library's request.py logs the full Authorization header including the API secret key. This procedure sets up a Python environment, configures logging to DEBUG, and executes a customer creation call, resulting in the key being printed to the console. It targets local development setups using the library, highlighting how logs in demos, CI outputs, or shared files could leak production keys, allowing unauthorized API access for malicious actions.

## Requirements

1. Python 2.7+ or 3.x installed.
2. omise-python library installed via pip.
3. A test API secret key from Omise dashboard.
4. Logging module configured for DEBUG level.

## Defense

Defensive measures and detection strategies:

- Disable debug logging in production environments.
- Mask secrets in logs using tools like logredactor or custom filters.
- Monitor logs for patterns matching API key formats (e.g., skey_test_).
- Use environment variables for secrets and avoid debug mode in shared setups.

## Objectives

1. Trigger the debug logging to expose the API key.
2. Confirm the vulnerability leads to cleartext credential output.
3. Evaluate the potential for unauthorized Omise API access.

## Instructions

### Step 1: Install Library and Configure Logging

**Context**: Prepare the environment to enable debug output.

Install omise and set logging level.

**Command** (pip-install-omise):
```bash
pip install omise
python -c "import logging; logging.basicConfig(level=logging.DEBUG)"
```

> Installs the library and configures DEBUG logging globally. Expected output: No errors, ready for script execution.

### Step 2: Run Sample Script to Create Customer

**Context**: Execute code that uses the API key, triggering the log.

Use [[commands/create-omise-customer-with-api-secret]] to set the secret and create a customer.

**Command** ([[commands/create-omise-customer-with-api-secret]]):
```python
import omise
omise.api_secret = 'skey_test_5sqdfyjv0rtqzs9f2x2'

customer = omise.Customer.create(
 description='John Doe',
 email='john.doe@example.com'
)
```

> This authenticates and creates a customer, logging the key in DEBUG mode. Expected output: Console shows 'DEBUG:omise.request:Authorization: skey_test_5sqdfyjv0rtqzs9f2x2' and customer object.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] Command and Scripting Interpreter: Python
- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/create-omise-customer-with-api-secret]]

## Tools Used


## Tags

- [[debug-logging]]
- [[credential-leak]]
- [[python-execution]]
