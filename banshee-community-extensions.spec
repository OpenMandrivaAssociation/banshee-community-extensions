%define name	banshee-community-extensions
%define version	2.4.0
%define release 4

%define banshee_version	2.4.0

Summary:	Contributed extensions for the Banshee media player
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	http://download.banshee.fm/%{name}/%{version}/%{name}-%{version}.tar.bz2
#gw mirage is GPL, all others MIT
License:	MIT and GPLv2+
Group:		Sound
Url:		https://banshee-project.org/download/extensions/
BuildRequires:	banshee-devel >= %{banshee_version}
BuildRequires:	mono-devel
BuildRequires:	lirc-devel
BuildRequires:	gnome-sharp2-devel
BuildRequires:	notify-sharp-devel
BuildRequires:	webkit-sharp-devel
BuildRequires:	clutter-sharp-devel
#gw not packaged:
#BuildRequires: ubuntuone-sharp
BuildRequires:	libfftw-devel
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	intltool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	locales-en
#gw for the git snapshot:
BuildRequires:	pkgconfig(gconf-2.0)
Suggests:	gstreamer0.10-plugins-ugly
Suggests:	gstreamer0.10-flac
Suggests:	gstreamer0.10-plugins-good

%description
The following extensions are developed mostly by third-parties, and
are not vetted by the core Banshee developers (though that will
probably change over time).

 * Alarm Clock – You can use Banshee to wake up or go to sleep to a
   selection of your own music.
 * Awn – Sets the current album cover as banshee icon in awn.
 * ClutterFlow ? Browse your albums in a cover art flip-book-like view.
 * Cover Wallpaper – Sets the current playing album cover as the GNOME
   desktop wallpaper.
 * Karaoke – Filter the singers voice out of songs 
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
%autopatch -p1

%build
#gw to make mcs accept Unicode symbols
export LC_ALL=en_US.UTF-8
%configure2_5x \
	--with-vendor-build-id="%{_vendor} %{distro_release}" \
	--disable-static
%make

%install
%makeinstall_std

%find_lang %name --with-gnome --all-name

# we don't want these
rm -f %buildroot%{_libdir}/banshee/Extensions/lib*.la

ln -sf %{_libdir}/clutter-sharp/* %{buildroot}%{_libdir}/banshee/Extensions/

%files -f %name.lang
%doc README NEWS AUTHORS
%{_libdir}/banshee/Extensions/Banshee.AlarmClock.dll*
%{_libdir}/banshee/Extensions/Banshee.AlbumArtWriter.dll*
%{_libdir}/banshee/Extensions/Banshee.Ampache.dll*
%{_libdir}/banshee/Extensions/Banshee.Awn.dll*
%{_libdir}/banshee/Extensions/Banshee.ClutterFlow.dll*
%{_libdir}/banshee/Extensions/Banshee.CoverWallpaper.dll*
%{_libdir}/banshee/Extensions/Banshee.DuplicateSongDetector.dll*
%{_libdir}/banshee/Extensions/Banshee.FolderSync.dll*
%{_libdir}/banshee/Extensions/Banshee.Jamendo.dll*
%{_libdir}/banshee/Extensions/Banshee.Karaoke.dll*
%{_libdir}/banshee/Extensions/Banshee.LastfmFingerprint.dll*
%{_libdir}/banshee/Extensions/Banshee.LCD.dll*
%{_libdir}/banshee/Extensions/Banshee.Lirc.dll*
%{_libdir}/banshee/Extensions/Banshee.LiveRadio.dll*
%{_libdir}/banshee/Extensions/Banshee.Lyrics.dll*
%{_libdir}/banshee/Extensions/Banshee.Magnatune.dll*
%{_libdir}/banshee/Extensions/Banshee.Mirage.dll*
%{_libdir}/banshee/Extensions/Banshee.RadioStationFetcher.dll*
%{_libdir}/banshee/Extensions/Banshee.RandomByLastfm.dll*
%{_libdir}/banshee/Extensions/Banshee.Streamrecorder.dll*
%{_libdir}/banshee/Extensions/Banshee.Telepathy.dll*
%{_libdir}/banshee/Extensions/ClutterFlow.dll*
%{_libdir}/banshee/Extensions/Mirage.dll*
%{_libdir}/banshee/Extensions/clutter*sharp.dll*
%{_libdir}/banshee/Extensions/glib-sharp.dll*
%{_libdir}/banshee/Extensions/liblastfmfpbridge.so
%{_libdir}/banshee/Extensions/liblircglue.so
%{_libdir}/banshee/Extensions/libmirageaudio.so
%{_datadir}/%{name}/icons/hicolor/*/categories/jamendo.*
