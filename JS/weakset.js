

var log = (a) => console.log(a);

// Weakset

let weakSet = new WeakSet();
// weak set only accept object 
// primitive value not accpted
weakSet.add({"a":"bbb"});

log(weakSet)


class AnyClass{
    constructor(){
        weakSet.add(this);
    }
    method(){
        if (!weakSet.has(this)){
            throw new Error("Cannot access this method directly.")
        }else{
            return 'abcdefghij'
        }
    }
}

log(AnyClass.prototype.method())