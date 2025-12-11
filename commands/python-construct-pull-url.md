---
data: >-
  pull_url = "https://github.sc-corp.net/api/v3/repos/Snapchat/android/pulls/" +
  str(pull_number)
tags:
  - python
  - variable
  - url
type: command
executor: python
platforms:
  - Web
  - GitHub Enterprise
id: c6fdb3ce-3132-45c9-b627-050110667d90
created_at: '2025-12-11T06:10:25.208Z'
updated_at: '2025-12-11T06:10:25.208Z'
verified: false
validated: true
submitted: true
---
# python-construct-pull-url

## Command

```python
pull_url = "https://github.sc-corp.net/api/v3/repos/Snapchat/android/pulls/" + str(pull_number)
```

## Description

Constructs the URL for the GitHub API endpoint to fetch a specific pull request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pull_url | String concatenation of base URL and pull_number | Yes |

## Examples

### Basic Usage

```python
pull_url = "https://github.sc-corp.net/api/v3/repos/Snapchat/android/pulls/" + str(76793)
```

## Expected Output

No output; variable is set to the full URL.

## Related

- [[commands/python-requests-get]]
- [[procedures/Extract-and-Validate-Leaked-GitHub-Token]]
