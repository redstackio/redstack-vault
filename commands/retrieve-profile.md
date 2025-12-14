---
data: >-
  curl -H 'Cookie: session=your_session'
  'https://larksuite-helpdesk.example.com/profile/view'
tags:
  - xss
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.482Z'
id: 06fe8324-3939-45f5-9758-83802b6db818
verified: false
validated: true
submitted: true
---
# retrieve-profile

## Command

```bash
curl -H 'Cookie: session=your_session' 'https://larksuite-helpdesk.example.com/profile/view'
```

## Description

Retrieves the user profile from the Lark Suite helpdesk to verify if the injected XSS payload in the city field is stored and rendered unsanitized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Cookie: ...'` | Provides authentication session | Yes |

## Examples

### Basic Usage

```bash
curl -H 'Cookie: session=abc' 'https://target.com/profile'
```

### Advanced Usage

```bash
curl -H 'Cookie: session=abc' -s 'https://target.com/profile' | grep -i 'script'
```

## Expected Output

HTML response containing the profile data, with the city field showing the raw injected `<script>` tag if vulnerable.

## Related

- [[Related Procedure|procedures/Inject-Stored-XSS-Payload-in-City-Field]]
