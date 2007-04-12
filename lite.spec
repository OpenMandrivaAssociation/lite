
%define name	lite
%define Name	LiTE
%define version	0.7.2
%define rel	2

%define libname_orig lib%{name}
%define libmajor 2
%define libname %mklibname %{name} %{libmajor}
%define libnamedevel %mklibname %{name} %{libmajor} -d

Name:		%{name}
Summary:	LiTE is a Toolkit Engine
Version:	%version
Release:	%mkrel %rel
URL:		http://www.directfb.org/
Group:		System/Libraries
Source0:	http://www.directfb.org/downloads/Libs/%{Name}-%{version}.tar.bz2
License:	LGPL
BuildRequires:	directfb-devel pkgconfig automake
BuildRoot:	%{_tmppath}/%{name}-root

%description
LiTE is a Toolkit Engine for DirectFB.

%package common
Summary:	Images and fonts for LiTE
Group:		Graphical desktop/Other

%description common
LiTE is a Toolkit Engine for DirectFB.
This package contains the images and fonts needed by LiTE.

%package tools
Summary:	LiTE tools
Group:		Graphical desktop/Other

%description tools
LiTE is a Toolkit Engine for DirectFB.
This package contains literun and dfbspy.

%package -n %{libname}
Summary:	Main library for LiTE
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Requires:	%{name}-common = %{version}

%description -n %{libname}
LiTE is a Toolkit Engine for DirectFB.
This package contains the library needed to run programs dynamically
linked with LiTE.

%package -n %{libnamedevel}
Summary:	Headers for developing programs that will use LiTE
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	pkgconfig

%description -n %{libnamedevel}
LiTE is a Toolkit Engine for DirectFB.
This package contains the headers that programmers will need to develop
applications which will use LiTE.

%prep
%setup -q -n %Name-%version

%build
./autogen.sh

%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files common
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO COPYING ChangeLog
%{_datadir}/LiTE
%{_datadir}/fonts/truetype/Misc-Fixed.pfa
%{_datadir}/fonts/truetype/decker.ttf
%{_datadir}/fonts/truetype/whiterabbit.ttf

%files tools
%defattr(-,root,root)
%{_bindir}/dfbspy
%{_bindir}/literun

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libnamedevel}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/lite.pc
%{_includedir}/lite


