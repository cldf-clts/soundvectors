init:
	git clone https://github.com/cldf-clts/clts

download:
	cd ./eval; git clone https://github.com/lexibank/lexibank-analysed.git; cd lexibank-analysed; git checkout v1.0

clear:
	cd ./eval; rm -rf ./lexibank-analysed