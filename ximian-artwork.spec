Summary:	Ximian Industrial theme
Summary(pl):	Motyw Ximian Industrial
Name:		ximian-artwork
Version:	0.2.34
Release:	8
License:	GPL
Group:		Themes
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	f7121cf3f5fca9170e1c1ba32cceab0d
Patch0:		%{name}-enginesdir.patch
Patch1:		%{name}-wallpapersdir.patch
URL:		http://www.ximian.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	gtk+2-devel >= 2:2.6.1
BuildRequires:	intltool >= 0.23
BuildRequires:	libtool
BuildRequires:	metacity
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Industrial look & feel.

%description -l pl
Wygl±dy Industrial.

%package -n icons-Industrial
Summary:	Industrial icons
Summary(pl):	Ikony Industrial
Group:		Themes
Obsoletes:	ximian-artwork
# contains dir used by icons
Requires:	XcursorTheme-Industrial = %{version}-%{release}

%description -n icons-Industrial
Industrial icons for GNOME & KDE.

%description -n icons-Industrial -l pl
Ikony Industrial dla GNOME i KDE.

%package -n gtk-theme-engine-Industrial
Summary:	GTK+ Industrial theme
Summary(pl):	Motyw Industrial dla GTK+
Group:		Themes
Obsoletes:	ximian-artwork

%description -n gtk-theme-engine-Industrial
GTK+ Industrial theme.

%description -n gtk-theme-engine-Industrial -l pl
Motyw Industrial dla GTK.

%package -n metacity-themes-Industrial
Summary:	Metacity Industrial theme
Summary(pl):	Motyw Industrial dla Metacity
Group:		Themes
Requires:	metacity = %(rpm -q --qf '%{EPOCH}:%{VERSION}' metacity)
Provides:	metacity-theme-base = %(rpm -q --qf '%{EPOCH}:%{VERSION}' metacity)
Obsoletes:	ximian-artwork

%description -n metacity-themes-Industrial
GTK+ Industrial Metacity.

%description -n metacity-themes-Industrial -l pl
Motyw Industrial dla Metacity.

%package -n gnome-theme-Industrial
Summary:	GNOME Industrial theme
Summary(pl):	Motyw Industrial dla GNOME
Group:		Themes
Requires:	icons-Industrial = %{version}-%{release}
Requires:	metacity-themes-Industrial = %{version}-%{release}
Requires:	gtk2-engines >= 1:2.6.0-1
Requires:	gtk2-theme-Industrial = %{version}-%{release}
Requires:	gtk-theme-engine-Industrial = %{version}-%{release}
Requires:	nautilus-theme-Industrial = %{version}-%{release}
Obsoletes:	ximian-artwork

%description -n gnome-theme-Industrial
GNOME Industrial theme (gtk, gtk2, metacity, nautilus).

%description -n gnome-theme-Industrial -l pl
Motyw Industrial dla GNOME (gtk, gtk2, metacity, nautilus).

%package -n gtk2-theme-Industrial
Summary:	GTK+2 Industrial theme
Summary(pl):	Motyw Industrial dla GTK+2
Group:		Themes
Obsoletes:	ximian-artwork

%description -n gtk2-theme-Industrial
GTK+2 Industrial theme.

%description -n gtk2-theme-Industrial -l pl
Motyw Industrial dla GTK+2.

%package -n nautilus-theme-Industrial
Summary:	Nautilus Industrial theme
Summary(pl):	Motyw Industrial dla Nautilusa
Group:		Themes
Requires:	nautilus
Obsoletes:	ximian-artwork

%description -n nautilus-theme-Industrial
Nautilus Industrial theme.

%description -n nautilus-theme-Industrial -l pl
Motyw Industrial dla Nautilusa.

%package -n xmms-skin-Industrial
Summary:	XMMS skin taken from Industrial
Summary(pl):	Skórka dla XMMS-a w stylu Industrial
Group:		X11/Applications/Multimedia
Requires:	xmms
Obsoletes:	ximian-artwork-xmms

%description -n xmms-skin-Industrial
XMMS skin taken from Industrial.

%description -n xmms-skin-Industrial -l pl
Skórka dla XMMS-a w stylu Industrial.

%package -n XcursorTheme-Industrial
Summary:	Industrial cursor pack
Summary(pl):	Motyw kursorów Industrial
Group:		X11/XFree86
Requires:	XFree86 
Obsoletes:	ximian-artwork

%description -n XcursorTheme-Industrial
Industrial cursor pack.

%description -n XcursorTheme-Industrial -l pl
Motyw kursorów Industrial.

%package -n gdm-theme-Industrial
Summary:	Industrial GDM theme
Summary(pl):	Motyw Industrial dla GDM-a
Group:		Themes
Requires:	gdm >= 2.4
Obsoletes:	ximian-artwork-gdm

%description -n gdm-theme-Industrial
Industrial GDM theme.

%description -n gdm-theme-Industrial -l pl
Motyw Industrial dla GDM-a.

%package -n galeon-theme-Industrial
Summary:	Industrial Galon theme
Summary(pl):	Motyw Industrial dla Galeona
Group:		Themes
Requires:	galeon
Obsoletes:	ximian-artwork-galeon

%description -n galeon-theme-Industrial
Industrial Galeon theme.

%description -n galeon-theme-Industrial -l pl
Motyw Industrial dla Galeona.

%package -n desktop-wallpapers-Industrial
Summary:	Industrial wallpapers
Summary(pl):	Tapety w stylu Industrial
Group:		Themes
Obsoletes:	ximian-artwork-backgrounds
Obsoletes:	wallpapers-Industrial

%description -n desktop-wallpapers-Industrial
Industrial wallpapers.

%description -n desktop-wallpapers-Industrial -l pl
Tapety w stylu Industrial.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# .a, .la are not needed, .so is included in gtk2-engines
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.{a,la,so}
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n icons-Industrial
%defattr(644,root,root,755)
%{_iconsdir}/Industrial/24x24
%{_iconsdir}/Industrial/32x32
%{_iconsdir}/Industrial/48x48
%{_iconsdir}/Industrial/72x72
%{_iconsdir}/Industrial/96x96
%{_iconsdir}/Industrial/scalable
%{_iconsdir}/Industrial/index.theme
%{_pixmapsdir}/*.png
%{_pixmapsdir}/ximian

%files -n gnome-theme-Industrial
%defattr(644,root,root,755)
%{_datadir}/themes/Industrial/index.theme

%files -n gtk2-theme-Industrial
%defattr(644,root,root,755)
%{_datadir}/themes/Industrial/gtk-2.0/*
%exclude %{_datadir}/themes/Industrial/gtk-2.0/gtkrc

%files -n gtk-theme-engine-Industrial
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/libindustrial.so
%{_datadir}/themes/Industrial/gtk

%files -n metacity-themes-Industrial
%defattr(644,root,root,755)
%{_datadir}/themes/Industrial/metacity*/

%files -n nautilus-theme-Industrial
%defattr(644,root,root,755)
%{_pixmapsdir}/nautilus/*

%files -n gdm-theme-Industrial
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/*

%files -n xmms-skin-Industrial
%defattr(644,root,root,755)
%{xmms_datadir}/Skins/*

%files -n XcursorTheme-Industrial
%defattr(644,root,root,755)
%dir %{_iconsdir}/Industrial
%{_iconsdir}/Industrial/cursors

%files -n galeon-theme-Industrial
%defattr(644,root,root,755)
%{_datadir}/galeon/themes/*

%files -n desktop-wallpapers-Industrial
%defattr(644,root,root,755)
%{_datadir}/wallpapers/ximian
