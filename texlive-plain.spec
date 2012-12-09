# revision 26647
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-plain
Version:	20120808
Release:	1
Summary:	TeXLive plain package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plain.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive plain package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120808-1
+ Revision: 812783
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.141592653-3
+ Revision: 754962
- Rebuild to reduce used resources

* Tue Nov 08 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.141592653-2
+ Revision: 729092
- texlive-plain

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.141592653-1
+ Revision: 719270
- texlive-plain
- texlive-plain
- texlive-plain
- texlive-plain

