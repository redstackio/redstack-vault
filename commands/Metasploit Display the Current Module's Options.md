---
id: 82638aec-9769-44ae-8945-2eae53a02715
name: Metasploit Display the Current Module's Options
type: command
executor: metasploit
data: show options
output: "msf5 exploit(windows/smb/ms17_010_eternalblue) > show options\n\nModule options\
  \ (exploit/windows/smb/ms17_010_eternalblue):\n\n   Name           Current Setting\
  \  Required  Description\n   ----           ---------------  --------  -----------\n\
  \   RHOSTS                          yes       The target host(s), range CIDR identifier,\
  \ or hosts file with syntax 'file:<path>'\n   RPORT          445              yes\
  \       The target port (TCP)\n   SMBDomain      .                no        (Optional)\
  \ The Windows domain to use for authentication\n   SMBPass                     \
  \    no        (Optional) The password for the specified username\n   SMBUser  \
  \                       no        (Optional) The username to authenticate as\n \
  \  VERIFY_ARCH    true             yes       Check if remote architecture matches\
  \ exploit Target.\n   VERIFY_TARGET  true             yes       Check if remote\
  \ OS matches exploit Target.\n..."
created_at: '2020-07-08T22:56:24.136792+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Display the Current Module's Options

```metasploit
show options
```

## Expected Output

```
msf5 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT          445              yes       The target port (TCP)
   SMBDomain      .                no        (Optional) The Windows domain to use for authentication
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target.
...
```
