---
data: python3 -m pip install requests beautifulsoup4
tags:
  - python
  - dependencies
  - installation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.292Z'
id: 85bfeaf0-5fa2-4f36-b99c-509a48618d8d
verified: false
validated: true
submitted: true
---
# install-python-dependencies-for-bypass-script

## Command

```bash
python3 -m pip install requests beautifulsoup4
```

## Description

This command installs the required Python libraries (requests for HTTP sessions and BeautifulSoup for HTML parsing) necessary to run the Nextcloud 2FA bypass script, which automates session creation and cookie manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Run the pip module as a script | Yes |
| `pip` | Python package installer | Yes |
| `install` | Install specified packages | Yes |
| `requests` | HTTP library for requests | Yes |
| `beautifulsoup4` | HTML parsing library | Yes |

## Examples

### Basic Usage

```bash
python3 -m pip install requests beautifulsoup4
```

### Advanced Usage

```bash
python3 -m pip install requests beautifulsoup4 --user
```

## Expected Output

Successful installation messages, e.g., 'Successfully installed requests-2.31.0 beautifulsoup4-4.12.2'. Verify with `pip list | grep requests`.

## Related

- [[commands/execute-nextcloud-2fa-bypass-script]]
- [[procedures/Bypass-2FA-via-Session-Cookie-Manipulation]]
