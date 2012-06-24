#
# --with smath - links libm statically (its smaller than mawk+libm)
#
Summary:	An interpreter for the awk programming language
Summary(de):	Mikes neuer Posix AWK-Interpretierer
Summary(fr):	Mike's New/Posix AWK Interpreter : interpr�teur AWK
Summary(pl):	Interpreter j�zyka programowania awk
Summary(tr):	Posix AWK Yorumlay�c�s�
Name:		mawk
Version:	1.3.3
Release:	17
License:	GPL
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narz�dzia/Tekst
Source0:	ftp://ftp.whidbey.net/pub/brennan/%{name}%{version}.tar.gz
Patch0:		mawk-fix_mawk_path.patch
Provides:	/bin/awk
Provides:	awk
%{!?bcond_off_smath:BuildRequires: glibc-static}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
Mawk is a version of the awk programming language. Awk interprets a
special-purpose programming language to do quick text pattern matching
and reformatting. Mawk improves on awk in certain ways and can
sometimes outperform gawk, the standard awk program for Linux. Mawk
conforms to the POSIX 1003.2 (draft 11.3) definition of awk.

%description -l de
Mawk ist eine Version von awk, einem leistungsf�higen
Textverarbeitungsprogramm. In bestimmten Bereichen leistet mawk mehr
als gawk, das Standard-awk-Programm auf Linux.

%description -l fr
mawk est une version d'awk, un puissant programme de traitement du
texte. Dans certains cas, mawk peut �tre sup�rieur � gawk, qui est le
programme awk standard sur Linux

%description -l pl
Mawk jest wersj� interpretera j�zyka programowania awk. Awk jest
specjalizowanym j�zykiem programowania do szybkiego przetwarzania
tekst�w. Mawk w pewien spos�b ulepsza awk i czasem przerasta nawet
gawk - standardowy interpreter awk-a w Linuksie. Mawk jest zgodny ze
standardem j�zyka awk opisanym w POSIX 1003.2 (draft 11.3).

%description -l tr
Mawk, �ok g��l� bir metin i�leme program� olan awk'�n bir s�r�m�d�r.
Baz� durumlarda Linux un standart awk program� olan gawk'dan daha
�st�nd�r.

%prep
%setup -q
%patch0 -p1

%build
autoconf
%configure
%{__make} %{!?bcond_off_smath:MATHLIB=/usr/lib/libm.a}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_examplesdir}/%{name},/bin}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

ln -s mawk $RPM_BUILD_ROOT%{_bindir}/awk
echo ".so mawk.1" > $RPM_BUILD_ROOT%{_mandir}/man1/awk.1

mv examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf ACKNOWLEDGMENT CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/mawk
%attr(755,root,root) /bin/awk
%{_examplesdir}/%{name}
%{_mandir}/man1/*
