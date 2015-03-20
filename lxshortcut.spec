#
# Conditional build:
%bcond_with		gtk3		# build GTK+3 disables GTK+2
%bcond_without		gtk2	# build with GTK+2

%if %{with gtk3}
%undefine	with_gtk2
%endif

Summary:	Program to edit application shortcuts
Name:		lxshortcut
Version:	0.1.2
Release:	4
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	72f0dfafa8098be853beae6e33b5e13b
URL:		http://wiki.lxde.org/en/LXShortCut
BuildRequires:	gettext-tools
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXShortcut is a small program used to edit application shortcuts
created with freedesktop.org Desktop Entry spec.

%prep
%setup -q

%build
%configure \
	%{?with_gtk3:--enable-gtk3}
touch po/stamp-it
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK
# unsupported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/frp

mv $RPM_BUILD_ROOT%{_datadir}/locale/tt{_RU,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxshortcut
%{_datadir}/lxshortcut
