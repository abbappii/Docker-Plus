
const hasMeeting = false;

const meeting = new Promise((resolve, reject) => {
    if (!hasMeeting){
        const meetingDetails = {
            name: "StandUp Morning meeting",
            location: "Google meet",
            time: "10:00 PM"
        };
        resolve(meetingDetails);
    }
    else{
        reject(new Error("meeting already scheduled!"));
    }
});

// it will get the pervious promise result 
// const addToCalenderPromise = (meetingDetails) =>{
//     return new Promise((resolve, reject) =>{
//         const calender = `${meetingDetails.name} scheduled on ${meetingDetails.location} at ${meetingDetails.time}`
//         resolve(calender)
//     });
// };

// more readable and concise code 
const addToCalenderPromise = (meetingDetails) =>{
    const calender = `${meetingDetails.name} scheduled on ${meetingDetails.location} at ${meetingDetails.time}`
    return Promise.resolve(calender);
};

meeting
    .then(
        addToCalenderPromise,
        console.log("first promise done.")
    )
    .then((res)=>{
        // resolve data 
        console.log("second promise just call.")
        console.log(res)
        // console.log(JSON.stringify(res));

    })
    .catch((err) => {
        // rejected data 
        console.log(err.message)
    })

