Name:           mpop
Version:        1.0.28
Release:        1%{?dist}
Summary:        POP3 client for recieving mail from POP3 mailboxes

Group:          Applications/Internet
License:        GPLv3+
URL:            http://mpop.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  openssl-devel
BuildRequires:  libgsasl-devel
BuildRequires:  libidn-devel
BuildRequires:  gnutls-devel
BuildRequires:  gnome-keyring-devel
BuildRequires:  gettext

Requires(post):  info
Requires(preun): info

%description
mpop is a small and fast POP3 client. Features include mail filtering,
delivery to mbox files, maildir folders or a mail delivery agent, a very
fast POP3 implementation, many authentication methods, good TLS/SSL
support, IPv6 support, and more.

%prep
%setup -q

%build
%configure --with-gnome-keyring
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS NOTES README THANKS
%doc doc/mpoprc.example
%{_mandir}/man*/%{name}*.*
%{_infodir}/%{name}.info.gz
%{_bindir}/%{name}

%changelog
* Tue Apr 23 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.28-1
- Updated to new upstream version 1.0.28

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.27-3
- Rebuild for libgsasl

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 05 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.27-1
- Updated to new upstream version 1.0.27

* Sun Jan 08 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.26-1
- Updated to new upstream version 1.0.26

* Tue Oct 25 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.25-1
- Updated to new upstream version 1.0.25

* Fri Aug 12 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-3
- Rebuild (info)

* Wed Apr 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-2
- Removed obsolete doc entries

* Wed Apr 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-1
- Updated to new upstream version 1.0.24

* Mon Mar 28 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.23-1
- Updated to new upstream version 1.0.23

* Mon Jan 17 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.22-1
- Updated to new upstream version 1.0.22

* Sat Jul 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.21-1
- Updated to new upstream version 1.0.21

* Thu Apr 08 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.20-1
- Updated to new upstream version 1.0.20

* Mon Nov 16 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.19-1
- Updated to new upstream version 1.0.19

* Sun Oct 12 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.18-1
- Updated to new upstream version 1.0.18

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.17-1
- Updated to new upstream version 1.0.17

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 10 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.16-3
- Added missing BR

* Sat Jan 10 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.16-2
- Fixed files section, removed duplicates

* Mon Dec 29 2008 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.16-1
- Initial package for Fedora
