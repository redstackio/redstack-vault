---
id: c64597d3-eb44-4f2e-a0a7-26b90fa1e47a
name: update-organization-email
type: command
executor: bash
data: >-
  window.RailsData.current_organization.business_email =
  "nonexistingemail@shopify.com";
output: null
created_at: '2025-12-11T06:10:40.638Z'
updated_at: '2025-12-11T06:10:40.638Z'
platforms:
  - Web
tags:
  - javascript
  - email-modification
verified: false
validated: true
submitted: true
---

# update-organization-email

## Command

```javascript
window.RailsData.current_organization.business_email = "nonexistingemail@shopify.com";
```

## Description

Updates the organization's business email in the Shopify store creation form data to a non-existing email controlled by the attacker, used in browser console to bypass read-only fields.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `business_email` | Sets the organization's email to the specified value | Yes |

## Examples

### Basic Usage

```javascript
window.RailsData.current_organization.business_email = "attacker@controlled.com";
```

### Advanced Usage

```javascript
window.RailsData.current_organization.business_email = "nonexistingemail@shopify.com";
```

## Expected Output

The form's business email field is updated in the client-side data, allowing submission with the modified value.

## Related

- [[commands/update-user-email]]
- [[procedures/Create-Development-Store-with-Modified-Email]]
