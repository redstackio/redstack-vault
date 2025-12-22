---
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/NxEmSxWnQK1GxnM8DPfvyTze?response-content-disposition=attachment%3B%20filename%3D%22samlbypasspoc.py%22%3B%20filename%2A%3DUTF-8%27%27samlbypasspoc.py&response-content-type=text%2Fx-python&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ2AVDIBDU%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T230906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDjxOv184kh7NXsgDfUxanpu4kjsN0ww17C0GkSDCnpKgIgdGGdsc9aCWjn2ZSGk4%2BVPY0tzzZ3eRPZ2jZukHus%2BQEqsgUIEBADGgwwMTM2MTkyNzQ4NDkiDH5yPnTogcYn47ivHSqPBX4UMr5v3RA6GoSUY3KywqXTxUPdsZpUaksBHJpAwsu57vosv7x4ZNM5TfbiG%2BK0MDxOieqQATMmeEgOLGbVseT5llablWM%2BvJ8iBtB%2BWelCNuzuHd9ItqD8zhwWrxiXF%2F1kZOTFJUIUbR2HSdkO6HFCCaB8LXI%2FrgJm1yvdZT3AZryJ%2Bj9yV11IOxqv%2BIt7cr%2F76WT2qCrlNx9TL%2BrgaOs101yt0dPyZ5YuX%2BqjoEnsVranXM2R5CSkMTYZyb%2BCJZrVvMiDhl0oXYKgFyy9e1avQ9lvZ8nV%2BaALfJExU%2FaC9N3X%2FfuAFZ2TRs95hWgyoeVgYGM4P2Rhhn%2FPmCO3Ji40TUoNNs4Z6%2FttBslOxFZRpOx5gZGKjxUYhv%2FktQoaHc8q1SzSHm5oc66ZnYeQ1frdlC91IjYm%2BZXV80oWuw%2FEH0bPiy2ur2I4TX7lXbwRuE0BN%2FH2rDmQO%2B%2FuTm8PleYi1%2Bt0oftbHF%2B94HCQGW4wssDgncbaWj3eURirNUQsfG76mltAgGThItqf1CKzaCypyYGYAW%2FZxDkfpTYvvv175ai7A52Q3CFQ0XgwizO7vBtX%2BCrLusEe01qS17DB4nkbKL0MUSSlxL5z5J6OiPDA4PpSs1fS3B70sZuKP7m0x7zP1IAGYCR2jGIqJasO8OoQVe3bG%2B7IKk6dJNn6QGge%2Buij0BO3ql3RH32JUpjaCBbXhkc5GVyX5bnqsT9c6uOdLKA48KiWNdzlbw4W9HW2wEdIRXI5Oq%2F6R5XvqePJYIDGOyyC23tHmZ4bEhvtrBe8pa%2BJTRangT%2FZytaoFMOHY%2BAymI%2FrlqvGkr87eq%2F8ImaxoyOxbPbpC3fKq3cSmZsO%2FEj8ZjQSB4dCzt2%2FlJYwzrryyQY6sQHf1wVdp%2B6Yxo9LTi0VcS8OL5qmKv3QGoJR%2BruwyaOgKMWLCTg6hPa9OxtGPA5Rny%2FDS9WiarmluvGn4ekyuNo6oTVIRrkrbeDLqmlDmDKgrF0I727F4TDE67%2Ff3ViraRYbivMSVlziHIkd2JRoDXhHbDO3BZtvh39M43WNVylcuRKmsFOkLQnINf3Hq1KO3HYC5NdWmxnekO2foerjLsoiXw9TuyM4R9ESpytF14KkOFs%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=7f74d910927791fd57ce302cfa65b32a13fe85e94d3bdc49ff0569b7aef0b4fb
tags:
  - poc
  - saml
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: POC script for SAML bypass
id: f765a3cb-127d-492a-96bd-6f4115c15d4a
created_at: '2025-12-13T09:01:26.287Z'
updated_at: '2025-12-13T09:01:26.287Z'
verified: false
validated: true
submitted: true
---
# samlbypasspoc.py

**Status**: Unverified

## Overview

Proof-of-concept Python script to bypass SAML authentication by injecting malicious Response elements into a valid SAML response.

## Description

The script decodes the input SAMLResponse, adds an unsigned malicious Response with custom assertions, and outputs the tampered version for injection.

## Features

- XML manipulation for SAML
- Custom attribute injection
- Base64 encoding/decoding

## Installation

### Requirements

- Python3

### Install Commands

```bash
# Download from URL and save as samlbypasspoc.py
```

## Basic Usage

```bash
python3 samlbypasspoc.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| None | Takes one argument: URL-encoded SAMLResponse |

## Examples

### Example 1: Basic Usage

```bash
python3 samlbypasspoc.py <encoded_response>
```

### Example 2: Advanced Usage

Edit script line 25+ for custom values, then run.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitoring for Python scripts processing XML
- Anomalous SAML response sizes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Python3]]

## References

- HackerOne report attachment
