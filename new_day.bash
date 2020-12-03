#!/bin/bash

current_dir=$(pwd)
amount_of_folders=$(ls | wc -l)

if [[ -z amount_of_folders ]]
then
    new_folder="1"
else
    last_folder=$(ls -rt1 | tail -1)
    let new_folder=last_folder+1
fi

mkdir ${new_folder}
cp ../solve-template.py ${new_folder}/solve.py
echo "" > ${new_folder}/input.txt
gedit ${new_folder}/input.txt
cd ${new_folder}
