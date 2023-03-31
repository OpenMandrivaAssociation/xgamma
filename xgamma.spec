Name:		xgamma
Version:	1.0.7
Release:	2
Summary:	Alter a monitor's gamma correction through the X server
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xxf86vm) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)

%description
Alter a monitor's gamma correction through the X server

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xgamma
%doc %{_mandir}/man1/xgamma.1*
