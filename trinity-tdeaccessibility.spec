%bcond clang 1
%bcond akode 1
%bcond libmad 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_pkg tdeaccessibility
%define tde_prefix /opt/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-tdeaccessibility
Summary:		Trinity Desktop Environment - Accessibility
Version:		14.1.5
Release:		3
Group:			System/GUI/Other
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:	  cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INCLUDE_PATH=%{tde_prefix}/include/tde
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/pkgconfig
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-arts-devel >= 1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tdemultimedia-devel >= %{version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	desktop-file-utils
BuildRequires:	fdupes

# AUDIOFILE support
BuildRequires:	pkgconfig(audiofile)

# AKODE support
%{?with_akode:BuildRequires: trinity-akode-devel}

# MAD support
%ifarch %{ix86} %{x86_64}
%{?with_libmad:BuildRequires: libakode_mpeg_decoder}
%endif

# ALSA support
BuildRequires:  pkgconfig(alsa)

# GLIB2 support
BuildRequires:  pkgconfig(glib-2.0)

# JPEG support
BuildRequires:  pkgconfig(libjpeg)

# XCB support
BuildRequires:  pkgconfig(xcb)

# XAU support
BuildRequires:  pkgconfig(xau)

BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xrender)

Obsoletes:		trinity-kdeaccessibility < %{EVRD}
Provides:		trinity-kdeaccessibility = %{EVRD}
Obsoletes:		trinity-kdeaccessibility-libs < %{EVRD}
Provides:		trinity-kdeaccessibility-libs = %{EVRD}

Requires: trinity-tde-icons-mono = %{EVRD}
Requires: trinity-kbstate = %{EVRD}
Requires: trinity-kmag = %{EVRD}
Requires: trinity-kmousetool = %{EVRD}
Requires: trinity-kmouth = %{EVRD}
Requires: trinity-ksayit = %{EVRD}
Requires: trinity-kttsd = %{EVRD}
Requires: trinity-kttsd-contrib-plugins = %{EVRD}

%description
Included with this package are:
* kmag, a screen magnifier,
* kmousetool, a program for people whom it hurts to click the mouse,
* kmouth, program that allows people who have lost their voice
  to let their computer speak for them.

%files

##########

%package -n trinity-tde-icons-mono
Summary:	A monochromatic icons theme for TDE
Group:		System/GUI/Other

Obsoletes:	trinity-kde-icons-mono < %{EVRD}
Provides:	trinity-kde-icons-mono = %{EVRD}

%description -n trinity-tde-icons-mono
A monochromatic icon theme for TDE, designed for accessibility purposes.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-tde-icons-mono
%defattr(-,root,root,-)
%{tde_prefix}/share/icons/mono/

##########

%package -n trinity-kbstate
Summary:	A keyboard status applet for TDE
Group:		System/GUI/Other

%description -n trinity-kbstate
A panel applet that displays the keyboard status.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-kbstate
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kbstate_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/kbstate_panelapplet.so
%{tde_prefix}/share/apps/kbstateapplet/
%{tde_prefix}/share/apps/kicker/applets/kbstateapplet.desktop

##########

%package -n trinity-kmag
Summary:	A screen magnifier for TDE
Group:		System/GUI/Other

%description -n trinity-kmag
TDE's screen magnifier tool.

You can use KMagnifier to magnify a part of the screen just as you would use 
a lens to magnify a newspaper fine-print or a photograph.  This application is
useful for a variety of people: from researchers to artists to web-designers to
people with low vision.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-kmag
%defattr(-,root,root,-)
%{tde_prefix}/bin/kmag
%{tde_prefix}/share/applications/tde/kmag.desktop
%{tde_prefix}/share/apps/kmag/
%{tde_prefix}/share/icons/hicolor/*/apps/kmag.png
%{tde_prefix}/share/icons/locolor/*/apps/kmag.png
%{tde_prefix}/share/doc/tde/HTML/en/kmag/
%{tde_prefix}/share/man/man1/kmag.1*

##########

%package -n trinity-kmousetool
Summary:	TDE mouse manipulation tool for the disabled
Group:		System/GUI/Other

