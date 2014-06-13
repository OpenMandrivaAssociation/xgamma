Name: xgamma
Version: 1.0.5
Release: 7
Summary: Alter a monitor's gamma correction through the X server
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xxf86vm) >= 1.0.0
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


%changelog
* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.5-1
+ Revision: 786823
- version update 1.0.5

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2
+ Revision: 671318
- mass rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 464707
- New version: 1.0.3

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-4mdv2009.1
+ Revision: 351132
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2009.0
+ Revision: 226042
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 154735
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 07 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 59597
- new upstream release: 1.0.2
- fix description

