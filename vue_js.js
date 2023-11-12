const vue_js = Vue.createApp({
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

vue_js.mount('#vue_js')