
%define		org_name	xmmplayer

Summary:	Plugin for XMMS that uses mplayer to play video files
Summary(pl):	Wtyczka dla XMMS-a u�ywaj�ca mplayera do odtwarzania film�w
Name:		xmms-%{org_name}
Version:	0.3.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://thegraveyard.org/files/%{org_name}-%{version}.tar.bz2
# Source0-md5:	4103a72283590474a98fe6ab60439efe
URL:		http://thegraveyard.org/xmmplayer.php
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.0
Requires:	mplayer
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMPlayer is an input plugin for XMMS that allows you to play video
files from within XMMS (using mplayer).

%description -l pl
XMMPlayer to wtyczka dla XMMS-a umo�liwiaj�ca odtwarzanie plik�w z
filmami z poziomu XMMS-a (przy u�yciu mplayera).

%prep
%setup -q -n %{org_name}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{xmms_input_plugindir}/libxmmplayer.*
