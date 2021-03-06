%global debug_package %{nil}

Name:           freeipa-plugin-macosx
Version:        0.0.2
Release:        1%{?dist}
Summary:        Support macOS systems in FreeIPA

License:        GPL
URL:            https://github.com/cabeljunky/freeipa-plugin-macos
Source0:        freeipa-plugin-macos-%{version}.tar.gz

BuildRequires:  python3-devel
Requires:       freeipa-server-common >= 4.8.7
Requires:       python3-ipaserver >= 4.8.7

%description
A module for FreeIPA to allow managing desktop profiles defined
by the FleetCommander.

%prep
%autosetup

%build
touch debugfiles.list

%install
rm -rf $RPM_BUILD_ROOT
%__mkdir_p %buildroot/%{python3_sitelib}/ipaclient/plugins
%__mkdir_p %buildroot/%{python3_sitelib}/ipaserver/plugins
%__mkdir_p %buildroot/%_datadir/ipa/schema.d
%__mkdir_p %buildroot/%_datadir/ipa/updates
#%__mkdir_p %buildroot/%_datadir/ipa/ui/js/plugins/macosx

#%__cp plugin/ipaclient/plugins/macosx.py %buildroot/%{python3_sitelib}/ipaclient/plugins
%__cp plugin/ipaserver/plugins/macosx.py %buildroot/%{python3_sitelib}/ipaserver/plugins
%__cp plugin/schema.d/60-apple.ldif %buildroot/%_datadir/ipa/schema.d
%__cp plugin/schema.d/60-apple-auxillary.ldif %buildroot/%_datadir/ipa/schema.d
%__cp plugin/schema.d/60-apple-ipa.ldif %buildroot/%_datadir/ipa/schema.d
%__cp plugin/updates/60-macos.update %buildroot/%_datadir/ipa/updates
#%__cp plugin/ui/macosx.js %buildroot/%_datadir/ipa/ui/js/plugins/macosx

%posttrans
python3 -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    # This must be run in posttrans so that updates from previous
    # execution that may no longer be shipped are not applied.
    /usr/sbin/ipa-server-upgrade --quiet >/dev/null || :

    # Restart IPA processes. This must be also run in postrans so that plugins
    # and software is in consistent state
    # NOTE: systemd specific section

    /bin/systemctl is-enabled ipa.service >/dev/null 2>&1
    if [  $? -eq 0 ]; then
        /bin/systemctl restart ipa.service >/dev/null 2>&1 || :
    fi
fi

%files
%license COPYING
%doc README
#%python3_sitelib/ipaclient/plugins/*
%python3_sitelib/ipaserver/plugins/*
%_datadir/ipa/schema.d/*
%_datadir/ipa/updates/*
#%_datadir/ipa/ui/js/plugins/macosx/*

%changelog
* Thu 02 21 2021 Edward Heuveling <sea.heuveling@red-software.nl> 0.0.2
- Initial release structure based on the deskprofile plugin code
* Thu Oct 26 2017 Alexander Bokovoy <abokovoy@redhat.com> 0.0.1-1
- Initial release structure based on the deskprofile plugin code

