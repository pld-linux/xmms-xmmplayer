
%define		org_name	xmmplayer
%define		rcver		pre1

Summary:	Plugin for XMMS that uses mplayer to play video files
Summary(pl):	Wtyczka umo¿liwiaj±ca odtwarzanie filmów
Name:		xmms-%{org_name}
Version:	0.0.5
Release:	0.%{rcver}.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{org_name}-%{version}%{rcver}.tar.gz
URL:		http://thegraveyard.org/xmmplayer.php
Requires:	mplayer
BuildRequires:	automake
BuildRequires:	xmms-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
XMMPlayer is an input plugin for XMMS that allows you to play video
files from within XMMS

%description -l pl
XMMPlayer to wtyczka XMMS'a umo¿liwiaj±ca odtwarzanie filów przy
pomocy XMMS'a

%prep
%setup -q -n %{org_name}-%{version}%{rcver}

%build
%{configure}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS 
%{_libdir}/xmms/Input/*
