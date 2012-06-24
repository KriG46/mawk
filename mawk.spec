Summary:	An interpreter for the awk programming language
Summary(de):	Mikes neuer Posix AWK-Interpretierer
Summary(es):	Nuevo interpretador (Posix) AWK del Mike
Summary(fr):	Mike's New/Posix AWK Interpreter : interpr�teur AWK
Summary(pl):	Interpreter j�zyka programowania awk
Summary(pt_BR):	Novo interpretador (Posix) AWK do Mike
Summary(ru):	������������� ����� ���������������� awk
Summary(tr):	Posix AWK Yorumlay�c�s�
Summary(uk):	������������� ���� ������������� awk
Name:		mawk
Version:	1.3.3
Release:	32
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.fu-berlin.de/pub/unix/languages/mawk/%{name}%{version}.tar.gz
# Source0-md5:	ad46743641924e1234b2bfba92641085
Source1:	%{name}.1.pl
Patch0:		%{name}-fix_%{name}_path.patch
Patch1:		%{name}-ac-ac.patch
Patch2:		%{name}-debian.patch
Patch3:		%{name}-resolve.patch
BuildRequires:	autoconf
BuildRequires:	automake
%{?BOOT:BuildRequires:	glibc-static}
Provides:	/bin/awk
Provides:	awk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_bindir		/bin

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

%description -l es
Mawk es una versi�n del awk, que es un fuerte programa procesador de
texto. En algunas �reas mawk puede superar gawk, que es el programa
awk padr�n del Linux.

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

%description -l pt_BR
Mawk � uma vers�o do awk, que � um poderoso programa processador de
texto. Em algumas �reas mawk pode superar gawk, que � o programa awk
padr�o do Linux.

%description -l ru
Mawk - ��� ������ ����� ���������������� awk, ������� ����������� ���
��������� ������. Mawk ����� ���������� ���������� ���������
������������ awk � ������ ������� gawk, ����������� ��������� awk ���
Linux. Mawk ������������� POSIX 1003.2 (draft 11.3) ����������� �����
awk.

%description -l tr
Mawk, �ok g��l� bir metin i�leme program� olan awk'�n bir s�r�m�d�r.
Baz� durumlarda Linux un standart awk program� olan gawk'dan daha
�st�nd�r.

%description -l uk
Mawk - �� ���Ӧ� ���� ������������� awk, ��������� ����������� ���
������� ������. Mawk ��� ��������� ���̦��æ� ������ ����������� awk �
���Ħ ������� �� gawk, ���������� �������� awk ��� Linux. Mawk
צ���צ��� POSIX 1003.2 (draft 11.3) ���������� ���� awk.

%package BOOT
Summary:	An interpreter for the awk programming language - BOOT
Summary(de):	Mikes neuer Posix AWK-Interpretierer - BOOT
Summary(fr):	Mike's New/Posix AWK Interpreter : interpr�teur AWK - BOOT
Summary(pl):	Interpreter j�zyka programowania awk - BOOT
Summary(tr):	Posix AWK Yorumlay�c�s� - BOOT
Group:		Applications/Text

%description BOOT
Bootdisk awk version.

%description BOOT -l pl
Wersja awka na bootkietk�.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoupdate mawk.ac.m4
autoupdate configure.in
%{__aclocal}
%{__autoconf}
%configure
%if %{?BOOT:1}%{!?BOOT:0}
%{__make} MATHLIB=/usr/lib/libm.a
mv -f mawk mawk.BOOT
%{__make} clean
%endif
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,pl/man1},%{_examplesdir}/%{name}-%{version},/bin}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

ln -sf mawk $RPM_BUILD_ROOT%{_bindir}/awk
echo ".so mawk.1" > $RPM_BUILD_ROOT%{_mandir}/man1/awk.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/mawk.1
echo ".so mawk.1" > $RPM_BUILD_ROOT%{_mandir}/pl/man1/awk.1

mv -f examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk/bin
install mawk.BOOT $RPM_BUILD_ROOT%{_libdir}/bootdisk/bin/awk
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGMENT CHANGES README
%attr(755,root,root) %{_bindir}/mawk
%attr(755,root,root) %{_bindir}/awk
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_examplesdir}/%{name}-%{version}

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bootdisk/bin/awk
%endif
