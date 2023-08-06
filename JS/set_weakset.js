
// console log func 
var log = (a) => console.log(a);

// Sets 
log(5)
// let myArr = new Array();
let mySet = new Set()

mySet.add(5);
mySet.add("bangla");
mySet.delete(5);
console.log(mySet.has(5));
// chain option in set
mySet.add(6).add(7).add(8) 
// mySet.clear()
log(mySet.size)
log(mySet)


// Now array to set 
let myArray = [1,2,3,4,5,6]
let setOfMy = new Set(myArray);

log(myArray)
log(setOfMy)


// set ki ki receive kore 
// iterable object 

// set theke array 
log([...mySet])
log(Array.from(mySet))


// set unique value return kore always
// array er element ke unique array korte set use kora jai
// set er union 
// set er Intersection
// set er diffrence 

let r = new Set([1,2,3])
let rr = new Set([2,3,4,5,2,3])

log(rr)
let union = new Set([...r, ...rr])

let intersection = new Set([...r].filter((x) => rr.has(x)))
/* new set a filter method use korate eita ekta arrow function 
nei r ekta ekta kore value 'x' diye check kore rr set er sathe */


// filter er moddhe ekta arrow function dite hoi
// and eita ekta ekta kore dei, amra ekta ekta kore element pabo

let diffrence = new Set([...r].filter(x=> !rr.has(x)))

log(union)
log(intersection)
log(diffrence)