Summary:	Evolution Connector for Sun Java Enterprise System Calendar Server (SJESCS)
Summary(pl.UTF-8):	Evolution Connector dla Sun Java Enterprise System Calendar Server (SJESCS)
Name:		evolution-jescs
Version:	2.22.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-jescs/2.22/%{name}-%{version}.tar.bz2
# Source0-md5:	f11a85739539ded6ae70aeeb86fe6dd9
URL:		http://www.go-evolution.org/Evolution_JESCS
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	evolution-devel >= 2.22.0
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool >= 0.36.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.22.0
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The JESCS-connector adds support to Evolution for Sun Java Enterprise
System Calendar Server (SJESCS) 5.1 and above, and for the Web
Calendar Access Protocol (WCAP) 2.0, 3.0, 3.1.

%description -l pl.UTF-8
JESCS-connector dodaje do Evolution wsparcie dla Sun Java Enterprise
System Calendar Server (SJESCS) 5.1 i nowszych oraz Web Calendar
Access Protocol (WCAP) 2.0, 3.0, 3.1.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/evolution-data-server-1.2/camel-providers/libcamelsunone.la

%find_lang %{name}-2.22

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-2.22.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/evolution-data-server-1.2/camel-providers/libcamelsunone.so
%{_libdir}/evolution-data-server-1.2/camel-providers/libcamelsunone.urls
%attr(755,root,root) %{_libdir}/evolution/2.22/evolution-jescs
%{_libdir}/bonobo/servers/GNOME_Evolution_SunOne_Storage.server
%{_datadir}/evolution-jescs
%{_datadir}/evolution/2.22/images/*.png
