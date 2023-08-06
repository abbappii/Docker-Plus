// destructuring 

// Object & Array 

// 1. Object
const user = {
    id: 22,
    name: "shahin",
    age: 26,
    dob: '23-04-96',
    degree: {
        ssc: 'jp',
        hsc: 'JpC',
        district:{
            title: "Joypurhat",
            code: 123
        }
    }
}

// ei object thke age ber kore new ekta variable e nibo 

const {degree:{district:{title: DistrictName}={}}={}} = user;

console.log(DistrictName)


// 2. Array 

let arr = [1,2,3,4,[44,55,66,77],5,6]

const [,,,,[,value1,,value2]] = arr;

console.log(value1, value2)


// Swap 

let f = 10, g=20;

[g,f] = [f,g]

console.log(f,g)