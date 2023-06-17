NAME := beipack-pybridge

$(NAME).pdf: $(NAME).md
	pandoc -t beamer -o $@ $<
	sed '/setbeameroption/ s/{.*notes/{show only notes/' $< | pandoc -t beamer -o $(NAME)-notes.pdf

.PHONY: app
app:
	+$(MAKE) -C app

install-beipack:
	sudo dnf install -y python3-setuptools python3-wheel
	sudo pip install --no-index --no-build-isolation -r app/requirements.txt

bots:
	git clone https://github.com/cockpit-project/bots/

clean:
	rm -f $(NAME)*.pdf bots

vms:
	[ -z "$$(virsh list --name)" ] || { echo "Stop all existing VMs for this demo" >&2; exit 1; }
	bots/image-download fedora-38 centos-9-stream
	./run-vms.py

# install the necessary tools to build this presentation
deps:
	which pandoc || sudo dnf install -y pandoc texlive-beamer texlive-collection-fontsrecommended

.PHONY: deps clean
