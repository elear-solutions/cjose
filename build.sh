#! /usr/bin/env bash

set -x

pwd

cd jansson

if [ $? -ne 0 ]; then
	git submodule add --force https://github.com/akheron/jansson.git
	git submodule init
	git submodule update	
	cd jansson	
fi

autoreconf -fsi

./configure CFLAGS="-fPIC"

make

sudo make install

sudo ldconfig

mkdir include
cp -v src/jansson.h src/jansson_config.h include/

cd ..

autoreconf -fsi

./configure

mkdir build/obj
cd build/obj
ar x /usr/local/lib/libjansson.a

cd ..

set +x

