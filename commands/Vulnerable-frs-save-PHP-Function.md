---
id: cmd-uuid-4
data: |-
  function frs_save() {
   global $wpdb;
   unset($_POST['action']);
   $id = htmlspecialchars($_POST['post_id']);
   // ... (later)
   $slide_type = htmlspecialchars($_POST['slide_type']);
   $title = htmlspecialchars($_POST['title']);
   $content = $_POST['content'];
   $my_post = array(
    'post_title' => $title,
    'post_content' => $content,
    'ID'=>$id
   );
   wp_update_post( $my_post );
  }
tags:
  - csrf
  - vulnerable
  - code
type: command
output: Database update via wp_update_post; no error if valid ID
executor: php
platforms:
  - Web
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.535Z'
verified: false
validated: true
submitted: true
---
# Vulnerable frs_save PHP Function

## Command

```php
function frs_save() {
 global $wpdb;
 unset($_POST['action']);
 $id = htmlspecialchars($_POST['post_id']);
 // ... (later)
 $slide_type = htmlspecialchars($_POST['slide_type']);
 $title = htmlspecialchars($_POST['title']);
 $content = $_POST['content'];
 $my_post = array(
  'post_title' => $title,
  'post_content' => $content,
  'ID'=>$id
 );
 wp_update_post( $my_post );
}
```

## Description

Plugin's AJAX handler code showing root cause: no CSRF check, raw $_POST for content leading to unsanitized updates.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| post_id | ID to update (htmlspecialchars) | Yes |
| title | Post title (htmlspecialchars) | Yes |
| content | Raw content, vulnerable to JS | Yes |
| slide_type | Slide type (htmlspecialchars) | No |

## Examples

### Basic Usage

This is source code; execute via AJAX call.

## Expected Output

Post updated in database.

## Related

- [[Related Procedure: Identify-Vulnerable-AJAX-Endpoints-in-WordPress-Plugin]]
