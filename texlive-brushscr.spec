# revision 28363
# category Package
# catalog-ctan /fonts/brushscr
# catalog-date 2012-10-18 12:56:21 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-brushscr
Version:	20180303
Release:	3
Summary:	A handwriting script font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/brushscr
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brushscr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brushscr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The BrushScript font simulates hand-written characters; it is
distributed in Adobe Type 1 format (but is available in italic
shape only). The package includes the files needed by LaTeX in
order to use that font. The file AAA_readme.tex fully describes
the package and sample.tex illustrates its use.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/brushscr/config.pbsi
%{_texmfdistdir}/fonts/afm/public/brushscr/BrushScriptX-Italic.afm
%{_texmfdistdir}/fonts/map/dvips/brushscr/pbsi.map
%{_texmfdistdir}/fonts/tfm/public/brushscr/pbsi.tfm
%{_texmfdistdir}/fonts/tfm/public/brushscr/pbsi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/brushscr/pbsi8t.tfm
%{_texmfdistdir}/fonts/type1/public/brushscr/BrushScriptX-Italic.pfa
%{_texmfdistdir}/fonts/vf/public/brushscr/pbsi8t.vf
%{_texmfdistdir}/tex/latex/brushscr/pbsi.sty
%{_texmfdistdir}/tex/latex/brushscr/t1pbsi.fd
%doc %{_texmfdistdir}/doc/fonts/brushscr/AAA_readme.tex
%doc %{_texmfdistdir}/doc/fonts/brushscr/Makefile
%doc %{_texmfdistdir}/doc/fonts/brushscr/README
%doc %{_texmfdistdir}/doc/fonts/brushscr/example.tex
%doc %{_texmfdistdir}/doc/fonts/brushscr/generate.tex
%doc %{_texmfdistdir}/doc/fonts/brushscr/kern.txt
%doc %{_texmfdistdir}/doc/fonts/brushscr/sample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex doc %{buildroot}%{_texmfdistdir}
