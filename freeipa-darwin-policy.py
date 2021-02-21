# There is also a JSON file with the same datatypes for easier visualisation
# What is needed to be filled in:
#        1) The Search Base
#        2) The Realm name
#        3) The friendly name for the IPA Domain
#        4) The friendly name for the current IPA replica (hostnamectl --pretty)
#        5) The KDCs and KADMs (hostname and IP)
#        6) The LDAP Replicas (hostname and IP)
#
# Append the BASE DN of the IPA Server to the following entries:
#    * macosODConfig."Record Type Map"."Native Map"."Search Base"
#    * macosODConfig."Template Search Base Suffix"
#    * macosODConfig."Map Search Base"
# Set the IP Address of this IPA Server in macosODConfig."Server"
# Set a friendly name (such as the Kerberos Realm Name) in macosODConfig."UI Name"
# 
# macosODConfig currently supports the following Record Type Maps:
#    * Users
#    * Groups
#    * Certification Authorities
#    * Computers
#    * Machines
#    * Computer Groups
#    * Config
#    * Automount Map
#    * Automount
# 
# macosODPolicy is a selfexplanatory Directory usage policy.
#  It basically enforces directory binding using the Computer Account,
#  and the usage of SSL and Kerberos across the board in relationship
#  with the LDAP Server. It furthermore disables the CRAM-MD5 and
#  DIGEST-MD5 SASL methods that we can't and shouldn't provide.
# 
# macosKerberosClient is the configuration for the Kerberos realm.
#  It includes the actual realm and mappings, as well as the KADMs
#  and KDCs in both FQDN and IP address format.
# 
# macosLDAPReplicas is the configuration for the LDAP replicas.
#  It mentions which are read-only and which are read-write and which
#  is the master replica. In a FreeIPA multi-master configuration it is
#  pointless so we choose ourselves as the master and set the other
#  replicas as read-write. As with the KerberosClient, we also provide
#  the IP(v4) addresses of the LDAP servers in case of name resolution
#  failure, but we are unsure of the codepath in the OpenDirectory client.
# 
# All this information is cached on the client computer and is checked
#  again for updates at every new OD session.
#
# The formatting is very heavy for readability. Please keep it this way
# specifically in this file.

