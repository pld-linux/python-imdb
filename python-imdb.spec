%define 	module	imdb
Summary:	Python package useful to retrieve and manage the data of the IMDb movie database
Summary(pl.UTF-8):	Pakiet Pythona do uzyskiwania i zarządzania danymi z bazy danych filmów IMDb
Name:		python-%{module}
Version:	4.7
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/imdbpy/IMDbPY-%{version}.tar.gz
# Source0-md5:	4deaed7b55ba3098af5ac559da7dde1a
URL:		http://imdbpy.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-lxml
# SQLAlchemy or SQLObject
Suggests:	python-SQLAlchemy
Suggests:	python-SQLObject
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

rm docs/GPL.txt

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}
mv $RPM_BUILD_ROOT{%{_prefix}%{_sysconfdir},%{_sysconfdir}}/imdbpy.cfg

# fix in setup.py instead
install -d $RPM_BUILD_ROOT%{_datadir}/locale/{en,it,tr,it}/LC_MESSAGES
rm $RPM_BUILD_ROOT%{_prefix}/imdb/locale/*.{pot,po}
mv $RPM_BUILD_ROOT{%{_prefix}/imdb/locale,%{_datadir}/locale}/en/LC_MESSAGES/imdbpy.mo
mv $RPM_BUILD_ROOT{%{_prefix}/imdb/locale,%{_datadir}/locale}/it/LC_MESSAGES/imdbpy.mo
mv $RPM_BUILD_ROOT{%{_prefix}/imdb/locale,%{_datadir}/locale}/tr/LC_MESSAGES/imdbpy.mo

# we use %doc
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

# .py ext is ugly
for a in $RPM_BUILD_ROOT%{_bindir}/*.py; do
	mv $a ${a%.py}
done

# add suffix to commands
for a in $RPM_BUILD_ROOT%{_bindir}/get_* $RPM_BUILD_ROOT%{_bindir}/search_*; do
	d=${a%/*}
	f=${a##*/}

	mv $a $d/imdbpy_$f
done

%find_lang imdbpy

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files -f imdbpy.lang
%defattr(644,root,root,755)
%doc docs/*.txt docs/README.????* docs/goodies
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/imdbpy.cfg
%attr(755,root,root) %{_bindir}/imdbpy_*
%attr(755,root,root) %{_bindir}/imdbpy2sql
%{py_sitedir}/*.egg-info
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/locale
%{py_sitedir}/%{module}/locale/*.py[co]
%dir %{py_sitedir}/%{module}/parser
%{py_sitedir}/%{module}/parser/*.py[co]
%dir %{py_sitedir}/%{module}/parser/http
%{py_sitedir}/%{module}/parser/http/*.py[co]
%dir %{py_sitedir}/%{module}/parser/http/bsouplxml
%{py_sitedir}/%{module}/parser/http/bsouplxml/*.py[co]
%dir %{py_sitedir}/%{module}/parser/mobile
%{py_sitedir}/%{module}/parser/mobile/*.py[co]
%dir %{py_sitedir}/%{module}/parser/sql
%{py_sitedir}/%{module}/parser/sql/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/parser/sql/*.so
