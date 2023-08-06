

function modifier(strings, ...values){
    // console.log(strings)
    // console.log(values)
    const m = strings.reduce((prev, current) =>{
        // console.log("previous val:",prev)
        // console.log("current val :",current)
        // // console.log("value       :",values.shift())
        // console.log("lengh of val:", values.length + " val " + values.shift())
        return prev + current + (values.length? "Mr. " + values.shift():"")
    },"")
    return m;
}

let a = 'ab';
let b = 'abc', c="def", d="dfg";

console.log(modifier`we have ${a} and ${b} in our string ${c} idk ${d}`)


// .reduce gives two params called previous and current state vlaue 
