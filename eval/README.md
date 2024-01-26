# Replicate the Tests

Install all packages:

```bash
pip install -r requirements.txt
```

Make sure to download lexibank-analysed and clts:

```bash
cd .. # go to the main folder
git clone https://github.com/cldf-clts/clts
cd clts
git checkout v2.1.0
cd ..
cd ..
git clone https://github.com/lexibank/lexibank-analysed
cd lexibank-analysed
git checkout v1.0
```

Alternatively, this can be done by running the following two shorthand commands (from the main repository):

```shell
make init # download clts
make download # download lexibank
```

Then run all individual Python scripts at your convenience.

Figures were cropped with pdfcrop:

```bash
for i in *.pdf; do pdfcropt $i; done
```
