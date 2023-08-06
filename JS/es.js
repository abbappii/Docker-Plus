
// globalThis.setTimeout(()=> console.log("hello"), 100)

// let larg_num = Number.MAX_SAFE_INTEGER;
// larg_num += 1;
// larg_num = BigInt(larg_num) + 1n;

// console.log(larg_num)

// shorcart checking for object_
const language = {
    name: "Javascript",
    creator: "Brendon Eich",
    library: {
        react: {
            // company: "Facebook"
        }
    }
};

let company = language?.library?.react?.company; 
console.log(company);


// shorcart checking for Array 
let colors = ['red','green', 'blue']
console.log(colors?.[1]);


// coalesing operator ekottrito kora 
// ??

// null and undefined paile second operator er value return kore 


// Dynamic import 
(async function(){
    const {add} = await import('./utils.js');
    const { remove } = await import('./utils.js');

    add();
    remove();
})();