function deepEqual(a, b) {

	if (typeof a === 'object' && typeof b === 'object') {

		let count = 0
		const aKeys = Object.keys(a)
		const bKeys = Object.keys(b)
		const aLen = aKeys.length
		const bLen = bKeys.length

		for (let i = 0; i < aLen; i++) {
		
			for (let j = 0; j < bLen; j++) {

				if (deepEqual(a[aKeys[i]], b[bKeys[j]])) {
					count++
					break
				}

			}
		}
		if (count === aLen && count === bLen)
			return true
		else 
			return false
	}
	else
		return a === b
}

const one = {
	1:'one',
	2:'two',
}

const two = {
	1:'one',
	2:'two',
}

const three = {
	1:'one',
	2:'two',
	inner: {
		key:"value"
	},
}

const four = {
	1:'one',
	2:'two',
	inner: {
		key:"value"
	},
}

const obj = {
	here: {
		is: "an"
	}, 
	object: 2
}

console.log(deepEqual(5, 5))
console.log(deepEqual(one, two))
console.log(deepEqual(one, three))
console.log(deepEqual(three, four))
console.log(deepEqual(obj, obj))
console.log(deepEqual(obj,{object: 2, here: {is: "an"}}))
