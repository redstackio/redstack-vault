---
data: r = requests.get(pull_url)
tags:
  - python
  - http
  - request
type: command
executor: python
platforms:
  - Web
  - GitHub Enterprise
id: c798f301-ffc3-416b-83e5-7af24ef86687
created_at: '2025-12-11T06:10:25.095Z'
updated_at: '2025-12-11T06:10:25.095Z'
verified: false
validated: true
submitted: true
---
# python-requests-get

## Command

```python
r = requests.get(pull_url)
```

## Description

Makes a GET request to the specified URL using the requests library in Python.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pull_url | The API endpoint URL | Yes |

## Examples

### Basic Usage

```python
r = requests.get("https://github.sc-corp.net/api/v3/repos/Snapchat/android/pulls/76793")
```

## Expected Output

Response object from the API call, including status code and content if successful.

## Related

- [[commands/python-construct-pull-url]]
- [[procedures/Extract-and-Validate-Leaked-GitHub-Token]]
