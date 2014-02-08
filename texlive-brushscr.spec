# revision 15878
# category Package
# catalog-ctan /fonts/brushscr
# catalog-date 2006-12-21 23:43:15 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-brushscr
Version:	20061221
Release:	3
Summary:	A handwriting script font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/brushscr
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brushscr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brushscr.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brushscr.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The BrushScript font is distributed in Adobe Type-1 format,
that simulates hand-written characters. The font is available
in italic shape only. The package includes the files needed by
LaTeX in order to use that font. The file AAA_readme.tex fully
describes the package and sample.tex illustrates its use.

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
%{_texmfdistdir}/fonts/type1/public/brushscr/BrushScriptX-Italic.pfb
%{_texmfdistdir}/fonts/vf/public/brushscr/pbsi8t.vf
%{_texmfdistdir}/tex/latex/brushscr/pbsi.sty
%{_texmfdistdir}/tex/latex/brushscr/t1pbsi.fd
%doc %{_texmfdistdir}/doc/latex/brushscr/AAA_readme.bbl
%doc %{_texmfdistdir}/doc/latex/brushscr/AAA_readme.blg
%doc %{_texmfdistdir}/doc/latex/brushscr/AAA_readme.dvi
%doc %{_texmfdistdir}/doc/latex/brushscr/AAA_readme.tex
%doc %{_texmfdistdir}/doc/latex/brushscr/README
%doc %{_texmfdistdir}/doc/latex/brushscr/example.dvi
%doc %{_texmfdistdir}/doc/latex/brushscr/example.tex
%doc %{_texmfdistdir}/doc/latex/brushscr/generate.tex
%doc %{_texmfdistdir}/doc/latex/brushscr/kern.txt
%doc %{_texmfdistdir}/doc/latex/brushscr/sample.dvi
%doc %{_texmfdistdir}/doc/latex/brushscr/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/brushscr/Makefile
%doc %{_texmfdistdir}/source/latex/brushscr/pbsi.mtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061221-2
+ Revision: 749889
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061221-1
+ Revision: 717986
- texlive-brushscr
- texlive-brushscr
- texlive-brushscr
- texlive-brushscr
- texlive-brushscr

