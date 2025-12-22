---
type: command
executor: bash
data: 'curl http://s3.amazonaws.com/$_BUCKET_NAME/'
tags:
  - aws
  - s3
  - enumeration
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# curl-check-s3-bucket

## Command

```bash
curl http://s3.amazonaws.com/$_BUCKET_NAME/
```

## Description

Sends an HTTP GET request to check if an Amazon S3 bucket is publicly accessible and lists its contents if open. Use the alternative format curl http://$_BUCKET_NAME.s3.amazonaws.com/ for regional endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BUCKET_NAME | The name of the S3 bucket to check (e.g., 'my-open-bucket') | Yes |

## Examples

### Basic Usage

```bash
curl http://s3.amazonaws.com/example-bucket/
```

### Advanced Usage

```bash
curl -I http://s3.amazonaws.com/example-bucket/  # Head request for quick status check
```

## Expected Output

If the bucket is open and public:
```
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Name>example-bucket</Name>
  <Prefix></Prefix>
  <Marker></Marker>
  <MaxKeys>1000</MaxKeys>
  <IsTruncated>false</IsTruncated>
  <Contents>
    <Key>file.txt</Key>
    <LastModified>2023-01-01T00:00:00.000Z</LastModified>
    <ETag>"abc123"</ETag>
    <Size>1024</Size>
  </Contents>
</ListBucketResult>
```
If private: HTTP 403 Forbidden error.

## Related

- [[procedures/Enumerate-Open-Amazon-S3-Buckets]]
