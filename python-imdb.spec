%include	/usr/lib/rpm/macros.python
%define 	module imdb

Summary:	Python package useful to retrieve and manage the data of the IMDb movie database
Summary(pl):	Pakiet Pythona do uzyskiwania i zarz±dzania danymi z bazy danych filmów IMDb
Name:		python-%{module}
Version:	1.2
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/imdbpy/imdbpy-%{version}.tar.gz
# Source0-md5:	0dfd175efa468926fd2753cf2130de5d
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

%description -l pl
IMDbPY to pythonowy pakiet przydatny do uzyskiwania i zarz±dzania
danymi z bazy danych filmów IMDb. Celem IMDbPY jest dostarczenie
³atwego sposobu na dostêp do baz IMDb z poziomu skryptów Pythona. Jest
niezale¿ny od platformy i napisany w czystym Pythonie, wiêc jest
teoretycznie niezale¿ny od ¼ród³a danych (jako ¿e IMDb dostarcza dwa
lub trzy ró¿ne interfejsy do ich bazy). IMDbPY jest przeznaczony
g³ównie dla programistów chc±cych tworzyæ programy przy u¿yciu tego
pakietu, ale za³±czonych jest tak¿e kilka przyk³adowych skryptów
przydatnych dla zwyk³ych u¿ytkowników.

%prep
%setup -q -n IMDbPY-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/parser
%{py_sitescriptdir}/%{module}/parser/*.py[co]
%dir %{py_sitescriptdir}/%{module}/parser/http
%{py_sitescriptdir}/%{module}/parser/http/*.py[co]