macosODConfig = {
    'Attribute Type Map': [{'Native Map': ['cn'], 'Standard Name': 'dsAttrTypeStandard=RecordName'},
                           {'Native Map': ['createTimestamp'], 'Standard Name': 'dsAttrTypeStandard=CreationTimestamp'},
                           {'Native Map': ['modifyTimestamp'],
                            'Standard Name': 'dsAttrTypeStandard=ModificationTimestamp'}],

    'Record Type Map': [
        {'Standard Name': 'dsRecTypeStandard=Users',
         'Attribute Type Map': [{'Native Map': ['uid', 'cn'], 'Standard Name': 'dsAttrTypeStandard=RecordName'},
                                {'Native Map': ['cn'], 'Standard Name': 'dsAttrTypeStandard=RealName'},
                                {'Native Map': ['uidNumber'], 'Standard Name': 'dsAttrTypeStandard=UniqueID'},
                                {'Native Map': ['gidNumber'], 'Standard Name': 'dsAttrTypeStandard=PrimaryGroupID'},
                                {'Native Map': ['homeDirectory'],
                                 'Standard Name': 'dsAttrTypeStandard=NFSHomeDirectory'},
                                {'Native Map': ['apple-user-homeurl'],
                                 'Standard Name': 'dsAttrTypeStandard=HomeDirectory'},
                                {'Native Map': ['apple-user-homequota'],
                                 'Standard Name': 'dsAttrTypeStandard=HomeDirectoryQuota'},
                                {'Native Map': ['apple-user-homesoftquota'],
                                 'Standard Name': 'dsAttrTypeStandard=HomeDirectorySoftQuota'},
                                {'Native Map': ['apple-user-mailattribute'],
                                 'Standard Name': 'dsAttrTypeStandard=MailAttribute'},
                                {'Native Map': ['apple-user-printattribute'],
                                 'Standard Name': 'dsAttrTypeStandard=PrintServiceUserData'},
                                {'Native Map': ['apple-mcxflags'], 'Standard Name': 'dsAttrTypeStandard=MCXFlags'},
                                {'Native Map': ['apple-mcxsettings'],
                                 'Standard Name': 'dsAttrTypeStandard=MCXSettings'},
                                {'Native Map': ['apple-user-adminlimits'],
                                 'Standard Name': 'dsAttrTypeStandard=AdminLimits'},
                                {'Native Map': ['userPassword'], 'Standard Name': 'dsAttrTypeStandard=Password'},
                                {'Native Map': ['apple-user-picture'], 'Standard Name': 'dsAttrTypeStandard=Picture'},
                                {'Native Map': ['jpegPhoto'], 'Standard Name': 'dsAttrTypeStandard=JPEGPhoto'},
                                {'Native Map': ['loginShell'], 'Standard Name': 'dsAttrTypeStandard=UserShell'},
                                {'Native Map': ['description'], 'Standard Name': 'dsAttrTypeStandard=Comment'},
                                {'Native Map': ['shadowLastChange'], 'Standard Name': 'dsAttrTypeStandard=Change'},
                                {'Native Map': ['shadowExpire'], 'Standard Name': 'dsAttrTypeStandard=Expire'},
                                {'Native Map': ['authAuthority'],
                                 'Standard Name': 'dsAttrTypeStandard=AuthenticationAuthority'},
                                {'Native Map': ['apple-user-authenticationhint'],
                                 'Standard Name': 'dsAttrTypeStandard=AuthenticationHint'},
                                {'Native Map': ['apple-user-passwordpolicy'],
                                 'Standard Name': 'dsAttrTypeStandard=PasswordPolicyOptions'},
                                {'Native Map': ['acctFlags'], 'Standard Name': 'dsAttrTypeStandard=SMBAccountFlags'},
                                {'Native Map': ['pwdLastSet'],
                                 'Standard Name': 'dsAttrTypeStandard=SMBPasswordLastSet'},
                                {'Native Map': ['logonTime'], 'Standard Name': 'dsAttrTypeStandard=SMBLogonTime'},
                                {'Native Map': ['logoffTime'], 'Standard Name': 'dsAttrTypeStandard=SMBLogoffTime'},
                                {'Native Map': ['kickoffTime'], 'Standard Name': 'dsAttrTypeStandard=SMBKickoffTime'},
                                {'Native Map': ['homeDrive'], 'Standard Name': 'dsAttrTypeStandard=SMBHomeDrive'},
                                {'Native Map': ['scriptPath'], 'Standard Name': 'dsAttrTypeStandard=SMBScriptPath'},
                                {'Native Map': ['profilePath'], 'Standard Name': 'dsAttrTypeStandard=SMBProfilePath'},
                                {'Native Map': ['userWorkstations'],
                                 'Standard Name': 'dsAttrTypeStandard=SMBUserWorkstations'},
                                {'Native Map': ['smbHome'], 'Standard Name': 'dsAttrTypeStandard=SMBHome'},
                                {'Native Map': ['rid'], 'Standard Name': 'dsAttrTypeStandard=SMBRID'},
                                {'Native Map': ['primaryGroupID'], 'Standard Name': 'dsAttrTypeStandard=SMBGroupRID'},
                                {'Native Map': ['sambaSID'], 'Standard Name': 'dsAttrTypeStandard=SMBSID'},
                                {'Native Map': ['sambaPrimaryGroupSID'],
                                 'Standard Name': 'dsAttrTypeStandard=SMBPrimaryGroupSID'},
                                {'Native Map': ['apple-keyword'], 'Standard Name': 'dsAttrTypeStandard=Keywords'},
                                {'Native Map': ['apple-generateduid'],
                                 'Standard Name': 'dsAttrTypeStandard=GeneratedUID'},
                                {'Native Map': ['sn'], 'Standard Name': 'dsAttrTypeStandard=LastName'},
                                {'Native Map': ['givenName'], 'Standard Name': 'dsAttrTypeStandard=FirstName'},
                                {'Native Map': ['mail'], 'Standard Name': 'dsAttrTypeStandard=EMailAddress'},
                                {'Native Map': ['apple-imhandle'], 'Standard Name': 'dsAttrTypeStandard=IMHandle'},
                                {'Native Map': ['labeledURI'], 'Standard Name': 'dsAttrTypeStandard=URL'},
                                {'Native Map': ['apple-webloguri'], 'Standard Name': 'dsAttrTypeStandard=WeblogURI'},
                                {'Native Map': ['telephoneNumber'], 'Standard Name': 'dsAttrTypeStandard=PhoneNumber'},
                                {'Native Map': ['facsimileTelephoneNumber'],
                                 'Standard Name': 'dsAttrTypeStandard=FAXNumber'},
                                {'Native Map': ['mobile'], 'Standard Name': 'dsAttrTypeStandard=MobileNumber'},
                                {'Native Map': ['pager'], 'Standard Name': 'dsAttrTypeStandard=PagerNumber'},
                                {'Native Map': ['street'], 'Standard Name': 'dsAttrTypeStandard=AddressLine1'},
                                {'Native Map': ['postalAddress'], 'Standard Name': 'dsAttrTypeStandard=PostalAddress'},
                                {'Native Map': ['street'], 'Standard Name': 'dsAttrTypeStandard=Street'},
                                {'Native Map': ['l'], 'Standard Name': 'dsAttrTypeStandard=City'},
                                {'Native Map': ['st'], 'Standard Name': 'dsAttrTypeStandard=State'},
                                {'Native Map': ['postalCode'], 'Standard Name': 'dsAttrTypeStandard=PostalCode'},
                                {'Native Map': ['c'], 'Standard Name': 'dsAttrTypeStandard=Country'},
                                {'Native Map': ['homePhone'], 'Standard Name': 'dsAttrTypeStandard=HomePhoneNumber'},
                                {'Native Map': ['o'], 'Standard Name': 'dsAttrTypeStandard=OrganizationName'},
                                {'Native Map': ['departmentNumber'], 'Standard Name': 'dsAttrTypeStandard=Department'},
                                {'Native Map': ['title'], 'Standard Name': 'dsAttrTypeStandard=JobTitle'},
                                {'Native Map': ['buildingName'], 'Standard Name': 'dsAttrTypeStandard=Building'},
                                {'Native Map': ['userCertificate;binary'],
                                 'Standard Name': 'dsAttrTypeStandard=UserCertificate'},
                                {'Native Map': ['userPKCS12'], 'Standard Name': 'dsAttrTypeStandard=UserPKCS12Data'},
                                {'Native Map': ['userSMIMECertificate'],
                                 'Standard Name': 'dsAttrTypeStandard=UserSMIMECertificate'},
                                {'Native Map': ['apple-mapcoordinates'],
                                 'Standard Name': 'dsAttrTypeStandard=MapCoordinates'},
                                {'Native Map': ['apple-relationships'],
                                 'Standard Name': 'dsAttrTypeStandard=Relationships'},
                                {'Native Map': ['apple-postaladdresses'],
                                 'Standard Name': 'dsAttrTypeStandard=PostalAddressContacts'},
                                {'Native Map': ['apple-emailcontacts'],
                                 'Standard Name': 'dsAttrTypeStandard=EMailContacts'},
                                {'Native Map': ['apple-phonecontacts'],
                                 'Standard Name': 'dsAttrTypeStandard=PhoneContacts'},
                                {'Native Map': ['apple-birthday'], 'Standard Name': 'dsAttrTypeStandard=Birthday'},
                                {'Native Map': ['apple-company'], 'Standard Name': 'dsAttrTypeStandard=Company'},
                                {'Native Map': ['apple-serviceslocator'],
                                 'Standard Name': 'dsAttrTypeStandard=ServicesLocator'},
                                {'Native Map': ['apple-mapuri'], 'Standard Name': 'dsAttrTypeStandard=MapURI'},
                                {'Native Map': ['apple-mapguid'], 'Standard Name': 'dsAttrTypeStandard=MapGUID'},
                                {'Native Map': ['apple-organizationinfo'],
                                 'Standard Name': 'dsAttrTypeStandard=OrganizationInfo'},
                                {'Native Map': ['apple-nickname'], 'Standard Name': 'dsAttrTypeStandard=NickName'},
                                {'Native Map': ['apple-namesuffix'], 'Standard Name': 'dsAttrTypeStandard=NameSuffix'},
                                {'Native Map': ['apple-xmlplist'], 'Standard Name': 'dsAttrTypeStandard=XMLPlist'},
                                {'Native Map': ['altSecurityIdentities'],
                                 'Standard Name': 'dsAttrTypeStandard=AltSecurityIdentities'}],
         'Native Map': [{'Group Object Classes': 'AND',
                         'Object Classes': ['posixAccount', 'ipaObject', 'person'],
                         'Search Base': 'cn=users,cn=accounts'}]},

        {'Standard Name': 'dsRecTypeStandard=Groups',
         'Attribute Type Map': [{'Native Map': ['memberUid'], 'Standard Name': 'dsAttrTypeStandard=GroupMembership'},
                                {'Native Map': ['memberUid'], 'Standard Name': 'dsAttrTypeStandard=Member'},
                                {'Native Map': ['gidNumber'], 'Standard Name': 'dsAttrTypeStandard=PrimaryGroupID'},
                                {'Native Map': ['memberOf'], 'Standard Name': 'dsAttrTypeStandard=NestedGroups'},
                                {'Native Map': ['description'], 'Standard Name': 'dsAttrTypeStandard=RealName'},
                                {'Native Map': ['description'], 'Standard Name': 'dsAttrTypeStandard=Comment'},
                                {'Native Map': ['mail'], 'Standard Name': 'dsAttrTypeStandard=EMailAddress'},
                                {'Native Map': ['jpegPhoto'], 'Standard Name': 'dsAttrTypeStandard=JPEGPhoto'},
                                {'Native Map': ['ipaUniqueId'], 'Standard Name': 'dsAttrTypeStandard=GeneratedUID'},
                                {'Native Map': ['rid'], 'Standard Name': 'dsAttrTypeStandard=SMBRID'},
                                {'Native Map': ['primaryGroupID'], 'Standard Name': 'dsAttrTypeStandard=SMBGroupRID'},
                                {'Native Map': ['sambaSID'], 'Standard Name': 'dsAttrTypeStandard=SMBSID'},
                                {'Native Map': ['apple-xmlplist'], 'Standard Name': 'dsAttrTypeStandard=XMLPlist'}],
         'Native Map': [{'Group Object Classes': 'AND',
                         'Object Classes': ['posixGroup', 'ipaUserGroup'],
                         'Search Base': 'cn=groups,cn=accounts'}]},

        {'Standard Name': 'dsRecTypeStandard=CertificateAuthorities',
         'Attribute Type Map': [{'Native Map': ['cn'], 'Standard Name': 'dsAttrTypeStandard=RecordName'},
                                {'Native Map': ['authorityRevocationList;binary'],
                                 'Standard Name': 'dsAttrTypeStandard=AuthorityRevocationList'},
                                {'Native Map': ['certificateRevocationList;binary'],
                                 'Standard Name': 'dsAttrTypeStandard=CertificateRevocationList'},
                                {'Native Map': ['cACertificate;binary'],
                                 'Standard Name': 'dsAttrTypeStandard=CACertificate'},
                                {'Native Map': ['crossCertificatePair;binary'],
                                 'Standard Name': 'dsAttrTypeStandard=CrossCertificatePair'}],
         'Native Map': [{'Group Object Classes': 'AND',
                         'Object Classes': ['pkiCA'],
                         'Search Base': 'cn=CAcert,cn=ipa,cn=etc'}]},

        {'Standard Name': 'dsRecTypeStandard=Computers',
         'Attribute Type Map': [{'Native Map': ['fqdn'], 'Standard Name': 'dsAttrTypeStandard=RecordName'},
                                {'Native Map': ['serialNumber'], 'Standard Name': 'dsAttrTypeStandard=HardwareUUID'},
                                {'Native Map': ['serverHostName'], 'Standard Name': 'dsAttrTypeStandard=RealName'},
                                {'Native Map': ['description'], 'Standard Name': 'dsAttrTypeStandard=Comment'},
                                {'Native Map': ['ipHostNumber'], 'Standard Name': 'dsAttrTypeStandard=IPAddress'},
                                {'Native Map': ['ipHostNumber'], 'Standard Name': 'dsAttrTypeStandard=IPv6Address'},
                                {'Native Map': ['macAddress'], 'Standard Name': 'dsAttrTypeStandard=ENetAddress'},
                                {'Native Map': ['uidNumber'], 'Standard Name': 'dsAttrTypeStandard=UniqueID'},
                                {'Native Map': ['gidNumber'], 'Standard Name': 'dsAttrTypeStandard=PrimaryGroupID'},
                                {'Native Map': ['authAuthority'],
                                 'Standard Name': 'dsAttrTypeStandard=AuthenticationAuthority'},
                                {'Native Map': ['ipaUniqueId'], 'Standard Name': 'dsAttrTypeStandard=GeneratedUID'},
                                {'Native Map': ['acctFlags'], 'Standard Name': 'dsAttrTypeStandard=SMBAccountFlags'},
                                {'Native Map': ['pwdLastSet'],
                                 'Standard Name': 'dsAttrTypeStandard=SMBPasswordLastSet'},
                                {'Native Map': ['logonTime'], 'Standard Name': 'dsAttrTypeStandard=SMBLogonTime'},
                                {'Native Map': ['logoffTime'], 'Standard Name': 'dsAttrTypeStandard=SMBLogoffTime'},
                                {'Native Map': ['kickoffTime'], 'Standard Name': 'dsAttrTypeStandard=SMBKickoffTime'},
                                {'Native Map': ['rid'], 'Standard Name': 'dsAttrTypeStandard=SMBRID'},
                                {'Native Map': ['primaryGroupID'], 'Standard Name': 'dsAttrTypeStandard=SMBGroupRID'},
                                {'Native Map': ['sambaSID'], 'Standard Name': 'dsAttrTypeStandard=SMBSID'},
                                {'Native Map': ['sambaPrimaryGroupSID'],
                                 'Standard Name': 'dsAttrTypeStandard=SMBPrimaryGroupSID'},
                                {'Native Map': ['apple-xmlplist'], 'Standard Name': 'dsAttrTypeStandard=XMLPlist'}],
         'Native Map': [{'Group Object Classes': 'OR',
                         'Object Classes': ['ipaHost', 'krbPrincipal', 'krbPrincipalAux', 'apple-user',
                                            'ieee802Device'],
                         'Search Base': 'cn=computers,cn=accounts'}]},

        {'Standard Name': 'dsRecTypeStandard=Machines',
         'Attribute Type Map': [{'Native Map': ['fqdn'], 'Standard Name': 'dsAttrTypeStandard=RecordName'},
                                {'Native Map': ['serialNumber'], 'Standard Name': 'dsAttrTypeStandard=HardwareUUID'},
                                {'Native Map': ['serverHostName'], 'Standard Name': 'dsAttrTypeStandard=RealName'},
                                {'Native Map': ['description'], 'Standard Name': 'dsAttrTypeStandard=Comment'},
                                {'Native Map': ['ipHostNumber'], 'Standard Name': 'dsAttrTypeStandard=IPAddress'},
                                {'Native Map': ['ipHostNumber'], 'Standard Name': 'dsAttrTypeStandard=IPv6Address'},
                                {'Native Map': ['macAddress'], 'Standard Name': 'dsAttrTypeStandard=ENetAddress'},
                                {'Native Map': ['uidNumber'], 'Standard Name': 'dsAttrTypeStandard=UniqueID'},
                                {'Native Map': ['gidNumber'], 'Standard Name': 'dsAttrTypeStandard=PrimaryGroupID'},
                                {'Native Map': ['authAuthority'],
                                 'Standard Name': 'dsAttrTypeStandard=AuthenticationAuthority'},
                                {'Native Map': ['ipaUniqueId'], 'Standard Name': 'dsAttrTypeStandard=GeneratedUID'},
                                {'Native Map': ['acctFlags'], 'Standard Name': 'dsAttrTypeStandard=SMBAccountFlags'},
                                {'Native Map': ['pwdLastSet'],
                                 'Standard Name': 'dsAttrTypeStandard=SMBPasswordLastSet'},
                                {'Native Map': ['logonTime'], 'Standard Name': 'dsAttrTypeStandard=SMBLogonTime'},
                                {'Native Map': ['logoffTime'], 'Standard Name': 'dsAttrTypeStandard=SMBLogoffTime'},
                                {'Native Map': ['kickoffTime'], 'Standard Name': 'dsAttrTypeStandard=SMBKickoffTime'},
                                {'Native Map': ['rid'], 'Standard Name': 'dsAttrTypeStandard=SMBRID'},
                                {'Native Map': ['primaryGroupID'], 'Standard Name': 'dsAttrTypeStandard=SMBGroupRID'},
                                {'Native Map': ['sambaSID'], 'Standard Name': 'dsAttrTypeStandard=SMBSID'},
                                {'Native Map': ['sambaPrimaryGroupSID'],
                                 'Standard Name': 'dsAttrTypeStandard=SMBPrimaryGroupSID'},
                                {'Native Map': ['apple-xmlplist'], 'Standard Name': 'dsAttrTypeStandard=XMLPlist'}],
         'Native Map': [{'Group Object Classes': 'OR',
                         'Object Classes': ['ipaHost', 'krbPrincipal', 'ieee802Device'],
                         'Search Base': 'cn=computers,cn=accounts'}]},

        {'Standard Name': 'dsRecTypeStandard=ComputerGroups',
         'Attribute Type Map': [{'Native Map': ['member'], 'Standard Name': 'dsAttrTypeStandard=GroupMembership'},
                                {'Native Map': ['member'], 'Standard Name': 'dsAttrTypeStandard=Member'},
                                {'Native Map': ['memberOf'], 'Standard Name': 'dsAttrTypeStandard=NestedGroups'},
                                {'Native Map': ['description'], 'Standard Name': 'dsAttrTypeStandard=RealName'},
                                {'Native Map': ['description'], 'Standard Name': 'dsAttrTypeStandard=Comment'},
                                {'Native Map': ['mail'], 'Standard Name': 'dsAttrTypeStandard=EMailAddress'},
                                {'Native Map': ['jpegPhoto'], 'Standard Name': 'dsAttrTypeStandard=JPEGPhoto'},
                                {'Native Map': ['ipaUniqueID'], 'Standard Name': 'dsAttrTypeStandard=GeneratedUID'},
                                {'Native Map': ['apple-xmlplist'], 'Standard Name': 'dsAttrTypeStandard=XMLPlist'}],
         'Native Map': [{'Group Object Classes': 'AND',
                         'Object Classes': ['ipaHostGroup'],
                         'Search Base': 'cn=hostgroups,cn=accounts'}]},

        {'Standard Name': 'dsRecTypeStandard=Config',
         'Attribute Type Map': [{'Native Map': ['cn', 'ou'], 'Standard Name': 'dsAttrTypeStandard=RecordName'},
                                {'Native Map': ['apple-config-realname'],
                                 'Standard Name': 'dsAttrTypeStandard=RealName'},
                                {'Native Map': ['description'], 'Standard Name': 'dsAttrTypeStandard=Comment'},
                                {'Native Map': ['apple-data-stamp'], 'Standard Name': 'dsAttrTypeStandard=DataStamp'},
                                {'Native Map': ['apple-kdc-authkey'], 'Standard Name': 'dsAttrTypeStandard=KDCAuthKey'},
                                {'Native Map': ['apple-kdc-configdata'],
                                 'Standard Name': 'dsAttrTypeStandard=KDCConfigData'},
                                {'Native Map': ['apple-keyword'], 'Standard Name': 'dsAttrTypeStandard=Keywords'},
                                {'Native Map': ['apple-ldap-replica'],
                                 'Standard Name': 'dsAttrTypeStandard=LDAPReadReplicas'},
                                {'Native Map': ['apple-ldap-writable-replica'],
                                 'Standard Name': 'dsAttrTypeStandard=LDAPWriteReplicas'},
                                {'Native Map': ['apple-password-server-list'],
                                 'Standard Name': 'dsAttrTypeStandard=PasswordServerList'},
                                {'Native Map': ['apple-password-server-location'],
                                 'Standard Name': 'dsAttrTypeStandard=PasswordServerLocation'},
                                {'Native Map': ['ttl'], 'Standard Name': 'dsAttrTypeStandard=TimeToLive'},
                                {'Native Map': ['apple-xmlplist'], 'Standard Name': 'dsAttrTypeStandard=XMLPlist'}],
         'Native Map': [{'Group Object Classes': 'OR',
                         'Object Classes': ['apple-configuration', 'organizationalUnit'],
                         'Search Base': 'cn=config'}]},

        {'Standard Name': 'dsRecTypeStandard=AutomountMap',
         'Attribute Type Map': [{'Native Map': ['description'], 'Standard Name': 'dsAttrTypeStandard=Comment'},
                                {'Native Map': ['automountMapName'], 'Standard Name': 'dsAttrTypeStandard=RecordName'}],
         'Native Map': [{'Group Object Classes': 'OR',
                         'Object Classes': ['automountMap'],
                         'Search Base': 'cn=automount'}]},

        {'Standard Name': 'dsRecTypeStandard=Automount',
         'Attribute Type Map': [{'Native Map': ['description'], 'Standard Name': 'dsAttrTypeStandard=Comment'},
                                {'Native Map': ['automountInformation'],
                                 'Standard Name': 'dsAttrTypeStandard=AutomountInformation'},
                                {'Native Map': ['automountKey'], 'Standard Name': 'dsAttrTypeStandard=RecordName'}],
         'Native Map': [{'Group Object Classes': 'OR',
                         'Object Classes': ['automount'],
                         'Search Base': 'cn=automount'}]}
    ],
    'Denied SASL Methods': ['DIGEST-MD5', 'CRAM-MD5'],
    'Delay Rebind Try in seconds': 0,
    'Enable Use': True,
    'Map Search Base': 'cn=config',
    'OpenClose Timeout in seconds': 15,
    'Port Number': 389,
    'SSL': True,
    'Search Timeout in seconds': 120,
    'Server': '',
    'Server Mappings': True,
    'Template Name': 'FreeIPA Server',
    'Template Search Base Suffix': '',
    'Template Version': '1.0',
    'UI Name': ''
};