%description -n trinity-kmousetool
KMouseTool clicks the mouse whenever the mouse cursor pauses briefly. It was
designed to help those with repetitive strain injuries, for whom pressing
buttons hurts.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-kmousetool
%defattr(-,root,root,-)
%{tde_prefix}/bin/kmousetool
%{tde_prefix}/share/applications/tde/kmousetool.desktop
%{tde_prefix}/share/apps/kmousetool/
%{tde_prefix}/share/icons/hicolor/*/apps/kmousetool.png
%{tde_prefix}/share/doc/tde/HTML/en/kmousetool/
%{tde_prefix}/share/man/man1/kmousetool.1*

##########

%package -n trinity-kmouth
Summary:	A type-and-say KDE frontend for speech synthesizers
Group:		System/GUI/Other

%description -n trinity-kmouth
KDE's type-and-say frontend for speech synthesizers.

It includes a history of spoken sentences from which the user can select
sentences to be re-spoken.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-kmouth
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/kmouthrc
%{tde_prefix}/bin/kmouth
%{tde_prefix}/share/applications/tde/kmouth.desktop
%{tde_prefix}/share/apps/kmouth/
%{tde_prefix}/share/icons/hicolor/*/actions/speak.png
%{tde_prefix}/share/icons/hicolor/*/actions/nospeak.png
%{tde_prefix}/share/icons/hicolor/*/apps/kmouth.png
%{tde_prefix}/share/icons/locolor/*/actions/speak.png
%{tde_prefix}/share/icons/locolor/*/apps/kmouth.png
%{tde_prefix}/share/doc/tde/HTML/en/kmouth/
%{tde_prefix}/share/man/man1/kmouth.1*

##########

%package -n trinity-ksayit
Summary:	A frontend for the TDE Text-to-Speech system
Group:		System/GUI/Other

%description -n trinity-ksayit
Text-to-speech front-end to kttsd.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-ksayit
%defattr(-,root,root,-)
%{tde_prefix}/bin/ksayit
%{tde_prefix}/%{_lib}/trinity/libFreeverb_plugin.la
%{tde_prefix}/%{_lib}/trinity/libFreeverb_plugin.so
%{tde_prefix}/%{_lib}/libKTTSD_Lib.so.*
%{tde_prefix}/share/applications/tde/ksayit.desktop
%{tde_prefix}/share/apps/ksayit/
%{tde_prefix}/share/icons/hicolor/*/apps/ksayit.png
%{tde_prefix}/share/icons/hicolor/32x32/apps/ksayit_clipempty.png
%{tde_prefix}/share/icons/hicolor/32x32/apps/ksayit_talking.png
%{tde_prefix}/share/services/ksayit_libFreeverb.desktop
%{tde_prefix}/share/servicetypes/ksayit_libFreeverb_service.desktop
%{tde_prefix}/share/doc/tde/HTML/en/ksayit/
%{tde_prefix}/share/man/man1/ksayit.1*

##########

%package -n trinity-kttsd
Summary:	A Text-to-Speech system for TDE
Group:		System/GUI/Other

%description -n trinity-kttsd
The KDE Text-to-Speech system is a plugin based service that allows any KDE
(or non-KDE) application to speak using the DCOP interface.

ksayit and kmouth are useful front-ends for this capability, while one of
festival, flite, and epos are essential back-ends.

This package is part of Trinity, as a component of the TDE accessibility module.

Homepage: http://accessibility.kde.org/developer/kttsd

%files -n trinity-kttsd
%defattr(-,root,root,-)
%{tde_prefix}/bin/kttsd
%{tde_prefix}/bin/kttsmgr
%{tde_prefix}/%{_lib}/trinity/kcm_kttsd.la
%{tde_prefix}/%{_lib}/trinity/kcm_kttsd.so
%{tde_prefix}/%{_lib}/trinity/tdetexteditor_kttsd.la
%{tde_prefix}/%{_lib}/trinity/tdetexteditor_kttsd.so
%if %{with akode}
%{tde_prefix}/%{_lib}/trinity/libkttsd_akodeplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_akodeplugin.so
%endif
%{tde_prefix}/%{_lib}/trinity/libkttsd_alsaplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_alsaplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsd_artsplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_artsplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsd_commandplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_commandplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsd_eposplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_eposplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsd_festivalintplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_festivalintplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsd_fliteplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_fliteplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsd_sbdplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_sbdplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsd_stringreplacerplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_stringreplacerplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsd_talkerchooserplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_talkerchooserplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsd_xmltransformerplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_xmltransformerplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsjobmgrpart.la
%{tde_prefix}/%{_lib}/trinity/libkttsjobmgrpart.so
%{tde_prefix}/%{_lib}/libkttsd.so.*
%{tde_prefix}/share/applications/tde/kcmkttsd.desktop
%{tde_prefix}/share/applications/tde/kttsmgr.desktop
%{tde_prefix}/share/apps/tdetexteditor_kttsd/
%exclude %{tde_prefix}/share/apps/kttsd/hadifix/xslt/SSMLtoTxt2pho.xsl
%{tde_prefix}/share/apps/kttsd/
%{tde_prefix}/share/icons/hicolor/16x16/actions/female.png
%{tde_prefix}/share/icons/hicolor/16x16/actions/male.png
%{tde_prefix}/share/icons/hicolor/*/apps/kttsd.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmkttsd.png
%{tde_prefix}/share/services/tdetexteditor_kttsd.desktop
%{tde_prefix}/share/services/kttsd.desktop
%{?with_akode:%{tde_prefix}/share/services/kttsd_akodeplugin.desktop}
%{tde_prefix}/share/services/kttsd_alsaplugin.desktop
%{tde_prefix}/share/services/kttsd_artsplugin.desktop
%{tde_prefix}/share/services/kttsd_commandplugin.desktop
%{tde_prefix}/share/services/kttsd_eposplugin.desktop
%{tde_prefix}/share/services/kttsd_festivalintplugin.desktop
%{tde_prefix}/share/services/kttsd_fliteplugin.desktop
%{tde_prefix}/share/services/kttsd_sbdplugin.desktop
%{tde_prefix}/share/services/kttsd_stringreplacerplugin.desktop
%{tde_prefix}/share/services/kttsd_talkerchooserplugin.desktop
%{tde_prefix}/share/services/kttsd_xmltransformerplugin.desktop
%{tde_prefix}/share/services/kttsjobmgr.desktop
%{tde_prefix}/share/servicetypes/kttsd_audioplugin.desktop
%{tde_prefix}/share/servicetypes/kttsd_filterplugin.desktop
%{tde_prefix}/share/servicetypes/kttsd_synthplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kttsd/
%{tde_prefix}/share/man/man1/kttsd.1*
%{tde_prefix}/share/man/man1/kttsmgr.1*

