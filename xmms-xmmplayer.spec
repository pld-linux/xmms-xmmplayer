
%define		org_name	xmmplayer
%define		rcver		pre1

Summary:	Plugin for XMMS that uses mplayer to play video files
Summary(pl):	Wtyczka dla XMMS-a u¿ywaj±ca mplayera do odtwarzania filmów
Name:		xmms-%{org_name}
Version:	0.1.0
Release:	0..1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{org_name}-%{version}.tar.gz
URL:		http://thegraveyard.org/xmmplayer.php
BuildRequires:	xmms-devel >= 1.2.0
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMPlayer is an input plugin for XMMS that allows you to play video
files from within XMMS (using mplayer).

%description -l pl
XMMPlayer to wtyczka dla XMMS-a umo¿liwiaj±ca odtwarzanie plików z
filmami z poziomu XMMS-a (przy u¿yciu mplayera).

%prep
%setup -q -n %{org_name}-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS 
%attr(755,root,root) %{_libdir}/xmms/Input/*.so
