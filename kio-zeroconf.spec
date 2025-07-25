#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kio-zeroconf
Version: 25.04.3
Release: %{?git:0.%{git}.}1
Summary: KIO worker to discover file systems by DNS-SD (zeroconf)
%if 0%{?git:1}
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/kio-zeroconf/-/archive/%{gitbranch}/kio-zeroconf-%{gitbranchd}.tar.bz2#/kio-zeroconf-%{git}.tar.bz2
%else
Source0:        https://invent.kde.org/network/%{name}/-/archive/master/%{name}-master.tar.bz2
%endif
%else
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/kio-zeroconf/-/archive/%{gitbranch}/kio-zeroconf-%{gitbranchd}.tar.bz2#/kio-zeroconf-%{git}.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/kio-zeroconf-%{version}.tar.xz
%endif
%endif
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)

%rename plasma6-kio-zeroconf

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DQT_MAJOR_VERSION=6

%description
KIO worker to discover file systems by DNS-SD (zeroconf)

%files -f %{name}.lang
%{_libdir}/qt6/plugins/kf6/kded/dnssdwatcher.so
%{_libdir}/qt6/plugins/kf6/kio/zeroconf.so
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml
%{_datadir}/metainfo/org.kde.kio_zeroconf.metainfo.xml
%{_datadir}/remoteview/zeroconf.desktop
