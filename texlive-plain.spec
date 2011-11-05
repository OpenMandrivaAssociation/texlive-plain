# revision 20544
# category Package
# catalog-ctan /macros/plain/base
# catalog-date 2009-06-23 17:13:15 +0200
# catalog-license knuth
# catalog-version 3.141592653
Name:		texlive-plain
Version:	3.141592653
Release:	1
Summary:	The Plain TeX format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/base
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plain.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
Contains files used to build the Plain TeX format, as described
in the TeXbook, together with various supporting files (some
also discussed in the book).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/plain/plaintex.ist
%{_texmfdistdir}/tex/plain/base/fontchart.tex
%{_texmfdistdir}/tex/plain/base/gkpmac.tex
%{_texmfdistdir}/tex/plain/base/letter.tex
%{_texmfdistdir}/tex/plain/base/list.tex
%{_texmfdistdir}/tex/plain/base/llist.tex
%{_texmfdistdir}/tex/plain/base/manmac.tex
%{_texmfdistdir}/tex/plain/base/mftmac.tex
%{_texmfdistdir}/tex/plain/base/mptmac.tex
%{_texmfdistdir}/tex/plain/base/picmac.tex
%{_texmfdistdir}/tex/plain/base/plain.tex
%{_texmfdistdir}/tex/plain/base/story.tex
%{_texmfdistdir}/tex/plain/base/testfont.tex
%{_texmfdistdir}/tex/plain/base/webmac.tex
%{_texmfdistdir}/tex/plain/base/wlist.tex
%{_texmfdistdir}/tex/plain/config/aleph.ini
%{_texmfdistdir}/tex/plain/config/bplain.ini
%{_texmfdistdir}/tex/plain/config/dviluatex.ini
%{_texmfdistdir}/tex/plain/config/etex.ini
%{_texmfdistdir}/tex/plain/config/luatex.ini
%{_texmfdistdir}/tex/plain/config/omega.ini
%{_texmfdistdir}/tex/plain/config/pdfbplain.ini
%{_texmfdistdir}/tex/plain/config/pdfetex.ini
%{_texmfdistdir}/tex/plain/config/pdftexmagfix.tex
%{_texmfdistdir}/tex/plain/config/tex.ini
%{_texmfdistdir}/tex/plain/config/xetex.ini
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
