%define name banshee-community-extensions
%define version 1.6.1
%define release %mkrel 1

Summary: Contributed extensions for the Banshee media player
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.banshee-project.org/%name/%version/%{name}-%{version}.tar.bz2
#gw mirage is GPL, all others MIT
License: MIT and GPLv2+
Group: Sound
Url: http://banshee-project.org/download/extensions/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: banshee >= 1.5.5
BuildRequires: mono-devel
BuildRequires: lirc-devel
BuildRequires: gnome-sharp2-devel
BuildRequires: notify-sharp
BuildRequires: webkit-sharp-devel
#gw not packaged:
#BuildRequires: clutter-sharp
#BuildRequires: ubuntuone-sharp
BuildRequires: libfftw-devel
BuildRequires: sqlite3-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: libsamplerate-devel
BuildRequires: intltool
BuildRequires: locales-en
Provides: banshee-mirage
Obsoletes: banshee-mirage
Suggests: gstreamer0.10-plugins-ugly
Suggests: gstreamer0.10-flac
Suggests: gstreamer0.10-plugins-good

%description
The following extensions are developed mostly by third-parties, and
are not vetted by the core Banshee developers (though that will
probably change over time).

 * Alarm Clock – You can use Banshee to wake up or go to sleep to a
   selection of your own music.
 * Awn – Sets the current album cover as banshee icon in awn.
 * Cover Wallpaper – Sets the current playing album cover as the GNOME
   desktop wallpaper.
 * LCD – Display track info on a LCD using LCDproc.
 * Lirc – Control Banshee via a normal (infrared) remote
      control. Requires LIRC.
 * Live Radio – Another way to discover internet radio stations.
 * Lyrics – Fetches and displays lyrics for the current song.
 * Magnatune – Listen to streamed music from Magnatune.com.
 * Mirage – Adds playback shuffle-by-similar and Auto DJ fill-by-similar
   modes, based on songs' acoustic similarity.
 * Radio Station Fetcher – Fetch radio stations from shoutcast.com and
   xiph.org.  Stream Recorder – Record internet-radio streams.
 * Telepathy – Browse your IM friends' music library, download or
   stream their tracks and share what you're listening to.

%prep
%setup -q

%build
#gw to make mcs accept Unicode symbols
export LC_ALL=en_US.UTF-8
%configure2_5x --with-vendor-build-id="Mandriva Linux %mandriva_release"
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name
rm -f %buildroot%_libdir/banshee-1/Extensions/lib*a

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc README
%_libdir/banshee-1/Extensions/Banshee.AlarmClock.dll*
%_libdir/banshee-1/Extensions/Banshee.Awn.dll*
%_libdir/banshee-1/Extensions/Banshee.CoverWallpaper.dll*
%_libdir/banshee-1/Extensions/Banshee.LCD.dll*
%_libdir/banshee-1/Extensions/Banshee.Lirc.dll*
%_libdir/banshee-1/Extensions/Banshee.LiveRadio.dll*
%_libdir/banshee-1/Extensions/Banshee.Lyrics.dll*
%_libdir/banshee-1/Extensions/Banshee.Magnatune.dll*
%_libdir/banshee-1/Extensions/Banshee.Mirage.dll*
%_libdir/banshee-1/Extensions/Banshee.RadioStationFetcher.dll*
%_libdir/banshee-1/Extensions/Banshee.Streamrecorder.dll*
%_libdir/banshee-1/Extensions/Banshee.Telepathy.dll*
%_libdir/banshee-1/Extensions/Mirage.dll*
%_libdir/banshee-1/Extensions/liblircglue.so
%_libdir/banshee-1/Extensions/libmirageaudio.so

