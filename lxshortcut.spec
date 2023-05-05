#
# Conditional build:
%bcond_with	gtk3	# use GTK+3 instead of GTK+2

Summary:	Program to edit application shortcuts
Summary(pl.UTF-8):	Program do modyfikowania skrótów do aplikacji
Name:		lxshortcut
Version:	0.1.2
Release:	4
License:	GPL v2+
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	72f0dfafa8098be853beae6e33b5e13b
URL:		http://www.lxde.org/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool
BuildRequires:	pkgconfig
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.12.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXShortcut is a small program used to edit application shortcuts
created with freedesktop.org Desktop Entry spec.

%description -l pl.UTF-8
LXShortcut to mały program służący do modyfikowania skrótów do
aplikacji tworzonych zgodnie ze specyfikacją freedesktop.org Desktop
Entry.

%prep
%setup -q

%build
%configure \
	%{?with_gtk3:--enable-gtk3}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unify name
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{tt_RU,tt}
# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK
# unsupported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/frp

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxshortcut
%{_datadir}/lxshortcut
