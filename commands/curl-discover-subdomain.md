---
id: cmd-uuid-1
data: 'curl https://www█████████.affirm.com'
tags:
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.715Z'
verified: false
validated: true
submitted: true
---
# curl-discover-subdomain

## Command

```bash
curl https://www█████████.affirm.com
```

## Description

Sends a GET request to the subdomain to discover if it points to a non-existent S3 bucket, revealing the bucket name via error response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target subdomain URL | Yes |

## Examples

### Basic Usage

```bash
curl https://www█████████.affirm.com
```

### Advanced Usage

```bash
curl -v https://www█████████.affirm.com
```

## Expected Output

XML response with PermanentRedirect error, including <Code>PermanentRedirect</Code>, <Message>The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.</Message>, <Endpoint>s3.amazonaws.com</Endpoint>, <Bucket>affirm-prod-www-cms█████████</Bucket>

## Related

- [[Related Procedure|procedures/Discover-Dangling-S3-Bucket-Reference]]
