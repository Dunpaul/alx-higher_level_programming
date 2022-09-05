#!/usr/bin/node
import { argv } from 'node:process';

// print process.argv
	argv.forEach((val, index) => {
		if(val){
			console.log('Argument found');
		} else {
			console.log('No argument');
	);
