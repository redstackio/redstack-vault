---
id: ff1db964-cb11-4f77-9d72-63787564d125
type: code
language: cs
verified: false
created_at: '2023-04-06T03:55:59.226462+00:00'
updated_at: '2023-04-06T03:55:59.229403+00:00'
---

# Code Snippet ff1db964

**Language**: cs

```cs
// System.Configuration.Install.AssemblyInstaller
public void set_Path(string value){
    if (value == null){
        this.assembly = null;
    }
    this.assembly = Assembly.LoadFrom(value);
}
```


