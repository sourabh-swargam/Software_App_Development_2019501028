function countBs(word) {
	const letter = "B"
	let count = 0
	for (let i = 0; i < word.length; i++) {
		if (word[i] == letter) {
			count++
		}
	}
	return count
}


function countChar(word, letter) {
	let count = 0
	for (let i = 0; i < word.length; i++) {
		if (word[i] == letter) {
			count++
		}
	}
	return count
}


console.log(countBs("BBBWbOBBBRBDbbbB"))
console.log(countBs(""))
console.log(countBs("bbbBbbb"))


console.log(countChar("letter","t"))
console.log(countChar("temp","p"))
console.log(countChar("","w"))
