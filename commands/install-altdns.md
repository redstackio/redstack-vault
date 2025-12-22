---
id: 5bade28d-2a67-43e1-b2f2-5f9bf6b01ce3
name: install-altdns
type: command
executor: bash
data: |-
  git clone https://github.com/infosec-au/altdns.git
  cd altdns/
  pip install -r requirements.txt
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - installation
  - recon
verified: true
validated: true
---

# install-altdns

## Command

```bash
git clone https://github.com/infosec-au/altdns.git
cd altdns/
pip install -r requirements.txt
```

## Description

This command installs AltDNS by cloning its GitHub repository and setting up Python dependencies. Use this before running subdomain permutation generation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Multi-line sequence; no parameters | N/A |

## Examples

### Basic Usage

```bash
git clone https://github.com/infosec-au/altdns.git
cd altdns/
pip install -r requirements.txt
```

### Advanced Usage

If pip fails, use `pip3` or a virtual environment: `python -m venv altdns_env && source altdns_env/bin/activate && pip install -r requirements.txt`.

## Expected Output

Cloning into 'altdns'...
remote: Enumerating objects: X, done.
...
Successfully installed dnspython-X.X.X

## Related

- [[procedures/Subdomain-Enumeration-using-AltDNS]]
- [[commands/generate-subdomain-permutations-with-altdns]]
