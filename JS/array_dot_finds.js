// array.prototype.find()


var n = [1,2,3,4,5,6]

var result = n.find(function(currentval, currentindex, arr){
    return currentval >4;
}, this);

console.log(n)
console.log(result)


var res = n.findIndex((curval, indx, arr) => {
    return !(curval % 2);
})

console.log(res)

//array.propotype.splice()
// songjukto kora 
// splice main array change kore new arry return kore


// array.push main array change kre 
    // array er last e add kore 
    // array.push last e jeta add kore oita return kore 