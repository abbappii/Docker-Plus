// Array.prototype.reduce()

// reduce main array change kore na
// purber state er value remind rakhe,
// can pass 4 parameter
// can set initial value for first indexedDB

// why it calls reduce function?
// answer: combine kore ekta result return kore

var numbers = [1,2,3,4,6,7];

var res = numbers.reduce((previousStateValue, CurrentStateValue, cIndex, arr) => {
    return previousStateValue + CurrentStateValue;
}, 0);

console.log(res)