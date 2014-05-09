all:
	latex ej_beamer.tex
	latex ej_beamer.tex
	bibtex ej_beamer
	latex ej_beamer.tex
	latex ej_beamer.tex
	dvips -o ej_beamer.ps ej_beamer.dvi
	ps2pdf -sPAPERSIZE=a4 -DMaxSubsetPct=100 -dCompatibilityLevel=1.2 -dSubsetFonts=true -dEmbedAllFonts=true ej_beamer.ps ej_beamer.pdf

clean:
	rm -f *.toc *.ps *.log *.lof *.lot *.dvi *.aux *.blg *.bbl
