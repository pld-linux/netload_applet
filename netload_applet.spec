Summary:	A nice looking network load monitor applet for GNOME
Name:		netload_applet
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Vendor:		Jan Oberländer <mindriot@gmx.net>
Source0:	http://www.stud.uni-karlsruhe.de/~uslk/%{name}-%{version}.tar.gz
URL:		http://netload-applet.sourceforge.net/
Requires:	gtk+ >= 1.2.0, gnome-core >= 1.2.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is a small network load monitoring applet for the GNOME panel.

%prep
%setup -q

%build
rm -f missing
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO AUTHORS ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/netload_applet
%{_sysconfdir}/CORBA/servers/netload_applet.gnorba
%{_datadir}/applets/Network/netload_applet.desktop
%{_pixmapsdir}/netload_applet.png
