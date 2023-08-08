
// eksate sob gulo promise return korbo 
// multiple then na niye
// const pro1 = Promise.resolve(`Promise 1 resolved.`)
const pro1 = new Promise((resolve, reject) =>{
    setTimeout(() => {
        resolve(`Promise 1 resolved.`)
    }, 5000);
})

const pro2 = new Promise((resolve, reject) =>{
    setTimeout(() => {
        resolve(`Promise 2 resolved.`)
    }, 2000);
})


// pro1.then(res => console.log(res))
// pro2.then(res => console.log(res))


Promise.race([pro1, pro2]).then(res => {
        console.log(res)
    });

