%global tl_name simurgh
%global tl_revision 31719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01b
Release:	%{tl_revision}.1
Summary:	Typeset Parsi in LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/simurgh
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simurgh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simurgh.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an automatic and unified interface for Parsi
typesetting in LaTeX, using the LuaTeX engine. The project to produce
this system is dedicated to Ferdowsi The Great.

