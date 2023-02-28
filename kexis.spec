Summary:	Open source lossless WAV file compressor
Summary(pl.UTF-8):	Bezstratny kompresor plików WAV o otwartych źródłach
Name:		kexis
Version:	0.2.2
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	https://downloads.sourceforge.net/kexis/%{name}-%{version}.tgz
# Source0-md5:	87cd9bb0ef53bc0f7ed44d148011785a
URL:		https://sourceforge.net/projects/kexis/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open source lossless WAV file compressor.

%description -l pl.UTF-8
Bezstratny kompresor plików WAV o otwartych źródłach.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CC_OPTS="%{rpmcflags} %{rpmcppflags} -Wall" \
	LD_OPTS="%{rpmldflags}" \
	PROFILE_OPTS="-lm"

%install
rm -rf $RPM_BUILD_ROOT

install -D kexis $RPM_BUILD_ROOT%{_bindir}/kexis

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{README.txt,todo.txt}
%attr(755,root,root) %{_bindir}/kexis
