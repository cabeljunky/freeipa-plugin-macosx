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
