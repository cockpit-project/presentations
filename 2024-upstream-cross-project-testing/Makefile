NAME := upstream-cross-project-testing

$(NAME).pdf: $(NAME).md
	pandoc -t beamer -o $@ $<
	sed '/setbeameroption/ s/{.*notes/{show only notes/' $< | pandoc -t beamer -o $(NAME)-notes.pdf

# install the necessary tools to build this presentation
deps:
	command -v pandoc || sudo dnf install -y pandoc texlive-beamer texlive-collection-fontsrecommended

.PHONY: deps clean
