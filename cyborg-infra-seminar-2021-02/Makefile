all: cyborg-infra-day-1.pdf cyborg-infra-day-2.pdf

cyborg-infra-day-1.pdf: cyborg-infra-day-1.md
	pandoc -t beamer -o $@ $<
	sed '/setbeameroption/ s/{.*notes/{show only notes/' $< | pandoc -t beamer -o cyborg-infra-day-1-notes.pdf -

cyborg-infra-day-2.pdf: cyborg-infra-day-2.md
	pandoc -t beamer -o $@ $<
	sed '/setbeameroption/ s/{.*notes/{show only notes/' $< | pandoc -t beamer -o cyborg-infra-day-2-notes.pdf -

clean:
	rm -f cyborg-infra-*.pdf

# install the necessary tools to build this presentation
deps:
	which pandoc || sudo dnf install -y pandoc texlive-beamer texlive-latex-bin texlive-collection-fontsrecommended texlive-hyphen-german texlive-hyphen-english texlive-dehyph texlive-fancyhdr texlive-dinbrief texlive-german texlive-a4wide texlive-ulem

.PHONY: deps clean
