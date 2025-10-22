---
id: 18f24bcf-d43d-4261-8d62-03ea540a7921
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.982399+00:00'
updated_at: '2023-04-10T20:19:35.334911+00:00'
---

# Code Snippet 18f24bcf

**Language**: Powershell

```powershell
# AAD Internals - Making your device compliant
# Get an access token for AAD join and save to cache
Get-AADIntAccessTokenForAADJoin -SaveToCache
# Join the device to Azure AD
Join-AADIntDeviceToAzureAD -DeviceName "SixByFour" -DeviceType "Commodore" -OSVersion "C64"
# Marking device compliant - option 1: Registering device to Intune
# Get an access token for Intune MDM and save to cache (prompts for credentials)
Get-AADIntAccessTokenForIntuneMDM -PfxFileName .\d03994c9-24f8-41ba-a156-1805998d6dc7.pfx -SaveToCache 
# Join the device to Intune
Join-AADIntDeviceToIntune -DeviceName "SixByFour"
# Start the call back
Start-AADIntDeviceIntuneCallback -PfxFileName .\d03994c9-24f8-41ba-a156-1805998d6dc7-MDM.pfx -DeviceName "SixByFour"
```
