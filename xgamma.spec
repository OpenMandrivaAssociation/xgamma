Name: xgamma
Version: 1.0.5
Release: 1
Summary: Alter a monitor's gamma correction through the X server
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxxf86vm-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Alter a monitor's gamma correction through the X server

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xgamma
%{_mandir}/man1/xgamma.1*
