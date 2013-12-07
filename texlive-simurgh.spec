# revision 31719
# category Package
# catalog-ctan /macros/luatex/latex/simurgh
# catalog-date 2013-09-21 10:47:25 +0200
# catalog-license gpl2
# catalog-version 0.01b
Name:		texlive-simurgh
Version:	0.01b
Release:	3
Summary:	Typeset Parsi in LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/simurgh
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simurgh.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simurgh.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an automatic and unified interface for
Parsi typesetting in LaTeX, using the LuaTeX engine. The
project to produce this system is dedicated to Ferdowsi The
Great.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-abjad.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-adadi.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-algorithm.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-algorithmic.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-amsart.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-amsbook.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-amsmath.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-amstext.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-amsthm.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-array.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-article.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-artikel1.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-artikel2.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-artikel3.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-arydshln.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-backref.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-bidi.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-boek.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-boek3.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-book.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-bookest.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-caption3.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-char-def.lua
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-char-ini.lua
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-chkeng.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-clss.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-counters.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-cptns.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-doc.cls
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-empheq.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-extarticle.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-extbook.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-extletter.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-extreport.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-fleqn.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-fonts.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-footnotes.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-ftnxtra.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-glossaries.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-harfi.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-jalalical.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-leqno.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-letter.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-lettrine.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-loader.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-ltx.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-mathdigitspec.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-memoir.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-minitoc.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-natbib.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-pkgs.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-poem.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-rapport1.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-rapport3.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-refrep.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-report.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-scrartcl.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-scrbook.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-scrlettr.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-scrreprt.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-shellescape.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-tags.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-tartibi.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-tools.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-unibidi-core.lua
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-unibidi-ini.lua
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-unibidi-math.lua
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-unibidi.lua
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh-unibidi.sty
%{_texmfdistdir}/tex/lualatex/simurgh/simurgh.sty
%doc %{_texmfdistdir}/doc/lualatex/simurgh/ChangeLog
%doc %{_texmfdistdir}/doc/lualatex/simurgh/README.doc
%doc %{_texmfdistdir}/doc/lualatex/simurgh/simurgh-doc.pdf
%doc %{_texmfdistdir}/doc/lualatex/simurgh/simurgh-doc.tex
%doc %{_texmfdistdir}/doc/lualatex/simurgh/simurgh-logo.pdf
%doc %{_texmfdistdir}/doc/lualatex/simurgh/simurgh-logo.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
