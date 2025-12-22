---
id: cmd-uuid-2
data: dig +short CNAME healthyhackathon.khanacademy.org
tags:
  - dns
  - cname
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.827Z'
verified: false
validated: true
submitted: true
---
# dig-cname-resolve

## Command

```bash
 dig +short CNAME healthyhackathon.khanacademy.org
```

## Description

Resolves CNAME records for a subdomain to identify delegated services like S3, critical for detecting potential takeover points.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+short` | Concise output | No |
| `CNAME` | Specifies CNAME query type | Yes |
| `subdomain` | Target to resolve | Yes |

## Examples

### Basic Usage

```bash
 dig +short CNAME healthyhackathon.khanacademy.org
```

### Advanced Usage

```bash
 dig CNAME hackweek.khanacademy.org
```

## Expected Output

Short CNAME target, e.g., healthyhackathon.khanacademy.org.s3.amazonaws.com.

## Related

- [[Related Procedure: Resolve-and-Analyze-DNS-Records]]
