Name:		fcitx-libpinyin
Version:	0.5.4
Release:	1
Summary:	Libpinyin Wrapper for Fcitx
License:	GPLv2+
URL:		https://fcitx-im.org/wiki/Libpinyin
Source0:	http://download.fcitx-im.org/fcitx-libpinyin/%{name}-%{version}_dict.tar.xz

BuildRequires:	gcc
BuildRequires:	libpinyin-devel >= 1.9.91
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libpinyin-devel
BuildRequires:	libpinyin-tools, glib2-devel, fcitx
BuildRequires:	qt5-qtwebengine-devel, dbus-devel
BuildRequires:	fcitx-qt5-devel >= 1.1
Requires:	    fcitx

%description
Fcitx-libpinyin is a libpinyin Wrapper for Fcitx.

Libpinyin is a Frontend of the Intelligent Pinyin IME Backend.


%prep
%setup -q -n %{name}-%{version}

%build
mkdir -pv build
pushd build
%cmake ..
make VERBOSE=1 %{?_smp_mflags}
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/fcitx/%{name}.so
%{_libdir}/fcitx/qt/*.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/imicon/*
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/inputmethod/*-libpinyin.conf
%{_datadir}/fcitx/libpinyin/
%{_datadir}/icons/hicolor/48x48/status/fcitx-*.png

%changelog
* Tue Sep 13 2022 misaka00251 <misaka00251@misakanet.cn> - 0.5.4-1
- Upgrade package version & changelog cleanup

* Fri Sep 18 2020 Luke Yue <lukedyue@gmail.com> - 0.5.3-12
- Adapt for openEuler
