%define 	module	imdb

Summary:	Python package useful to retrieve and manage the data of the IMDb movie database
Summary(pl.UTF-8):	Pakiet Pythona do uzyskiwania i zarządzania danymi z bazy danych filmów IMDb
Name:		python-%{module}
Version:	3.5
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/imdbpy/IMDbPY-%{version}.tar.gz
# Source0-md5:	914b5f23c8e3649cb747c9fe8522c544
URL:		http://imdbpy.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMDbPY is a Python package useful to retrieve and manage the data of
the IMDb movie database. IMDbPY aims to provide an easy way to access
the IMDb's database using a Python script. Platform-independent and
written in pure Python, it's theoretically independent from the data
source (since IMDb provides two or three different interfaces to their
database). IMDbPY is mainly intended for programmers and developers
who want to build their Python programs using the IMDbPY package, but
some example scripts - useful for simple users - are included.

%description -l pl.UTF-8
IMDbPY to pythonowy pakiet przydatny do uzyskiwania i zarządzania
danymi z bazy danych filmów IMDb. Celem IMDbPY jest dostarczenie
łatwego sposobu na dostęp do baz IMDb z poziomu skryptów Pythona. Jest
niezależny od platformy i napisany w czystym Pythonie, więc jest
teoretycznie niezależny od źródła danych (jako że IMDb dostarcza dwa
lub trzy różne interfejsy do ich bazy). IMDbPY jest przeznaczony
głównie dla programistów chcących tworzyć programy przy użyciu tego
pakietu, ale załączonych jest także kilka przykładowych skryptów
przydatnych dla zwykłych użytkowników.

%prep
%setup -q -n IMDbPY-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2 \
	--install-purelib=%{py_sitedir}

find $RPM_BUILD_ROOT%{py_sitedir} -type f -name "*.py" | xargs rm
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/AUTHOR.txt docs/CONTRIBUTORS.txt docs/CREDITS.txt docs/Changelog.txt docs/DISCLAIMER.txt docs/README.* docs/TODO.txt
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/parser
%{py_sitedir}/%{module}/parser/*.py[co]
%dir %{py_sitedir}/%{module}/parser/http
%{py_sitedir}/%{module}/parser/http/*.py[co]
%dir %{py_sitedir}/%{module}/parser/common
%{py_sitedir}/%{module}/parser/common/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/parser/common/cutils.so
%dir %{py_sitedir}/%{module}/parser/local
%{py_sitedir}/%{module}/parser/local/*.py[co]
%dir %{py_sitedir}/%{module}/parser/mobile
%{py_sitedir}/%{module}/parser/mobile/*.py[co]
%dir %{py_sitedir}/%{module}/parser/sql
%{py_sitedir}/%{module}/parser/sql/*.py[co]
