%include	/usr/lib/rpm/macros.python
%define 	module imdb

Summary:	Python package useful to retrieve and manage the data of the IMDb movie database.
Name:		python-%{module}
Version:	1.0
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/imdbpy/imdbpy-%{version}.tar.gz
# Source0-md5:	fb25af8fec6fd4fa2523a9bf2ec1f96c
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
%{py_sitescriptdir}/%{module}/parser/*.py[co]
%{py_sitescriptdir}/%{module}/parser/http/*.py[co]
