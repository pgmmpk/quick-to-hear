DOCKER := docker run -it --rm --workdir /data -v$(PWD):/data minidocks/weasyprint

all: akathist.pdf

clean:
	rm -f *.pdf *.html

akathist.pdf: akathist.html common.css
	$(DOCKER) weasyprint -e utf-8 $< $@

akathist.html: akathist.md md2html.py
	python3 -m md2html akathist.md > akathist.html