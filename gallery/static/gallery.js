const app = Vue.createApp({
    data() {
        return {
            message: 'HEllo world'
        };
    },
    computed: {
        display() {
            if (active === false) {
                return {display: 'none'};
            } else {
                return {display: 'inline-block'};
            }
        }
    },
    methods: {
        toggle() {
            this.active = !this.active;
        }
    }
});

app.mount('#gallery');