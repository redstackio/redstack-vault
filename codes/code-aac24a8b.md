---
id: aac24a8b-ba35-434a-9a6a-8a02381d6fa6
type: code
language: PHP
verified: false
created_at: '2023-04-06T03:55:58.434553+00:00'
updated_at: '2023-04-10T20:22:20.133324+00:00'
---

# Code Snippet aac24a8b

**Language**: PHP

```php
// create new Phar
$phar = new Phar('test.phar');
$phar->startBuffering();
$phar->addFromString('test.txt', 'text');
$phar->setStub('<?php __HALT_COMPILER(); ? >');

// add object of any class as meta data
class AnyClass {}
$object = new AnyClass;
$object->data = 'rips';
$phar->setMetadata($object);
$phar->stopBuffering();
```
