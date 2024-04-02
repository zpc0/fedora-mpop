Name:           mpop
Version:        1.4.10
Release:        9%{?dist}
Summary:        Client for receiving mail from POP3 mailboxes

License:        GPLv3+
URL:            https://marlam.de/mpop/
Source0:        https://marlam.de/mpop/releases/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  libgsasl-devel
BuildRequires:  libidn-devel
BuildRequires:  gnutls-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  gettext

%description
mpop is a small and fast POP3 client. Features include mail filtering,
delivery to mbox files, maildir folders or a mail delivery agent, a very
fast POP3 implementation, many authentication methods, good TLS/SSL
support, IPv6 support, and more.

%prep
%autosetup

%build
%configure --with-gnome-keyring
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS NOTES README THANKS
%doc doc/mpoprc.example
%license COPYING
%{_mandir}/man*/%{name}*.*
%{_infodir}/%{name}.info.*
%{_bindir}/%{name}

%changelog
%autochangelog
