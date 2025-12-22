---
type: command
executor: powershell
data: (user.otherMails -any (_ -contains "vendor")) -and (user.userType -eq "guest")
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Azure
tags:
  - persistence
  - azure-ad
verified: true
validated: true
---

# Create-Azure-Dynamic-Group-Rule-for-Guest-Vendors

## Command

```powershell
(user.otherMails -any (_ -contains "vendor")) -and (user.userType -eq "guest")
```

## Description

This is a dynamic membership rule expression for Azure AD groups. It automatically adds guest users whose alternate emails contain 'vendor' to the group. Use it when creating or updating dynamic groups via PowerShell (New-AzureADMSGroup) or Azure portal to enable attribute-based access, which attackers can abuse by inviting controlled guest accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| user.otherMails -any (_ -contains "vendor") | Matches any alternate email containing 'vendor' | Yes |
| user.userType -eq "guest" | Ensures the user is a guest type | Yes |
| -and | Logical operator combining conditions | Yes |

## Examples

### Basic Usage

Apply in group creation:
```powershell
New-AzureADMSGroup -DisplayName "Vendor Group" -Description "Dynamic vendor access" -GroupTypes "DynamicMembership" -MembershipRule "(user.otherMails -any (_ -contains \"vendor\")) -and (user.userType -eq \"guest\")" -MembershipRuleProcessingState "On"
```

### Advanced Usage

Combine with department filter:
```powershell
(user.otherMails -any (_ -contains "vendor")) -and (user.userType -eq "guest") -and (user.department -eq "IT")
```

## Expected Output

When applied to a group, no direct output from the expression itself. Verify with `Get-AzureADMSGroup -Id <GroupId>` showing MembershipRule populated. After inviting a matching guest, `Get-AzureADMSGroupMember` lists the new member.

## Related

- [[procedures/Abuse-Azure-Dynamic-Group-Membership-and-Guest-Vendor-Rules]]
- [[commands/Get-Azure-ADMS-Groups-Filtered-by-Dynamic-Membership]]
