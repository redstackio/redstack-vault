---
type: command
executor: bash
data: snmpwalk -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
platforms:
  - Linux
  - Windows
tags:
  - enumeration
  - snmp
verified: true
validated: true
---

# snmpwalk-enumerate-server

## Command

```bash
snmpwalk -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
```

## Description

This command performs a comprehensive walk of the SNMP Management Information Base (MIB) tree on a target device using the specified community string and SNMP version. It retrieves all accessible objects in a hierarchical format, making it ideal for enumerating system details, network interfaces, and other device information during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c $_COMMUNITY_STRING` | SNMP community string for read access (e.g., 'public' or 'private') | Yes |
| `-v $_VERSION` | SNMP protocol version (1, 2c, or 3) | Yes |
| `$_TARGET_IP` | Target IP address or hostname (defaults to UDP port 161) | Yes |

## Examples

### Basic Usage

```bash
snmpwalk -c public -v 1 10.10.10.10
```

### Advanced Usage

```bash
snmpwalk -c private -v 2c 192.168.1.100 -O e
```

(Omits OIDs with `-O e` for cleaner, value-only output)

## Expected Output

Successful execution returns a series of OID-value pairs representing the MIB tree. Example output:

```
root@kali:~# snmpwalk -c public -v1 10.10.10.10
Created directory: /var/lib/snmp/mib_indexes
SNMPv2-MIB::sysDescr.0 = STRING: Linux Host 4.4.0-75-generic #96~14.04.1-Ubuntu SMP Thu Apr 20 11:06:56 UTC 2017 i686
SNMPv2-MIB::sysObjectID.0 = OID: NET-SNMP-MIB::netSnmpAgentOIDs.10
DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (38145) 0:06:21.45
SNMPv2-MIB::sysContact.0 = STRING: root
...
...
DISMAN-EVENT-MIB::mteEventNotificationObjects."_snmpd".'_linkUp' = STRING: _linkUpDown
DISMAN-EVENT-MIB::mteEventNotificationObjects."_snmpd".'_mteTriggerFailure' = STRING: _triggerFail
DISMAN-EVENT-MIB::mteEventNotificationObjects."_snmpd".'_mteTriggerFalling' = STRING: _triggerFire
DISMAN-EVENT-MIB::mteEventNotificationObjects."_snmpd".'_mteTriggerFired' = STRING: _triggerFire
DISMAN-EVENT-MIB::mteEventNotificationObjects."_snmpd".'_mteTriggerRising' = STRING: _triggerFire
NOTIFICATION-LOG-MIB::nlmConfigGlobalEntryLimit.0 = Gauge32: 1000
NOTIFICATION-LOG-MIB::nlmConfigGlobalAgeOut.0 = Gauge32: 1440 minutes
NOTIFICATION-LOG-MIB::nlmStatsGlobalNotificationsLogged.0 = Counter32: 0 notifications
NOTIFICATION-LOG-MIB::nlmStatsGlobalNotificationsBumped.0 = Counter32: 0 notifications
```

Empty or error output (e.g., 'Timeout: No Response') indicates authentication failure, version mismatch, or firewall blocking UDP/161.

## Related

- [[tools/snmpwalk]]
