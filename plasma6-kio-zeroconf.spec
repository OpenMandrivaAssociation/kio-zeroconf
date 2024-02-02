%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma6-kio-zeroconf
Version: 24.01.95
Release: 1
Summary: KIO worker to discover file systems by DNS-SD (zeroconf)
%if 0%{?git:1}
Source0:        https://invent.kde.org/network/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/kio-zeroconf-%{version}.tar.xz
%endif
License: GPL
Group: System/Libraries
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)

%description
KIO worker to discover file systems by DNS-SD (zeroconf)

%prep
%autosetup -p1 -n kio-zeroconf-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DQT_MAJOR_VERSION=6 \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kio5_zeroconf

%files -f kio5_zeroconf.lang
%{_libdir}/qt6/plugins/kf6/kded/dnssdwatcher.so
%{_libdir}/qt6/plugins/kf6/kio/zeroconf.so
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml
%{_datadir}/metainfo/org.kde.kio_zeroconf.metainfo.xml
%{_datadir}/remoteview/zeroconf.desktop
