#!/bin/bash

current_dir=$(pwd)
amount_of_folders=$(ls | wc -l)

if [[ -z ${amount_of_folders} ]]
then
    new_folder="01"
else
    last_folder=$(ls -1 | tail -1 | cut -d '_' -f 1)
    let new_folder=last_folder+1
    new_folder=$(printf "%02d" ${new_folder})
fi

mkdir ${new_folder}
cp ../solve-template.py ${new_folder}/solve.py
echo "" > ${new_folder}/input.txt
gedit ${new_folder}/input.txt
cd ${new_folder}
