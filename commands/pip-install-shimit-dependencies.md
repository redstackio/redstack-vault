---
id: 4f696b1e-e488-439d-bf6c-8be3f99b9e3c
name: pip-install-shimit-dependencies
type: command
executor: bash
data: >-
  python -m pip install boto3 botocore defusedxml enum python_dateutil lxml
  signxml
output: null
created_at: '2023-04-06T03:56:09.723899+00:00'
updated_at: '2023-04-10T20:20:18.060634+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - installation
  - python
verified: true
validated: true
---

# pip-install-shimit-dependencies

## Command

```bash
python -m pip install boto3 botocore defusedxml enum python_dateutil lxml signxml
```

## Description

This command installs the Python dependencies required for the Shimit tool, including AWS SDK components (boto3, botocore), XML parsing (defusedxml, lxml), cryptography (signxml), and utilities (enum, python_dateutil). Use this prior to running Shimit for Golden SAML forgery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `boto3` | AWS SDK for Python | Yes |
| `botocore` | Low-level AWS interface | Yes |
| `defusedxml` | Secure XML parsing to prevent XXE | Yes |
| `enum` | Enum support for Python | Yes |
| `python_dateutil` | Date parsing utilities | Yes |
| `lxml` | XML/HTML processing library | Yes |
| `signxml` | XML digital signing | Yes |

No command-line flags are needed beyond the package list; pip handles the rest.

## Examples

### Basic Usage

```bash
python -m pip install boto3 botocore defusedxml enum python_dateutil lxml signxml
```

### Usage with Upgrade

```bash
python -m pip install --upgrade boto3 botocore defusedxml enum python_dateutil lxml signxml
```

## Expected Output

Collecting boto3
  Downloading boto3-1.26.0-py3-none-any.whl (...)
...
Successfully installed boto3-1.26.0 botocore-1.29.0 defusedxml-0.7.1 enum34-1.1.10 python-dateutil-2.8.2 lxml-4.9.1 signxml-2.9.0

## Related

- [[procedures/Golden-SAML-Attack-Using-Shimit]]
- [[commands/run-shimit-for-golden-saml-forgery]]
