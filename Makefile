download:
	mkdir ./eval
	cd ./eval; git clone https://github.com/lexibank/northeuralex.git; cd northeuralex; git checkout v4.0
	cd ./eval; git clone https://github.com/lexibank/lexibank-analysed.git; cd lexibank-analysed; git checkout v1.0

clear:
	rm -rf ./eval