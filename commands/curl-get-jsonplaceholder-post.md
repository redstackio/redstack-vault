---
id: e242b435-81da-48c9-a41e-4f0276d42135
name: curl-get-jsonplaceholder-post
type: command
executor: bash
data: curl -X GET $_URL
output: null
created_at: '2023-04-06T03:55:54.012136+00:00'
updated_at: '2023-04-06T03:55:54.027547+00:00'
platforms:
  - Linux
  - Unix
tags:
  - http
  - curl
  - api
verified: true
validated: true
---

# curl-get-jsonplaceholder-post

## Command

```bash
curl -X GET $_URL
```

## Description

This command performs a GET request to retrieve data from a JSON placeholder API endpoint, used as an example of safe HTTP interaction in the injection procedure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | The API endpoint URL (e.g., https://jsonplaceholder.typicode.com/posts/1) | Yes |
| -X GET | Specify HTTP method as GET | Built-in |

## Examples

### Basic Usage

```bash
curl -X GET https://jsonplaceholder.typicode.com/posts/1
```

### Advanced Usage

```bash
curl -X GET -H "Content-Type: application/json" https://jsonplaceholder.typicode.com/posts/1
```

## Expected Output

JSON response:
```
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere...",
  "body": "quia et suscipit..."
}
```

## Related

- [[procedures/Command-Injection-via-Curl-Arguments]]
