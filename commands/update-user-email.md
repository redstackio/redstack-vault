---
id: e62d3278-6215-43ff-af96-55c2c62748a1
name: update-user-email
type: command
executor: bash
data: window.RailsData.user.email = "nonexistingemail@shopify.com";
output: null
created_at: '2025-12-11T06:10:40.635Z'
updated_at: '2025-12-11T06:10:40.635Z'
platforms:
  - Web
tags:
  - javascript
  - email-modification
verified: false
validated: true
submitted: true
---

# update-user-email

## Command

```javascript
window.RailsData.user.email = "nonexistingemail@shopify.com";
```

## Description

Updates the user's email in the Shopify store creation form data to a non-existing email controlled by the attacker, executed in browser console for bypassing restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `email` | Sets the user's email to the specified value | Yes |

## Examples

### Basic Usage

```javascript
window.RailsData.user.email = "attacker@controlled.com";
```

### Advanced Usage

```javascript
window.RailsData.user.email = "nonexistingemail@shopify.com";
```

## Expected Output

The form's user email field is updated client-side, enabling submission without server-side validation errors.

## Related

- [[commands/update-organization-email]]
- [[procedures/Create-Development-Store-with-Modified-Email]]
