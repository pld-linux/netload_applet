# Specfile for netload_applet
# $Id: netload_applet.spec,v 1.1 2001-10-07 03:21:42 kloczek Exp $

%define name netload_applet
%define version @VERSION@
%define release 1
%define prefix /usr

Summary:	A nice looking network load monitor applet for GNOME.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Copyright:	GPL
Group:		User Interface/Desktops
Vendor:		Jan Oberländer <mindriot@gmx.net>
Source:		http://www.stud.uni-karlsruhe.de/~uslk/netload_applet-%{version}.tar.gz
URL:		http://netload-applet.sourceforge.net/
Packager:	Jan Oberländer <mindriot@gmx.net>
Buildroot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk+ >= 1.2.0, gnome-core >= 1.2.0

%description
This is a small network load monitoring applet for the GNOME panel.

%prep
%setup -n netload_applet-%{version}

%build
./configure --prefix=%prefix --sysconfdir=/etc
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make sysconfdir=$RPM_BUILD_ROOT/etc prefix=$RPM_BUILD_ROOT/%{prefix} install-strip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO AUTHORS INSTALL COPYING ChangeLog
%attr(755,root,root) %{prefix}/bin/netload_applet
%{prefix}/share/applets/Network/netload_applet.desktop
%{prefix}/share/pixmaps/netload_applet.png
/etc/CORBA/servers/netload_applet.gnorba
%{prefix}/share/locale/*/*/*

%changelog
* Thu Mar  8 2001 Jan Oberländer <mindriot@gmx.net>
  [netload_applet-0.3.0-1]
- Autoconf/automake and i18n!

* Thu Nov 10 2000 Jan Oberländer <mindriot@gmx.net>
  [netload_applet-0.2.1-1]
- Small bugfix, see ChangeLog file in source distribution

* Thu Nov 9 2000 Jan Oberländer <mindriot@gmx.net>
  [netload_applet-0.2.0-1]
- Totally reworked version with several new features

* Tue Jul 18 2000 Matthias Saou <matthias.saou@est.une.marmotte.net>
  [netload_applet-0.1.1-1]
- Initial RPM release