macosODPolicy = {'Denied SASL Methods': ['DIGEST-MD5', 'CRAM-MD5'],
                 'Configured Security Level': {'Advisory Client Caching': False,
                                               'Binding Required': True,
                                               'Man In The Middle': True,
                                               'No ClearText Authentications': True,
                                               'Packet Encryption': True,
                                               'Packet Signing': True},
                 'Directory Binding': True};

macosLDAPReplicas = {'IPaddresses': ['172.16.23.138', '172.16.23.139', '172.16.23.140'],
                     'PrimaryMaster': 'ipa01.example.org',
                     'ReplicaName': 'Master IPA Server',
                     'Replicas': ['ipa02.example.org', 'ipa03.example.org']};

macosKerberosClient = {
    'edu.mit.kerberos': {'domain_realm': {'.example.org': 'EXAMPLE.ORG',
                                          'example.org': 'EXAMPLE.ORG'},
                         'libdefaults': {'default_realm': 'EXAMPLE.ORG'},
                         'realms': {'EXAMPLE.ORG': {'KADM_List': ['ipa.example.org', '172.16.23.138'],
                                                    'KDC_List': ['ipa.example.org', '172.16.23.138']}
                                    }
                         },
    # UNIX Timestamp in this case 10/26/2017 @ 8=25am (UTC)
    'generationID': 1509006343
};
