---
id: b620d846-4df6-4a30-842b-aff05cf2e031
name: github-subdomains-enumerate-domain
type: command
executor: bash
data: |
  python3 github-subdomains.py -d $_DOMAIN -t
output: null
created_at: '2020-07-24T17:11:23.460131+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - subdomain-enumeration
verified: true
validated: true
---

# github-subdomains-enumerate-domain

## Command

```bash
python3 github-subdomains.py -d $_DOMAIN -t
```

## Description

This command executes the github-subdomains.py script to search public GitHub repositories for mentions of subdomains related to a specified domain, using an optional GitHub token for authenticated access to increase query limits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_DOMAIN` | Target domain to search for subdomains (e.g., owasp.com) | Yes |
| `-t` | Use GitHub personal access token from environment variable GITHUB_TOKEN | No (but recommended) |
| `-d` | Flag to specify the domain parameter | Yes |

## Examples

### Basic Usage

```bash
python3 github-subdomains.py -d owasp.com -t
```

### Advanced Usage

Redirect output to file: `python3 github-subdomains.py -d example.com -t > subdomains.txt`

## Expected Output

Searching GitHub for subdomains of owasp.com...
Found 5 subdomains:
api.owasp.com
www.owasp.com
docs.owasp.com
mail.owasp.com
staging.owasp.com
Total repositories searched: 123

## Related

- [[procedures/Scrape-GitHub-Repositories-for-Subdomains]]
- [[tools/GitHub-Subdomains]]
