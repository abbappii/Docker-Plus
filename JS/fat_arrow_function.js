

let num = (a , b) =>  a + b;
console.log(num(10, 15));

// arrow functions speciality
// simplify this keyword issue in function 

// Example---------------->
// 1.simple function use 
var javascript = {
    name: "hello",
    libraries: [
        'React','Angular', 'Vue'
    ],
    // this library will print own libraries 
    printlibraries: function (){
        console.log(this)
        // to solve this issue we can use this solution -:
        var self = this;
        // foreach prottek element er moddhe iteration korbe. ie: react,  vue ... 
        this.libraries.forEach(function (a){
            // console.log(this)
            console.log(`${this.name} loves ${a}`);
        })
    }
}

javascript.printlibraries()

// result 
// undefined loves React
// undefined loves Angular
// undefined loves Vue
// findings: foreach er function ekta alada call back func. so foreach er vetor er this r object er this alada. so result is undefined.
// foreach -> vetorer function bairer this ke change kore felce 


// Example 2 with fat arrow function 
var Js = {
    name: "hello",
    libraries: [
        'React','Angular', 'Vue'
    ],
    // this library will print own libraries 
    printlibraries: function (){
        // foreach prottek element er moddhe iteration korbe. ie: react,  vue ... 
        this.libraries.forEach((a) => {
            console.log(`${this.name} loves ${a}`);
        })
    }
}

Js.printlibraries()

// findings: arrow function this niye concern na 


// this is the main benifit of fat arrow function  :done;


// Tweaks: prottek ta function itself a constructor function. 