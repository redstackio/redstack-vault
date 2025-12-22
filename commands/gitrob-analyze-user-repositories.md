---
type: command
executor: bash
data: >-
  gitrob analyze $_USERNAME --site=https://github.com
  --endpoint=https://api.github.com --access-tokens=$_GITHUB_TOKENS
output: null
platforms:
  - Linux
tags:
  - reconnaissance
  - leak-detection
verified: true
validated: true
---

# GitRob Analyze User Repositories

## Command

```bash
gitrob analyze $_USERNAME --site=https://github.com --endpoint=https://api.github.com --access-tokens=$_GITHUB_TOKENS
```

## Description

This command uses GitRob to scan a GitHub user's repositories for sensitive information like API keys, passwords, and private data, generating a report on potential leaks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| analyze $_USERNAME | Username or org to analyze | Yes |
| --site | GitHub site URL (default: github.com) | No |
| --endpoint | API endpoint URL | No |
| --access-tokens | Comma-separated GitHub tokens for auth | Yes (for rate limits) |

## Examples

### Basic Usage

```bash
gitrob analyze johndoe --access-tokens=ghp_token123
```

### Advanced Usage (Enterprise)

```bash
gitrob analyze johndoe --site=https://github.acme.com --endpoint=https://github.acme.com/api/v3 --access-tokens=token1,token2
```

## Expected Output

Report of findings:

```
Analyzing repositories...
Found 2 secrets:
- AWS Access Key in repo/file.py (line 10)
- Private key in config.pem
Report saved to gitrob-report.json
```

## Related

- [[procedures/passive-reconnaissance-information-gathering]]
- [[tools/gitrob]]
