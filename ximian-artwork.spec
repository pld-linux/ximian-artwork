Summary:	Ximian Industrial theme
Summary(pl):	Motyw Ximian Industrial
Name:		ximian-artwork
Version:	0.2.32
Release:	3
License:	GPL
Group:		Themes
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	a5a602b15956020d56b561d833351bd4
URL:		http://www.ximian.com/
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.23
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ximian-artwork contains the default style configuration for the Ximian
Desktop. This package contains themes for GNOME2, gdm, xmms and
galeon.

%description -l pl
ximian-artwork zawiera domy¶lny motyw dla Ximian Desktop. Pakiet ten
zawiera motywy dla GNOME2, gdm, xmms oraz dla galeona.

%package backgrounds
Summary:	Ximian Industrial theme - backgrounds
Summary(pl):	Motyw Ximian Industrial - t³a
Group:		Themes

%description backgrounds
Ximian Industrial theme - backgrounds.

%description backgrounds -l pl
Motyw Ximian Industrial - t³a.

%package galeon
Summary:	Ximian Industrial theme for galeon
Summary(pl):	Motyw Ximian Industrial dla galeona
Group:		Themes
Requires:	galeon

%description galeon
Ximian Industrial theme for galeon.

%description galeon -l pl
Motyw Ximian Industrial dla galeona.

%package gdm
Summary:	Ximian Industrial theme for gdm
Summary(pl):	Motyw Ximian Industrial dla gdm
Group:		Themes
Requires:	gdm

%description gdm
Ximian Industrial theme for gdm.

%description gdm -l pl
Motyw Ximian Industrial dla gdm.

%package xmms
Summary:	Ximian Industrial theme for xmms
Summary(pl):	Motyw Ximian Industrial dla xmms
Group:		Themes
Requires:	xmms

%description xmms
Ximian Industrial theme for xmms.

%description xmms -l pl
Motyw Ximian Industrial dla xmms.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
exit 0

%files
%defattr(644,root,root,755)
%{_datadir}/themes/*
%{_pixmapsdir}/*.png
%{_pixmapsdir}/ximian
%{_pixmapsdir}/nautilus/*
%{_libdir}/gtk/themes/engines/libindustrial.so
%{_libdir}/gtk-2.0/*/engines/libindustrial.so
%{_datadir}/icons/Industrial/
%{_datadir}/icons/gnome/*/*/*

%files backgrounds
%defattr(644,root,root,755)
%{_pixmapsdir}/backgrounds

%files galeon
%defattr(644,root,root,755)
%{_datadir}/galeon/themes/*

%files gdm
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/*

%files xmms
%defattr(644,root,root,755)
%{xmms_datadir}/Skins/*