##########

%package -n trinity-kttsd-contrib-plugins
Summary:	The TDE Text-to-Speech system
Group:		System/GUI/Other
Requires:	trinity-kttsd = %{EVRD}

%description -n trinity-kttsd-contrib-plugins
kttsd synthetizer plugins that depends on non-free software :
* FreeTTS plugin.
* Hadifix (mbrola/txt2pho) plugin.
Those plugins will require manual installation of third party,
non free software to work.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-kttsd-contrib-plugins
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/libkttsd_freettsplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_freettsplugin.so
%{tde_prefix}/%{_lib}/trinity/libkttsd_hadifixplugin.la
%{tde_prefix}/%{_lib}/trinity/libkttsd_hadifixplugin.so
%{tde_prefix}/share/apps/kttsd/hadifix/xslt/SSMLtoTxt2pho.xsl
%{tde_prefix}/share/services/kttsd_freettsplugin.desktop
%{tde_prefix}/share/services/kttsd_hadifixplugin.desktop

##########

%package devel
Summary:	Development files for tdeaccessibility
Group:		Development/Libraries/X11
Requires:	%{name} = %{EVRD}
Requires:	trinity-tdelibs-devel >= %{version}
Requires:	pkgconfig(libjpeg)
Requires:	pkgconfig(libpng)

Obsoletes:		trinity-kdeaccessibility-devel < %{EVRD}
Provides:		trinity-kdeaccessibility-devel = %{EVRD}

%description devel
This package contains the development file for TDE accessibility 
programs.

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkttsd.la
%{tde_prefix}/%{_lib}/libkttsd.so
%{tde_prefix}/%{_lib}/libKTTSD_Lib.la
%{tde_prefix}/%{_lib}/libKTTSD_Lib.so
%{tde_prefix}/include/tde/ksayit_fxplugin.h

%prep -a
# Update icons for some control center modules
%__sed -i "kttsd/kcmkttsmgr/kcmkttsd.desktop" -e "s|^Icon=.*|Icon=kcmkttsd|"


%conf -p
unset QTDIR QTLIB QTINC
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"

%install -a
# Adds missing icons in 'hicolor' theme
# These icons are copied from 'crystalsvg' theme, provided by 'tdelibs'.
%__mkdir_p "%{?buildroot}%{tde_prefix}/share/icons/hicolor/"{16x16,22x22,32x32,48x48,64x64,128x128}"/apps/"
pushd "%{?buildroot}%{tde_prefix}/share/icons"
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/apps/kttsd.png  hicolor/"$i"x"$i"/apps/kttsd.png    ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/apps/kttsd.png  hicolor/"$i"x"$i"/apps/kcmkttsd.png ;done
popd

# Avoid conflict with tdelibs
%__rm -f %{?buildroot}%{tde_prefix}/share/icons/crystalsvg/*/apps/kttsd.png
%__rm -f %{?buildroot}%{tde_prefix}/share/icons/crystalsvg/scalable/apps/kttsd.svgz

# Links duplicate files
%fdupes "%{?buildroot}%{tde_prefix}/share"

