init:
	pip install -r requirement.txt

install:
	sudo -H pip install ./

uninstall:
	sudo rm -rf /usr/local/lib/python2.7/dist-packages/pwmodel
	sudo rm -rf /usr/local/lib/python2.7/dist-packages/pwmodel-0.1-py2.7.egg-info

reinstall:
	sudo rm -rf /usr/local/lib/python2.7/dist-packages/pwmodel
	sudo rm -rf /usr/local/lib/python2.7/dist-packages/pwmodel-0.1-py2.7.egg-info
	sudo -H pip install ./
