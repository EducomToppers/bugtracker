<template>
  <div class="container">
    <form @submit="submit_login" method="post">
      <ul v-if="errors.length > 0" class="errors">
        <span class="error-description">Please resolve the following errors:</span>
        <li v-for="error, idx in errors" :key="idx" class="error">{{ error }}</li>
      </ul>
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" class="form-control" name="username" v-model="username">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input class="form-control" type="password" id="password" name="password" v-model="password">
      </div>
      <button type="submit" class="btn btn-primary">Log in</button>
    </form>
    <a class="btn-signup" href="/accounts/register">No account?, click here to register</a>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        username:'',
        password: '',
        errors: []
      };
    },
    methods: {
      async submit_login(e) {
        e.preventDefault();
        this.errors.length = 0;
        const axios = require('axios');
        
        // get a csrf token from the server first to block cross origin attacks
        const {data: csrftoken} = await axios.get('/accounts/csrf-token/');
        const config = {
          headers: {
            'X-CSRFToken': csrftoken
          }
        };
        const payload = {
          username: this.username,
          password: this.password,
        }
          const response = await axios.post("accounts/login/", payload, config)
            .catch(error => {
              if (error.response.status === 400) {
                this.errors = [...this.errors, error.response.data.error];
              } else if (error.response.status === 500) {
                this.errors = [...this.errors, "Server error"];
              }
          });
          if (response && response.status === 200) {
            localStorage.setItem('user', JSON.stringify(response.data));
            this.$router.push('/');
            this.$router.go('/');
          }
      }
    }
  }
</script>
<style scoped>
  .btn.btn-primary {
    margin-top: 20px;
  }
  .help-block {
    color: red;
  }
  .btn-signup {
    margin-top: 20px;
  }
  .errors {
    color: #d81d1d;
  }
  .error-description {
    font-size: 1.2rem;
  }
</style>
