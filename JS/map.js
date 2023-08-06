// Map 
// array.propotype.map()

// map new array return kore prottek ta element er sathe iterate kore 

// Example 
var numbers = [1,3,4,5,6,8]

var res = numbers.map((num)=>{
    console.log(num)
    return num + 2;
});

console.log(res)