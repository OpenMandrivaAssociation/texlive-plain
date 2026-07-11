%global tl_name plain
%global tl_revision 75712

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1415926535
Release:	%{tl_revision}.1
Summary:	The Plain TeX format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/base
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plain.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Contains files used to build the Plain TeX format, as described in the
TeXbook, together with various supporting files (some also discussed in
the book).

