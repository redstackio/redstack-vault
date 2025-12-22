---
id: proc-craft-xss-package
tags:
  - xss
  - python
  - setup.py
  - distutils
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.192Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Python-Package-with-XSS-Payload

## Summary

This procedure creates a Python package with a malicious setup.py file that injects JavaScript URIs into the home_page and download_url metadata fields, exploiting downstream HTML rendering without sanitization in services like Uber's PyPI mirror.

## Description

In the attack scenario, a Python package is crafted using distutils.core to define setup parameters. By setting home_page and download_url to 'Javascript:alert(0)', the metadata becomes a vector for stored XSS when mirrored sites render these as <a href> links without validating or escaping the URI scheme. This is particularly effective against public repositories that auto-generate package pages. Prerequisites include a Python environment with distutils installed. Expected outcomes include a packaged .tar.gz file that, when uploaded, propagates the payload to vulnerable mirrors.

## Requirements

1. Python 2 or 3 with distutils.core module
2. Basic knowledge of Python packaging
3. Local development environment for building packages

## Defense

Defensive measures and detection strategies:

- Sanitize all URL fields in package metadata to block javascript: schemes
- Implement Content Security Policy (CSP) on mirror sites to restrict script execution
- Monitor for anomalous package uploads with suspicious URLs in metadata

## Objectives

1. Inject persistent XSS payload into package metadata
2. Prepare package for upload to public repositories
3. Enable exploitation via unsanitized rendering on mirrors

## Instructions

### Step 1: Create setup.py File

**Context**: Define the package setup with malicious metadata to embed the JavaScript URI.

Create a file named setup.py with the following content:

```python
from distutils.core import setup

setup(
    name='ignore-me',
    version='1.0',
    home_page='Javascript:alert(0)',
    download_url='Javascript:alert(0)',
)
```

> This sets the home_page and download_url to the XSS payload, which will be rendered as clickable links later.

### Step 2: Package the File

**Context**: Build the package into a distributable archive.

Run the following to create the .tar.gz:

```bash
python setup.py sdist
```

> This generates ignore-me-1.0.tar.gz in the dist/ directory, containing the malicious metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- python
- metadata-injection
