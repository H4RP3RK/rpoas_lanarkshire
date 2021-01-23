const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            active: false,
            current: ''
        };
    },
    methods: {
        toggle() {
            active = !active;
        }
        toggleButton(current) {
            if (current == 'location') {
                this.current == 'location';
                active = !active;
            }
        }
    }
});

app.mount('#gallery');