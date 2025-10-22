---
id: 27a78800-080e-48af-acea-63ed5334d53a
name: Service Stop
type: technique
mitre_id: T1489
mitre_url: null
created_at: '2019-08-28T21:17:43.194671+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
procedures:
- '[[Abusing DNSAdmins Group to Change DNS Service DLL]]'
---

# Service Stop

**MITRE ID**: T1489

## Description

Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment.[1][2] Adversaries may accomplish this by disabling individual services of high importance to an organization, such as MSExchangeIS, which will make Exchange content inaccessible [2]. In some cases, adversaries may stop or disable many or all services to render systems unusable.[1] Services may not allow for modification of their data stores while running. Adversaries may stop services in order to conduct Data Destruction or Data Encrypted for Impact on the data stores of services like Exchange and SQL Server.[3]

# Detection

Monitor processes and command-line arguments to see if critical processes are terminated or stop running.

Monitor Registry edits for modifications to services and startup programs that correspond to services of high importance. Look for changes to service Registry entries that do not correlate with known software, patch cycles, etc. Service information is stored in the Registry at HKLM\SYSTEM\CurrentControlSet\Services.

Alterations to the service binary path or the service startup type changed to disabled may be suspicious.

Remote access tools with built-in features may interact directly with the Windows API to perform these functions outside of typical system utilities. For example, ChangeServiceConfigW may be used by an adversary to prevent services from starting.[1]

# Mitigation

Ensure proper process, registry, and file permissions are in place to inhibit adversaries from disabling or interfering with critical services. Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service configurations. Harden systems used to serve critical network, business, and communications functions. Operate intrusion detection, analysis, and response systems on a separate network from the production environment to lessen the chances that an adversary can see and interfere with critical response functions.

# Footnotes

[1] Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.

[2] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[3] Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.

[4] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved March 2, 2016.

[5] Berry, A., Homan, J., and Eitzman, R. (2017, May 23). WannaCry Malware Profile. Retrieved March 15, 2019.

## Defense

Ensure proper process, registry, and file permissions are in place to inhibit adversaries from disabling or interfering with critical services. Limit privileges of user accounts and groups so that only authorized administrators can interact with service c

## Tactics

- [[Impact|TA0040 - Impact]]

## Related Procedures (1)

- [[Abusing DNSAdmins Group to Change DNS Service DLL]]
