const app = Vue.createApp({
    data() {
        return { 
            isActive: false,
        }
    },
    methods: {
        toggleBtn() {
            console.log("hellow world!"),
             this.isActive = !this.isActive
        },
    }
})

app.mount('#app')