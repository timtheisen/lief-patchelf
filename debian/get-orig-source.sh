#!/bin/bash
version=0.17.1
package=lief-patchelf
tdir=$(mktemp -d)
mkdir "${tdir}/${package}_${version}"
cp -a ../* "${tdir}/${package}_${version}/"
pushd "${tdir}" || exit
tar cfz "${package}_${version}.orig.tar.gz" "${package}_${version}"
popd || exit
mv "${tdir}/${package}_${version}.orig.tar.gz" ../..
