const takeorder = (customer, callback) =>{
    console.log(`take order for ${customer}`);
    callback(customer)
}
const processOrder = (customer, callback) => {
    console.log(`processing order for ${customer}`);

    setTimeout(()=>{
        console.log(`cooking completed.`)
        console.log(`take order from ${customer}`);

        callback(customer)
    }, 5000);
};

const completeOrder = (customer) => {
    console.log(`completed order from ${customer}`);
}

takeorder("customer 1 rakib.", (customer)=>{
    processOrder(customer, (customer)=>{
        completeOrder(customer)
    });
})


// Promise 
// promise use hoi kono ekta async operation er result ke handle korar jnno
// promise and callback are same 
// ********
// tailwind css
// react hook
// promise chain
// ********


// updated one:
// class Service(BaseModelWithUID):
//     title = models.CharField(max_length=255)
//     description = models.TextField(blank=True)
//     status = models.CharField(
//         max_length=20,
//         choices=ServiceStatus.choices,
//         default=ServiceStatus.DRAFT,
//         db_index=True,
//     )
//     is_preset = models.BooleanField(default=False)

//     # Custom Managers
//     objects = ServiceQuerySet.as_manager()

//     class Meta:
//         ordering = ["-created_at"]
//         verbose_name_plural = "Services"

//     def __str__(self):
//         return f"UID:{self.uid} Title: {self.title}"


// class OrganizationServiceConnector(BaseModelWithUID):
//     organization = models.ForeignKey("accountio.Organization", on_delete=models.CASCADE)
//     service = models.ForeignKey(Service, on_delete=models.CASCADE)

//     def __str__(self):
//         return f"Organization: {self.organization.name}, Service: {self.service.title}"