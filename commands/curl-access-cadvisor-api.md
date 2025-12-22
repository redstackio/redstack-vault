---
id: 868d81c9-58bf-4295-b3b7-c227001f67bc
name: curl-access-cadvisor-api
type: command
executor: bash
data: 'curl -k https://$_NODE_IP:4194/'
output: null
created_at: '2023-04-06T03:56:01.426971+00:00'
updated_at: '2023-04-10T20:34:05.848077+00:00'
platforms:
  - Linux
  - Kubernetes
tags:
  - reconnaissance
  - api-access
verified: true
validated: true
---

# curl-access-cadvisor-api

## Command

```bash
curl -k https://$_NODE_IP:4194/
```

## Description

This command sends an unauthenticated HTTPS GET request to the cAdvisor API endpoint on a Kubernetes node to retrieve container resource metrics. Use it during reconnaissance to enumerate running containers and their usage patterns without needing cluster credentials, assuming the port is exposed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_NODE_IP | IP address of the Kubernetes node hosting cAdvisor (e.g., 192.168.1.100) | Yes |
| -k | Insecure mode: skips SSL certificate verification (useful for self-signed certs) | Yes for insecure setups |
| https://... :4194/ | The cAdvisor root endpoint for subcontainer stats | Built-in |

## Examples

### Basic Usage

```bash
curl -k https://192.168.1.100:4194/
```

### With Output Formatting (using jq)

```bash
curl -k https://192.168.1.100:4194/ | jq '.subcontainers'
```

## Expected Output

On success, returns JSON with container details:

```
{"subcontainers":[{...}]}
```

Look for fields like "name", "cpu_usage", and "memory_usage". Errors like "connection refused" indicate firewall blocks or closed ports.

## Related

- [[procedures/Access-Kubernetes-cAdvisor-API]] (procedure that uses this command)
- [[tools/cURL]] (base tool documentation)
