---
data: dig studio.redditinc.com
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.040Z'
id: 8008ac5c-afe4-4f16-8732-41fef3e2211f
verified: false
validated: true
submitted: true
---
---

# dig-studio-redditinc-cname

## Command

```bash
dig studio.redditinc.com
```

## Description

Performs a DNS lookup to resolve the target domain and retrieve its CNAME record, used in reconnaissance to identify CloudFront distributions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| studio.redditinc.com | Target domain to query | Yes |

## Examples

### Basic Usage

```bash
dig studio.redditinc.com
```

### Advanced Usage

```bash
dig +short studio.redditinc.com
```

## Expected Output

DNS response with ANSWER SECTION showing CNAME d326d3e45wj426.cloudfront.net.

## Related

- [[commands/host-ns-s3-endpoint]]
- [[procedures/DNS-Enumeration-to-Identify-S3-Bucket]]
