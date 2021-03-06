Summary:	A nice looking network load monitor applet for GNOME
Summary(pl.UTF-8):	Ładnie wyglądający monitor obciążenia sieci dla GNOME
Name:		netload_applet
Version:	0.3.1
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/netload-applet/%{name}-%{version}.tar.gz
# Source0-md5:	7294ddb00d94edf0d557544418e87ade
URL:		http://netload-applet.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-core-devel >= 1.2.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
This is a small network load monitoring applet for the GNOME panel.

%description -l pl.UTF-8
To mały monitor obciążenia sieci jako aplet do panelu GNOME.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/netload_applet
%{_sysconfdir}/CORBA/servers/netload_applet.gnorba
%{_datadir}/applets/Network/netload_applet.desktop
%{_pixmapsdir}/netload_applet.png
