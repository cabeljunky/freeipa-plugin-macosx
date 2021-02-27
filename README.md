# FreeIPA DirectoryService.Framework Support.
## What will this plugin offer?
This plugin sketch will allow macOS/OS X/Mac OS X/Darwin clients that use the DirectoryService Framework (introduced in 10.4) to join a FreeIPA domain like joining a native OpenDirectory Server.
## How?
The DirectoryService.Framework, although open source only until Snow Leopard was designed from it's initial release to be flexible enough to allow this, using templates published in the LDAP itself.
It is accomplished by publishing a MacOS X OD Config entry in the cn=opendirectory,cn=etc,$SUFFIX container. The config entry contains the schema mapping templates, kerberos realm configuration and LDAP connection security policy configuration.
## What is needed
1. Announcing via mDNS to enable the discovery of the IPA server. We intend to use Avahi.
2. A configuration template, that is already sketched in freeipa-darwin-policy.py
3. An ACI that allows anonymous access to the configuration template (/plugin.d/updates/60-macosx.ldif)
4. A schema extension for the needed apple properties (/plugin.d/schema/60-macosx.ldif)
5. A COS Plugin configuration for autogeneration of the authAuthority entries of the existing accounts
## What's implemented?
 - The IPA script that will take the json object and convert it to the ldap config
 - The IPA script that shows the content
 - A UI that acn show th content or change the content

## How to get it working now,
In the examples directory there are xml files that maps the data.
The ldif file there is an example config. The content is base64 encode in the ldif and represents the xml files
The plugin folder need to be copyed to the ipa python plugin folder
The schema.d needs to be copy to the ipa server folder 
The updates folder needs to go to the  ipa server update folder.

You can have a look in the freeipa-plugin-macosx.spec file for the locations.


Add to all the users object:
```ldif
objectClass: apple-user
```
Add the following attributes to the users:
```ldif
altSecurityIdentities: Kerberos:admin@EXAMPLE.ORG
authAuthority: Kerberosv5;;diradmin@EXAMPLE.ORG;EXAMPLE.ORG;
```

Add to all the users groups:
```ldif
objectClass: apple-group
```


Add to all the computers:
```ldif
objectClass: apple-computer
cn: test-mac.example.com
cn: test-mac.example.com$
authAuthority: ;Kerberosv5;;test-mac.example.com$@EXAMPLE.ORG;EXAMPLE.ORG;
fqdn: test-mac.example.com$
krbPrincipalName: test-mac.example.com$
```


#To authenticate wit FreeIPA
The mac machnins will try to use "CRAM-MD5"
This will not work with the freeipa server.

So on [this article](https://serverfault.com/a/922177) describes the way to disable this on the mac machine when you have set up the connection
You can also disable it on the Freeipa side [describe here](https://access.redhat.com/documentation/en-us/red_hat_directory_server/11/html/configuration_command_and_file_reference/core_server_configuration_reference#nsslapd-allowed-sasl-mechanisms
)

But for me that didn't work properly.
The only way that I got this working wit MacOS 10.14, 10.15 and 11.0 was to use it like this:

Create a keytab file for the machine.

Generate keytab on IPA server
```bash
ipa-getkeytab -s yourserver.yourdomain.com -p host/workstation.yourdomain.com -k ~/workstation.keytab
```
Retrieve keytab from server
```bash
scp user@yourserver.yourdomain.com:/home/user/workstation.keytab /etc/krb5.keytab
chown root:wheel /etc/krb5.keytab
chmod 0600 /etc/krb5.keytab
```
Now connect the machine to the FreeIPA server. Use the "Directory Utility" 
Then
```bash
rm /etc/krb5.keytab
```


#Hide the admin user
https://support.apple.com/en-us/HT203998

https://apple.stackexchange.com/questions/379080/hide-a-user-account-from-the-login-screen-of-macos-catalina

```bash
sudo /System/Library/CoreServices/ManagedClient.app/Contents/Resources/createmobileaccount -P -n [username]
```

# Links:

https://listman.redhat.com/archives/freeipa-users/2016-February/msg00059.html
https://listman.redhat.com/archives/freeipa-users/2016-February/msg00059.html
https://listman.redhat.com/archives/freeipa-users/2016-February/msg00070.html
https://support.apple.com/lv-lv/guide/directory-utility/diruc0621ca1/6.0/mac/11.0
https://annvix.com/Using_Kerberos_5_for_Single_Sign-On_Authentication

### schema

Apple OpenLDAP 2.4.28

https://opensource.apple.com/source/OpenLDAP/OpenLDAP-530.80.2/OpenLDAP/servers/slapd/schema/apple_auxillary.schema.auto.html
https://opensource.apple.com/source/OpenLDAP/OpenLDAP-530.80.2/OpenLDAP/servers/slapd/schema/apple.schema

https://opensource.apple.com/source/OpenLDAP/OpenLDAP-530.80.2/OpenLDAP/servers/slapd/schema/microsoft.schema
https://www.freeipa.org/page/HowTo/Setup_FreeIPA_Services_for_Mac_OS_X_10.12

###FreeIPA info

https://access.redhat.com/documentation/en-us/red_hat_directory_server/11/html/configuration_command_and_file_reference/core_server_configuration_reference#nsslapd-allowed-sasl-mechanisms
https://serverfault.com/a/922177
https://access.redhat.com/documentation/en-us/red_hat_directory_server/11/html-single/administration_guide/index

### MDM
http://docs.macsysadmin.se/2017/pdf/Day2Session5.pdf
https://developer.apple.com/business/documentation/MDM-Protocol-Reference.pdf
https://github.com/micromdm/micromdm
https://github.com/ProfileCreator/ProfileCreator