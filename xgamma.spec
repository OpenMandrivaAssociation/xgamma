Name: xgamma
Version: 1.0.2
Release: %mkrel 2
Summary: Alter a monitor's gamma correction through the X server
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: libxxf86vm-devel	>= 1.0.1

%description
Alter a monitor's gamma correction through the X server

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xgamma
%{_mandir}/man1/xgamma.1*
