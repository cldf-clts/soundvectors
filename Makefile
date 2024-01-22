download:
	cd resources/eval; git clone https://github.com/lexibank/northeuralex.git; cd northeuralex; git checkout v4.0
	cd resources/eval; git clone https://github.com/lexibank/lexibank-analysed.git; cd lexibank-analysed; git checkout v1.0

clear:
	cd resources/eval; rm -rf lexibank-analysed; rm -rf northeuralex