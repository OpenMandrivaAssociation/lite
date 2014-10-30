
%define name	lite
%define Name	LiTE
%define version	0.9.1_svn
%define rel	1
%define api 0.9
%define libname_orig lib%{name}
%define libmajor 1
%define libname %mklibname %{name} %{libmajor}
%define lecklibname %mklibname leck %{libmajor}
%define libnamedevel %mklibname %{name} -d

Name:		%{name}
Summary:	Toolkit Engine
Version:	%version
Release:	%rel
URL:		http://www.directfb.org/
Group:		System/Libraries
Source0:	http://www.directfb.org/downloads/Libs/%{Name}-0.9.1.tar.gz
License:	LGPLv2+
BuildRequires:	directfb-devel 
BuildRequires:	pkgconfig 
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool



%description
LiTE is a Toolkit Engine for DirectFB.

%package common
Summary:	Images and fonts for LiTE
Requires:	fonts-ttf-vera
Group:		Graphical desktop/Other

%description common
LiTE is a Toolkit Engine for DirectFB.
This package contains the images and fonts needed by LiTE.

%package tools
Summary:	LiTE tools and examples
Group:		Graphical desktop/Other

%description tools
LiTE is a Toolkit Engine for DirectFB.
This package contains example tools for LiTE.

%package -n %{libname}
Summary:	Main library for LiTE
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Requires:	%{name}-common >= %{version}

%description -n %{libname}
LiTE is a Toolkit Engine for DirectFB.
This package contains the library needed to run programs dynamically
linked with LiTE.

%package -n %{lecklibname}
Summary:	LiTE's extended Component Kit
Group:		System/Libraries

%description -n %{lecklibname}
LiTE is a Toolkit Engine for DirectFB. This package contains
LiTE's extended Component Kit.

%package -n %{libnamedevel}
Summary:	Headers for developing programs that will use LiTE
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{lecklibname} = %{version}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	leck-devel = %{version}-%{release}
Obsoletes:	%{_lib}lite2-devel < 0.8.6
Requires:	pkgconfig

%description -n %{libnamedevel}
LiTE is a Toolkit Engine for DirectFB.
This package contains the headers that programmers will need to develop
applications which will use LiTE.

%prep
%setup -q -n %Name-0.9.1

%build
./autogen.sh
%configure2_5x --with-fontdir=%{_datadir}/%{Name}/fonts
%make

%install
%makeinstall_std

rm %{buildroot}%{_datadir}/%{Name}/fonts/vera{,bd,bi,i}.ttf
ln -s %{_datadir}/fonts/TTF/Vera.ttf %{buildroot}%{_datadir}/%{Name}/fonts/vera.ttf
ln -s %{_datadir}/fonts/TTF/VeraBd.ttf %{buildroot}%{_datadir}/%{Name}/fonts/verabd.ttf
ln -s %{_datadir}/fonts/TTF/VeraBI.ttf %{buildroot}%{_datadir}/%{Name}/fonts/verabi.ttf
ln -s %{_datadir}/fonts/TTF/VeraIt.ttf %{buildroot}%{_datadir}/%{Name}/fonts/verai.ttf


%files common
%doc AUTHORS NEWS README TODO COPYING ChangeLog
%{_datadir}/LiTE

%files tools
%doc AUTHORS NEWS README TODO COPYING ChangeLog
%{_bindir}/lite_*


%files -n %{libname}
%doc AUTHORS NEWS README TODO COPYING ChangeLog
%{_libdir}/liblite-%{api}.so.%{libmajor}.0.0


%files -n %{lecklibname}
%doc AUTHORS NEWS README TODO COPYING ChangeLog
%{_libdir}/libleck-%{api}.so.%{libmajor}.0.0

%files -n %{libnamedevel}
%doc AUTHORS NEWS README TODO COPYING ChangeLog
%{_libdir}/liblite-%{api}.so.%{libmajor}
%{_libdir}/liblite-%{api}.so.%{libmajor}.0.0
%{_libdir}/liblite.so
%{_libdir}/libleck-%{api}.so.%{libmajor}
%{_libdir}/libleck-%{api}.so.%{libmajor}.0.0
%{_libdir}/libleck.so
%{_libdir}/pkgconfig/lite.pc
%{_libdir}/pkgconfig/leck.pc
%{_includedir}/lite
%{_includedir}/leck



