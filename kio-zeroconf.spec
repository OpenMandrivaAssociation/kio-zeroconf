%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kio-zeroconf
Version: 23.08.4
Release: 2
Summary: KIO worker to discover file systems by DNS-SD (zeroconf)
%if 0%{?git:1}
Source0:        https://invent.kde.org/network/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
License: GPL
Group: System/Libraries
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DNSSD)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)

%description
KIO worker to discover file systems by DNS-SD (zeroconf)

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kio5_zeroconf

%files -f kio5_zeroconf.lang
%{_libdir}/qt5/plugins/kf5/kded/dnssdwatcher.so
%{_libdir}/qt5/plugins/kf5/kio/zeroconf.so
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml
%{_datadir}/metainfo/org.kde.kio_zeroconf.metainfo.xml
%{_datadir}/remoteview/zeroconf.desktop
