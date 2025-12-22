---
type: command
executor: bash
data: |-
  pip install lxml
  pip install signxml
  pip uninstall -y cryptography
  cd cryptography
  pip install -e .
  cd ../ADFSpoof
  pip install -r requirements.txt
platforms:
  - Linux
  - macOS
tags:
  - python
  - dependencies
verified: true
validated: true
---

# install-python-dependencies-for-adfsspoof

## Command

```bash
pip install lxml
pip install signxml
pip uninstall -y cryptography
cd cryptography
pip install -e .
cd ../ADFSpoof
pip install -r requirements.txt
```

## Description

Installs XML parsing libraries, replaces the default cryptography package with a modified version, and sets up ADFSpoof requirements in the active virtual environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None (fixed paths assumed) | Relies on current directory structure | Yes |

## Examples

### Basic Usage

```bash
pip install lxml
pip install signxml
pip uninstall -y cryptography
cd cryptography
pip install -e .
cd ../ADFSpoof
pip install -r requirements.txt
```

### Advanced Usage

If in venv, ensure activated first. Use `pip install --upgrade` for latest versions.

## Expected Output

Collecting lxml
...
Successfully installed lxml-4.x.x
...
Uninstalling cryptography:
  Successfully uninstalled cryptography-3.x.x
Obtaining file:///path/cryptography
Installing collected packages: cryptography
Successfully installed cryptography
Collecting ... (from requirements.txt)
...

All packages installed without errors.

## Related

- [[procedures/Golden-SAML-Attack-via-ADFS]]
